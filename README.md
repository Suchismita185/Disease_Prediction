# 🏥 Multiple Disease Prediction System

A comprehensive **Machine Learning web application** built with Streamlit for predicting three critical diseases:
- 🩺 **Diabetes Prediction** - Early detection based on metabolic markers
- ❤️ **Heart Disease Prediction** - Cardiac risk assessment
- 🫘 **Kidney Disease Prediction** - Renal health evaluation

## ✨ Features

- **3 Disease Prediction Models** - Pre-trained ML models for accurate predictions
- **Interactive Web Interface** - User-friendly Streamlit dashboard with intuitive navigation
- **Real-time Predictions** - Instant results with risk scores
- **Comprehensive Input Validation** - Robust error handling and input validation
- **Responsive Design** - Works seamlessly on desktop and mobile devices
- **Professional UI** - Clean, modern interface with visual feedback
- **Educational Purpose** - Includes disclaimers and health recommendations

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/Suchismita185/Disease_Prediction.git
cd Disease_Prediction
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Prepare Model Files

Place your pre-trained model files in the `saved_models/` directory:
- `saved_models/diabetes.pkl`
- `saved_models/heart.pkl`
- `saved_models/kidney.pkl`

If you don't have trained models, you can use the notebooks in `notebooks/` to train them on your datasets.

## 🎯 Usage

### Run the Application

```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

### Using the Application

1. **Select Disease** - Choose from the sidebar which disease you want to predict
2. **Enter Health Metrics** - Fill in all required medical parameters
3. **Get Prediction** - Click the prediction button to get risk assessment
4. **View Results** - See the prediction result with risk score percentage

## 📋 Disease Prediction Details

### 🩺 Diabetes Prediction

Enter the following health parameters:
- Number of Pregnancies
- Glucose Level (mg/dL)
- Blood Pressure (mmHg)
- Skin Thickness (mm)
- Insulin Level (µU/ml)
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age (years)

**Model Features:**
- BMI category classification
- Glucose level categorization
- Insulin level assessment

### ❤️ Heart Disease Prediction

Provide the following cardiac health metrics:
- Age (years)
- Sex (0=Female, 1=Male)
- Chest Pain Type (0-3)
- Resting Blood Pressure (mmHg)
- Serum Cholesterol (mg/dl)
- Fasting Blood Sugar > 120 (0/1)
- Resting Electrocardiographic Results (0-2)
- Maximum Heart Rate Achieved
- Exercise-Induced Angina (0/1)
- ST Depression Induced by Exercise
- Slope of ST Segment (0-2)
- Major Vessels Colored by Fluoroscopy (0-4)
- Thalassemia Type (0/1/2)

### 🫘 Kidney Disease Prediction

Input comprehensive renal health data:
- Age (years)
- Blood Pressure (mmHg)
- Specific Gravity
- Albumin (0-5)
- Sugar (0-5)
- Red Blood Cells (0/1)
- Pus Cells (0/1)
- Pus Cell Clumps (0/1)
- Bacteria (0/1)
- Blood Glucose Random (mg/dL)
- Blood Urea (mg/dL)
- Serum Creatinine (mg/dL)
- Sodium (mEq/L)
- Potassium (mEq/L)
- Hemoglobin (g/dL)
- Packed Cell Volume (%)
- WBC Count (cells/µL)
- RBC Count (millions/µL)
- Hypertension (0/1)
- Diabetes Mellitus (0/1)
- Coronary Artery Disease (0/1)
- Appetite (0/1)
- Pedal Edema (0/1)
- Anemia (0/1)

## 📁 Project Structure

```
Disease_Prediction/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── setup.py                    # Package configuration
├── README.md                   # This file
├── Procfile                    # Deployment configuration
├── saved_models/               # Pre-trained ML models (add your models here)
│   ├── diabetes.pkl
│   ├── heart.pkl
│   └── kidney.pkl
├── datasets/                   # Training datasets
└── notebooks/                  # Jupyter notebooks for model training
```

## 🔧 Technologies Used

- **Streamlit** (>=1.40.0) - Web framework for ML apps
- **scikit-learn** (>=1.5.0) - Machine Learning library
- **Pandas** (>=2.2.0) - Data manipulation
- **NumPy** (>=1.26.4) - Numerical computing
- **Matplotlib** (>=3.8.3) - Data visualization
- **Plotly** (>=5.18.0) - Interactive visualization
- **Joblib** (>=1.3.2) - Model serialization
- **Python-dotenv** (>=1.0.0) - Environment management

## 📊 Models Used

All three prediction models:
- Are pre-trained on medical datasets
- Use scikit-learn algorithms for classification
- Are optimized for healthcare prediction
- Use pickle format for serialization
- Include probability-based risk scoring

## ✅ Features & Improvements

### Latest Updates (v2.0.0)
- ✅ Comprehensive input validation with error handling
- ✅ Fixed typos and grammar issues throughout the codebase
- ✅ Improved code structure and organization
- ✅ Enhanced UI with better visual feedback
- ✅ Risk score percentage calculation
- ✅ Improved documentation and user guidance
- ✅ Updated setup.py with all dependencies
- ✅ Added Home page with feature overview
- ✅ Responsive design for all screen sizes
- ✅ Better error messages for user guidance
- ✅ Caching for model loading performance

### Fixed Issues
- ✅ Fixed typo: "Mulitple" → "Multiple"
- ✅ Fixed typo: "Cholestroal" → "Cholesterol"
- ✅ Fixed typo: "flourosopy" → "Fluoroscopy"
- ✅ Fixed typo: "reversable" → "Reversible"
- ✅ Fixed typo: "Appetitte" → "Appetite"
- ✅ Fixed typo: "aanemia" → "Anemia"
- ✅ Fixed typo: "kindey" → "Kidney"
- ✅ Fixed incorrect glucose label: "Overweight" → "PreDiabetic"
- ✅ Fixed result messages: "has diabetic" → "has diabetes"
- ✅ Added graceful error handling for missing model files
- ✅ Added input validation for all fields
- ✅ Removed hardcoded model loading (now with error handling)

## ⚠️ Important Disclaimer

**This application is for educational and informational purposes only.**

- ❌ Results are **NOT** a substitute for professional medical diagnosis
- ❌ Do not rely solely on this tool for medical decisions
- ✅ Always consult with qualified healthcare professionals
- ✅ Seek immediate medical attention for emergencies

## 🚨 When to Seek Emergency Help

If you experience any of the following, seek immediate medical attention:
- Chest pain or severe shortness of breath
- Difficulty urinating or severe abdominal pain
- Loss of consciousness or severe confusion
- Severe bleeding or injury

## 🤝 Contributing

Contributions are welcome! Here's how to help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

Please ensure:
- Code follows PEP 8 style guidelines
- All tests pass
- Documentation is updated
- Commit messages are descriptive

## 📄 License

This project is open source and available under the **MIT License**.

See LICENSE file for more details.

## 👤 Author

**Suchismita Bangal**
- GitHub: [@Suchismita185](https://github.com/Suchismita185)
- Email: suchismitabangal05@gmail.com

## 📧 Support & Contact

For questions, bug reports, or suggestions:
- Open an issue on [GitHub Issues](https://github.com/Suchismita185/Disease_Prediction/issues)
- Email: suchismitabangal05@gmail.com

## 🙏 Acknowledgments

- Streamlit for the amazing web framework
- scikit-learn for robust ML algorithms
- Healthcare community for inspiring this project

## 📈 Roadmap

- [ ] Add more disease prediction models
- [ ] Implement user authentication
- [ ] Add medical history tracking
- [ ] Create mobile app version
- [ ] Add multi-language support
- [ ] Implement data visualization dashboards
- [ ] Add API endpoints for integration

---

**Made with ❤️ for healthcare innovation**

*Last Updated: 2026*
