import os
import logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TF GPU warnings

from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import cv2
import io

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model('best_model.keras')
# Print model's expected input shape
print("Model's expected input shape:", model.input_shape)

def preprocess_image(image_bytes):
    try:
        # Convert bytes to numpy array
        nparr = np.frombuffer(image_bytes, np.uint8)
        # Decode image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # Convert BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Resize image
        img = cv2.resize(img, (64, 64))
        # Convert to float32 and normalize
        img = img.astype(np.float32) / 255.0
        
        print(f"Image shape before batch: {img.shape}")
        
        # Add batch dimension
        img = np.expand_dims(img, axis=0)
        
        print(f"Final image shape: {img.shape}")
        return img
        
    except Exception as e:
        print(f"Error in preprocessing: {str(e)}")
        raise

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Read the image file
        img_bytes = file.read()
        
        # Preprocess the image
        processed_image = preprocess_image(img_bytes)
        print(f"Image shape before prediction: {processed_image.shape}")
        
        # Check if input shape matches model's expected input shape
        if processed_image.shape[1:] != model.input_shape[1:]:
            return jsonify({'error': 'Input shape does not match model\'s expected input shape'}), 400
        
        # Make prediction
        prediction = model.predict(processed_image)
        print(f"Prediction output: {prediction}")
        
        # Get the predicted class
        predicted_class = "Infected" if prediction[0][0] > 0.5 else "Uninfected"
        confidence = float(prediction[0][0] if prediction[0][0] > 0.5 else 1 - prediction[0][0])
        
        return jsonify({
            'prediction': predicted_class,
            'confidence': f"{confidence * 100:.2f}%"
        })
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
