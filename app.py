from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import joblib
import cv2
import os
from datetime import datetime

app = Flask(__name__)

def load_required_files():
    global label_encoder, model, X_train, X_test, y_train, y_test
    label_encoder = joblib.load('label_encoder.pkl')
    model = joblib.load('model.pkl')
    X_train = np.load('X_train.npy')
    X_test = np.load('X_test.npy')
    y_train = np.load('y_train.npy')
    y_test = np.load('y_test.npy')

load_required_files()

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def extract_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        face = image[y:y + h, x:x + w]
        return cv2.resize(face, (128, 128))
    return None

@app.route('/')
def home():
    names = ["John Doe", "Jane Smith"]
    rolls = ["12345", "67890"]
    times = ["09:00 AM", "09:05 AM"]
    l = len(names)
    totalreg = len(np.unique(y_train))
    datetoday2 = datetime.today().strftime('%Y-%m-%d')
    return render_template("home.html", names=names, rolls=rolls, times=times, l=l, totalreg=totalreg, datetoday2=datetoday2, zip=zip)

@app.route('/listusers')
def list_users():
    unique_labels = np.unique(y_train)
    names = label_encoder.inverse_transform(unique_labels)
    data = []
    count = 1
    for name in names : 
        data.append((count, name))
        count += 1
    return render_template("listusers.html", data=data)

@app.route('/reload')
def reload():
    load_required_files()
    return "Files reloaded successfully."

@app.route('/start')
def start_attendance():
    if not os.path.exists('sample_images'):
        os.makedirs('sample_images')

    indices = np.random.choice(X_test.shape[0], 50, replace=False)
    sampled_X = X_test[indices]
    sampled_y = y_test[indices]
    
    print("Predicting names...")
    predicted_labels = model.predict(sampled_X)
    predicted_names = label_encoder.inverse_transform(predicted_labels)

    current_time = datetime.now().strftime("%H:%M %p")
    count = 1
    attendance = []
    for i, (image, name) in enumerate(zip(sampled_X, predicted_names)):
        # Reshape image to (128, 128, 3) if necessary
        if image.shape[-1] != 3:
            image = np.stack((image,) * 3, axis=-1)
        
        face_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to correct color format
        file_path = os.path.join('sample_images', f'{name}_{count}.jpg')
        cv2.imwrite(file_path, face_image)
        
        attendance.append((name, current_time, count))
        count += 1
    print("Done predicting")
    print(attendance)

    return render_template("attendance.html", attendance=attendance)

if __name__ == '__main__':
    app.run(debug=True)
