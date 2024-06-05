import os
import numpy as np
import cv2
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib
import argparse

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def extract_face(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        face = image[y:y + h, x:x + w]
        return cv2.resize(face, (128, 128))  
    return None

def process_images(image_dir, limit):
    X, y = [], []
    for person_name in os.listdir(image_dir):
        person_dir = os.path.join(image_dir, person_name)
        if not os.path.isdir(person_dir):
            continue
        image_files = os.listdir(person_dir)[:limit]  
        for image_name in image_files:
            image_path = os.path.join(person_dir, image_name)
            face = extract_face(image_path)
            if face is not None:
                X.append(face)
                y.append(person_name)
    return np.array(X), np.array(y)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess face images")
    parser.add_argument('--limit', type=int, default=50, help="Limit the number of images processed per person")
    args = parser.parse_args()

    image_dir = r'static\dataset\lfw-deepfunneled\lfw-deepfunneled'
    X, y = process_images(image_dir, args.limit)

    X = X.reshape(X.shape[0], -1)

    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    joblib.dump(label_encoder, 'label_encoder.pkl')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    joblib.dump(model, 'model.pkl')

    np.save('X_train.npy', X_train)
    np.save('X_test.npy', X_test)
    np.save('y_train.npy', y_train)
    np.save('y_test.npy', y_test)

    print("Preprocessing complete. Data and model saved.")
