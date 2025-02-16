# -*- coding: utf-8 -*-
"""CNN AND RNN TESTING

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18zJz-janp7dDENUQPy5uE5ylKXjs8ZYG
"""

from google.colab import drive
import os

# Step 1: Mount Google Drive
drive.mount('/content/drive')

# Step 2: Specify the folder path
# Update 'your-folder-path' with the path to your folder in Google Drive.
folder_path = '/content/drive/My Drive/FINAL_CODE_EMO_R_A ORIGINAL - Copy'

# Step 3: Check and load files from the folder
if os.path.exists(folder_path):
    print(f"Folder '{folder_path}' contents:")
    for file_name in os.listdir(folder_path):
        print(file_name)
else:
    print(f"The folder '{folder_path}' does not exist.")

from google.colab import drive
import os

# Step 1: Mount Google Drive
drive.mount('/content/drive')

# Step 2: Specify the folder path in Google Drive
# Replace 'your-folder-path' with the actual folder path in your Google Drive
folder_path = '/content/drive/My Drive/FINAL_CODE_EMO_R_A ORIGINAL - Copy'

# Step 3: Check and list all files in the folder
if os.path.exists(folder_path):
    print(f"Files in '{folder_path}':")
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        print(file_path)  # Print the full path of each file

        # Example: Load each file based on its type
        if file_name.endswith('.csv'):
            import pandas as pd
            data = pd.read_csv(file_path)
            print(f"Loaded CSV file: {file_name}")
            print(data.head())  # Display first few rows

        elif file_name.endswith(('.jpg', '.png')):
            from PIL import Image
            image = Image.open(file_path)
            print(f"Loaded Image file: {file_name}")
            # Display image size as an example
            print(f"Image size: {image.size}")

        elif file_name.endswith('.txt'):
            with open(file_path, 'r') as file:
                content = file.read()
                print(f"Loaded Text file: {file_name}")
                print(content[:100])  # Display first 100 characters

else:
    print(f"The folder '{folder_path}' does not exist.")

from google.colab import drive
import os

# Step 1: Mount Google Drive
drive.mount('/content/drive')

# Step 2: Specify the file path
# Replace 'your-file-path' with the actual path to the file in your Google Drive
file_path = '/content/drive/My Drive/FINAL_CODE_EMO_R_A ORIGINAL - Copy/CNN/test.ipynb'

# Step 3: Check if the file exists and open it
if os.path.exists(file_path):
    print(f"Opening file: {file_path}")

    # Example: Handling the file based on its type
    if file_path.endswith('.csv'):
        import pandas as pd
        data = pd.read_csv(file_path)
        print(f"Loaded CSV file:\n{data.head()}")

    elif file_path.endswith(('.jpg', '.png')):
        from PIL import Image
        image = Image.open(file_path)
        image.show()
        print(f"Image size: {image.size}")

    elif file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Text file content:\n{content[:500]}")  # Display first 500 characters

    else:
        print(f"File type not recognized for file: {file_path}")
else:
    print(f"The file '{file_path}' does not exist.")

#CNN
import os
import numpy as np
import librosa
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib  # For saving and loading the label encoder

# Function to load and preprocess audio data
def load_data(dataset_path):
    features = []  # List to store feature vectors
    labels = []    # List to store corresponding labels
    for emotion in os.listdir(dataset_path):
        emotion_path = os.path.join(dataset_path, emotion)
        if os.path.isdir(emotion_path):
            for file in os.listdir(emotion_path):
                if file.endswith('.wav'):
                    file_path = os.path.join(emotion_path, file)
                    audio, sr = librosa.load(file_path, sr=None)  # Load audio file
                    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)  # Extract MFCC features
                    mfcc_scaled = np.mean(mfcc.T, axis=0)  # Average MFCC coefficients
                    features.append(mfcc_scaled)
                    labels.append(emotion)
    return np.array(features), np.array(labels)

# Define the path to your dataset
dataset_path = r'/content/drive/My Drive/FINAL_CODE_EMO_R_A ORIGINAL - Copy/DATASET/Tess/'

# Load the dataset
X, y = load_data(dataset_path)

# Encode the labels into numerical format
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Reshape the data to fit the input requirements of a CNN
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# Build the CNN model using Conv1D layers
model = tf.keras.Sequential([
    tf.keras.layers.Conv1D(32, kernel_size=3, activation='relu', input_shape=(X_train.shape[1], 1), padding='same'),
    tf.keras.layers.MaxPooling1D(pool_size=2),
    tf.keras.layers.Conv1D(64, kernel_size=3, activation='relu', padding='same'),
    tf.keras.layers.MaxPooling1D(pool_size=2),
    tf.keras.layers.Conv1D(128, kernel_size=3, activation='relu', padding='same'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(label_encoder.classes_), activation='softmax')
])

# Compile the model with Adam optimizer and sparse categorical crossentropy loss
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Early stopping callback
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Train the model on the training data
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test), callbacks=[early_stopping])

# Save the trained model
model.save('emotion_detection_model.h5')
print('Model saved to disk.')

# Save the label encoder
label_encoder_path = 'label_encoder.pkl'
joblib.dump(label_encoder, label_encoder_path)
print(f'Label encoder saved to {label_encoder_path}.')

# Evaluate the model on the test data
y_pred = np.argmax(model.predict(X_test), axis=1)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Function to make predictions on new data
def predict_emotion(file_path, model, label_encoder):
    # Load the audio file
    audio, sr = librosa.load(file_path, sr=None)
    # Extract MFCC features
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    # Compute the mean of MFCC coefficients
    mfcc_scaled = np.mean(mfcc.T, axis=0)
    # Reshape the input to match the model's input shape
    input_data = mfcc_scaled.reshape(1, mfcc_scaled.shape[0], 1)
    # Make prediction
    prediction = model.predict(input_data)
    # Get the class with highest probability
    predicted_class = np.argmax(prediction, axis=1)[0]
    # Decode the class label
    predicted_label = label_encoder.classes_[predicted_class]
    return predicted_label

# Example usage:
# Replace 'path_to_new_audio_file.wav' with the path to an actual WAV file
new_file_path = r'/content/drive/My Drive/FINAL_CODE_EMO_R_A ORIGINAL - Copy/DATASET/Tess/OAF_angry/OAF_back_angry.wav'
predicted_emotion = predict_emotion(new_file_path, model, label_encoder)
print(f'Predicted emotion: {predicted_emotion}')

#RNN
import os
import numpy as np
import librosa
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib  # For saving and loading the label encoder

# Function to load and preprocess audio data
def load_data(dataset_path):
    features = []  # List to store feature vectors
    labels = []    # List to store corresponding labels
    for emotion in os.listdir(dataset_path):
        emotion_path = os.path.join(dataset_path, emotion)
        if os.path.isdir(emotion_path):
            for file in os.listdir(emotion_path):
                if file.endswith('.wav'):
                    file_path = os.path.join(emotion_path, file)
                    audio, sr = librosa.load(file_path, sr=None)  # Load audio file
                    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)  # Extract MFCC features
                    mfcc_scaled = np.mean(mfcc.T, axis=0)  # Average MFCC coefficients
                    features.append(mfcc_scaled)
                    labels.append(emotion)
    return np.array(features), np.array(labels)

# Define the path to your dataset
dataset_path = r'/content/drive/My Drive/FINAL_CODE_EMO_R_A ORIGINAL - Copy/DATASET/Tess/'

# Load the dataset
X, y = load_data(dataset_path)

# Encode the labels into numerical format
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Feature Standardization
X_train = (X_train - np.mean(X_train, axis=0)) / np.std(X_train, axis=0)
X_test = (X_test - np.mean(X_test, axis=0)) / np.std(X_test, axis=0)

# Reshape the data to fit the input requirements of an RNN (LSTM layer)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# Build the RNN model using LSTM layers
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(128, return_sequences=True, input_shape=(X_train.shape[1], 1)),  # LSTM layer
    tf.keras.layers.LSTM(128, return_sequences=False),  # LSTM layer
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(len(label_encoder.classes_), activation='softmax')
])

# Compile the model with Adam optimizer and sparse categorical crossentropy loss
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Define EarlyStopping callback
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_accuracy', patience=10, verbose=1, restore_best_weights=True)

# Train the model on the training data
model.fit(X_train, y_train, epochs=150, batch_size=64, validation_data=(X_test, y_test), callbacks=[early_stopping])

# Save the trained model
model.save('emotion_detection_model_rnn.h5')
print('Model saved to disk.')

# Save the label encoder
label_encoder_path = 'label_encoder.pkl'
joblib.dump(label_encoder, label_encoder_path)
print(f'Label encoder saved to {label_encoder_path}.')

# Evaluate the model on the test data
y_pred = np.argmax(model.predict(X_test), axis=1)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Print the classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

import numpy as np
import librosa
import tensorflow as tf
import joblib

# Function to preprocess a single audio file
def preprocess_audio(file_path):
    audio, sr = librosa.load(file_path, sr=None)  # Load audio file
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)  # Extract MFCC features
    mfcc_scaled = np.mean(mfcc.T, axis=0)  # Average MFCC coefficients
    return mfcc_scaled

# Load the saved model
model = tf.keras.models.load_model('emotion_detection_model_rnn.h5')
print("Model loaded successfully.")

# Load the saved label encoder
label_encoder = joblib.load('label_encoder.pkl')
print("Label encoder loaded successfully.")

# Function to make predictions
def predict_emotion(audio_file):
    # Preprocess the audio file
    features = preprocess_audio(audio_file)

    # Standardize the features (assuming training mean/std was 0 and 1)
    features = (features - np.mean(features)) / np.std(features)

    # Reshape to match the model input
    features = features.reshape(1, -1, 1)

    # Make predictions
    prediction = model.predict(features)
    predicted_label_index = np.argmax(prediction)

    # Decode the label
    predicted_emotion = label_encoder.inverse_transform([predicted_label_index])[0]

    return predicted_emotion

# Test the prediction function with an example audio file
audio_file_path = r'/content/drive/My Drive/FINAL_CODE_EMO_R_A ORIGINAL - Copy/DATASET/Tess/OAF_angry/OAF_back_angry.wav'
predicted_emotion = predict_emotion(audio_file_path)

print(f"The predicted emotion for the audio file is: {predicted_emotion}")