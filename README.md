# 🏥 Multiple Disease Prediction System

A comprehensive **Machine Learning web application** built with Streamlit for predicting three critical diseases:
- 🩺 **Diabetes Prediction**
- ❤️ **Heart Disease Prediction**
- 🫘 **Kidney Disease Prediction**

## 📋 Features

- **3 Disease Prediction Models** - Pre-trained ML models for accurate predictions
- **Interactive Web Interface** - User-friendly Streamlit dashboard
- **Real-time Predictions** - Instant results based on medical parameters
- **Responsive Design** - Works seamlessly on desktop and mobile devices

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Suchismita185/Disease_Prediction.git
cd Disease_Prediction
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## 🎯 Usage

Run the Streamlit app locally:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Diabetes Prediction
Enter the following health parameters:
- Number of Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Value
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

### Heart Disease Prediction
Provide cardiac health metrics:
- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Serum Cholesterol
- Fasting Blood Sugar
- Resting Electrocardiographic Results
- Maximum Heart Rate
- Exercise-Induced Angina
- ST Depression
- Slope of ST Segment
- Major Vessels Colored by Fluoroscopy
- Thalassemia Status

### Kidney Disease Prediction
Input comprehensive renal health data:
- Age
- Blood Pressure
- Specific Gravity
- Albumin
- Sugar
- Red Blood Cells
- Pus Cells
- Bacteria
- Blood Glucose
- Blood Urea
- Serum Creatinine
- Sodium & Potassium Levels
- Hemoglobin
- Blood Cell Counts
- Pre-existing Conditions (Hypertension, Diabetes, CAD)
- And more...

## 📁 Project Structure
```
Disease_Prediction/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── saved_models/         # Pre-trained ML models
│   ├── diabetes.pkl
│   ├── heart.pkl
│   └── kidney.pkl
├── datasets/             # Training datasets
├── notebooks/            # Jupyter notebooks for model training
└── README.md            # This file
```

## 🔧 Technologies Used
- **Streamlit** - Web framework for building ML apps
- **scikit-learn** - Machine Learning library
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Pickle** - Model serialization

## 📊 Models Used
All three prediction models are:
- Pre-trained on medical datasets
- Optimized using scikit-learn
- Serialized as pickle files for quick loading
- Evaluated for accuracy and reliability

## ⚠️ Disclaimer
**This application is for educational and informational purposes only.**
- Results are NOT a substitute for professional medical diagnosis
- Always consult with qualified healthcare professionals
- Do not rely solely on this tool for medical decisions

## 🤝 Contributing
Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## 📄 License
This project is open source and available under the MIT License.

## 👤 Author
**Suchismita185** - [GitHub Profile](https://github.com/Suchismita185)

## 📧 Contact & Support
For questions or support, please open an issue on GitHub.

---

**Made with ❤️ for healthcare innovation**
