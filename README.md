# Face Recognition Attendance System

## Overview
The Face Recognition Attendance System is a Python-based application designed to streamline the process of taking attendance using facial recognition technology. This system offers two main features:

1. **Attendance Taking:** This feature allows users to capture the faces of individuals and record their attendance automatically. The system detects faces using a webcam or uploaded images, matches them against a pre-existing database, and logs the attendance details.

2. **User Listing:** Users can view a list of registered individuals along with their unique identifiers, such as names and roll numbers. This feature provides an overview of the individuals stored in the system's database.

## Images
### Home page
> 
### User List Page
> 
### Attendance Page
> 

## Working
1. **Recording Attendance:**
- Users start the attendance process by choosing the "Take Attendance" option.
- The user is asked by the system to either take photos of people with a webcam or upload images from a local folder.
- Facial recognition algorithms review the captured images and compare them to the current database for matches.
After successfully identifying the individual, the system logs the attendance information, such as their name and the time they arrived.

2. **List of Users:**
- To see the people who have signed up, users can choose the "List Users" feature.
- The data from the database is fetched by the system and presented in an organized way, usually in the form of a table layout.
Users have the ability to examine the roster of people and their pertinent details, like names and distinct identifiers.

## Dataset
The dataset for the Face Recognition Attendance App is taken from kaggle. A popular dataset Labelled Faces in the wild which contains images of around 5000 individuals and around 13000 images. One can find the dataset [here](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset)   

## Installation
To run the Face Recognition Attendance System, follow these steps:
1. Install the required dependencies listed in the `requirements.txt` file.
2. Run the main application file, typically named `app.py` or `main.py`.


# Usage

## Running the Application

To run the Face Recognition Attendance System, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/face-recognition-attendance-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd face-recognition-attendance-system
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the main application file:

    ```bash
    python app.py
    ```

5. Once the application is running, you can access it via your web browser at [http://localhost:5000](http://localhost:5000).

## Using the Features

### Attendance Taking

1. Click on the "Take Attendance" option in the navigation menu.

2. Follow the on-screen instructions to capture images of individuals using your webcam or upload images from your local directory.

3. The system will process the images and log the attendance details for recognized individuals.

### User Listing

1. Click on the "List Users" option in the navigation menu.

2. The system will display a list of registered individuals along with their relevant information, such as names and roll numbers.

3. You can review the list of users and their details on the screen.


## Contributing
Contributions to the project are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request or open an issue on GitHub.

## License
This project is licensed under the [MIT License](LICENSE).
