# 🌿 Plant Leaf Disease Detection using Transfer Learning

An AI-powered web application that detects plant leaf diseases from images using **EfficientNetB0 Transfer Learning**. The application provides disease prediction, confidence score, symptoms, treatment recommendations, and prevention tips through an easy-to-use Streamlit interface.

---

## 🚀 Live Demo

🔗 https://plantleaf-disease-detection-ai.streamlit.app/

---

## 📌 Project Overview

Plant diseases significantly reduce crop yield and quality. Early disease detection helps farmers take timely action and minimize losses.

This project uses **Deep Learning** with **EfficientNetB0** to classify plant leaf images into **38 disease categories** from the PlantVillage dataset.

After prediction, the application displays:

- Disease Name
- Confidence Score
- Disease Description
- Symptoms
- Organic Treatment
- Chemical Treatment
- Prevention Methods

---

## ✨ Features

- 🌱 Detects **38 Plant Leaf Disease Classes**
- 🧠 EfficientNetB0 Transfer Learning
- 📷 Upload Leaf Image
- 📊 Confidence Score
- 📖 Disease Description
- 🌿 Organic Treatment Suggestions
- 💊 Chemical Treatment Recommendations
- 🛡 Prevention Tips
- 🌍 English & Hindi Language Support
- ☁️ Deployed on Streamlit Cloud

---

## 🧠 Model Architecture

- Base Model: EfficientNetB0
- Framework: TensorFlow & Keras
- Transfer Learning
- Fine-Tuning
- Image Size: 224 × 224
- Dataset: PlantVillage

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Validation Accuracy | **96.72%** |
| Classes | 38 |
| Architecture | EfficientNetB0 |
| Framework | TensorFlow/Keras |

---

## 🖼️ Application Preview

### Home Page

*(Screenshot will be added)*

### Upload Image

*(Screenshot will be added)*

### Prediction Result

*(Screenshot will be added)*

---

## 📂 Project Structure

```text
PlantLeaf-Disease-Detection/
│
├── app.py
├── predict.py
├── disease_info.py
├── requirements.txt
├── README.md
├── notebooks/
│   └── Plant_Leaf_Disease_Training.ipynb
├── model/
│   ├── best_plant_model.keras
│   └── class_indices.json
└── assets/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/adityaraj9934/PlantLeaf-Disease-Detection.git
```

Move into the project directory

```bash
cd PlantLeaf-Disease-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- EfficientNetB0
- Streamlit
- NumPy
- Pillow
- Git
- GitHub

---

## 📚 Dataset

**PlantVillage Dataset**

- 38 Plant Disease Classes
- Thousands of labeled leaf images
- Used for supervised image classification

---

## 🔮 Future Improvements

- Grad-CAM Visualization
- Multi-language Support
- Mobile Application
- Real-time Camera Detection
- Fertilizer Recommendation
- Weather-based Disease Advisory

---

## 👨‍💻 Author

**Aditya Raj**

MCA (Data Science)  
National Institute of Technology Patna

GitHub: https://github.com/adityaraj9934

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
