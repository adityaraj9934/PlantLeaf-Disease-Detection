import json
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.efficientnet import preprocess_input

# Load the trained model (loads only once when the app starts)
model = load_model("model/best_plant_model.keras")

# Load class indices
with open("model/class_indices.json", "r") as f:
    class_indices = json.load(f)


    # Reverse the dictionary: index -> class name
idx_to_class = {value: key for key, value in class_indices.items()}

def predict_image(image):
    # Resize image to the size expected by EfficientNetB0
    image = image.resize((224, 224))

    # Convert image to RGB (ensures 3 color channels)
    image = image.convert("RGB")

    # Convert PIL image to NumPy array
    image = np.array(image)

    # Apply EfficientNet preprocessing
    image = preprocess_input(image)

    # Add batch dimension (1, 224, 224, 3)
    image = np.expand_dims(image, axis=0)

    # Predict probabilities for all classes
    predictions = model.predict(image)

    # Get the index of the class with highest probability
    predicted_index = np.argmax(predictions)

    # Get confidence score
    confidence = float(np.max(predictions))

    # Convert class index to disease name
    predicted_class = idx_to_class[predicted_index]

    # Return both disease name and confidence
    return predicted_class, confidence