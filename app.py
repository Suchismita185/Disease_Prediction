import streamlit as st
import pickle
import os
import sys
from pathlib import Path
from streamlit_option_menu import option_menu
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Multiple Disease Prediction",
    layout="wide",
    page_icon="🏥",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .stAlert {
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .result-success {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }
    .result-danger {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }
    </style>
    """, unsafe_allow_html=True)

# Define model paths
MODEL_DIR = Path("saved_models")
DIABETES_MODEL_PATH = MODEL_DIR / "diabetes.pkl"
HEART_MODEL_PATH = MODEL_DIR / "heart.pkl"
KIDNEY_MODEL_PATH = MODEL_DIR / "kidney.pkl"

@st.cache_resource
def load_models():
    """Load all ML models with error handling"""
    models = {}
    
    try:
        if DIABETES_MODEL_PATH.exists():
            with open(DIABETES_MODEL_PATH, 'rb') as f:
                models['diabetes'] = pickle.load(f)
        else:
            st.warning(f"⚠️ Diabetes model not found at {DIABETES_MODEL_PATH}")
    except Exception as e:
        st.error(f"Error loading diabetes model: {str(e)}")
    
    try:
        if HEART_MODEL_PATH.exists():
            with open(HEART_MODEL_PATH, 'rb') as f:
                models['heart'] = pickle.load(f)
        else:
            st.warning(f"⚠️ Heart model not found at {HEART_MODEL_PATH}")
    except Exception as e:
        st.error(f"Error loading heart model: {str(e)}")
    
    try:
        if KIDNEY_MODEL_PATH.exists():
            with open(KIDNEY_MODEL_PATH, 'rb') as f:
                models['kidney'] = pickle.load(f)
        else:
            st.warning(f"⚠️ Kidney model not found at {KIDNEY_MODEL_PATH}")
    except Exception as e:
        st.error(f"Error loading kidney model: {str(e)}")
    
    return models

def validate_input(value, field_name):
    """Validate and convert input to float with error handling"""
    try:
        float_value = float(value)
        if float_value < 0:
            return None, f"❌ {field_name} cannot be negative"
        return float_value, None
    except ValueError:
        return None, f"❌ {field_name} must be a valid number"

def calculate_bmi_category(bmi):
    """Calculate BMI category features"""
    features = {
        'underweight': 1 if bmi <= 18.5 else 0,
        'normal': 1 if 18.5 < bmi <= 24.9 else 0,
        'overweight': 1 if 24.9 < bmi <= 29.9 else 0,
        'obese_class1': 1 if 29.9 < bmi <= 34.9 else 0,
        'obese_class2': 1 if 34.9 < bmi <= 39.9 else 0,
        'obese_class3': 1 if bmi > 39.9 else 0
    }
    return features

def calculate_glucose_category(glucose):
    """Calculate glucose level category features"""
    features = {
        'low': 1 if glucose <= 70 else 0,
        'normal': 1 if 70 < glucose <= 99 else 0,
        'prediabetic': 1 if 99 < glucose <= 126 else 0,
        'diabetic': 1 if glucose > 126 else 0
    }
    return features

def calculate_insulin_category(insulin):
    """Calculate insulin level category features"""
    return 1 if 16 <= insulin <= 166 else 0

# Load models
models = load_models()

# Sidebar navigation
with st.sidebar:
    st.markdown("### 🏥 Disease Prediction System")
    selected = option_menu(
        "Select Disease",
        ['Home', 'Diabetes Prediction', 'Heart Disease Prediction', 'Kidney Disease Prediction'],
        menu_icon='hospital-fill',
        icons=['house', 'activity', 'heart', 'person'],
        default_index=0
    )
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.info(
        "This application uses Machine Learning models to predict disease risk based on medical parameters. "
        "**Always consult healthcare professionals for accurate diagnosis.**"
    )

# Home Page
if selected == 'Home':
    st.markdown("# 🏥 Multiple Disease Prediction System")
    st.markdown("""
    Welcome to the comprehensive disease prediction system. This application uses machine learning 
    to help assess the risk of three critical health conditions:
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🩺 Diabetes")
        st.write(
            "Predict diabetes risk based on medical metrics including glucose levels, "
            "BMI, and family history."
        )
    
    with col2:
        st.markdown("### ❤️ Heart Disease")
        st.write(
            "Assess heart disease risk using cardiac health indicators like blood pressure, "
            "cholesterol, and heart rate."
        )
    
    with col3:
        st.markdown("### 🫘 Kidney Disease")
        st.write(
            "Evaluate kidney disease risk through comprehensive renal health parameters "
            "and blood chemistry indicators."
        )
    
    st.markdown("---")
    st.warning(
        "⚠️ **Disclaimer**: This application is for educational purposes only. "
        "Results are NOT a substitute for professional medical diagnosis. "
        "Always consult qualified healthcare professionals."
    )

# Diabetes Prediction
elif selected == 'Diabetes Prediction':
    st.title("🩺 Diabetes Prediction")
    
    if 'diabetes' not in models:
        st.error("❌ Diabetes model is not available. Please ensure the model file exists.")
    else:
        st.markdown(
            "Enter your health metrics to predict diabetes risk. All fields are required."
        )
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            pregnancies = st.text_input("Number of Pregnancies", value="0")
        with col2:
            glucose = st.text_input("Glucose Level (mg/dL)", value="")
        with col3:
            blood_pressure = st.text_input("Blood Pressure (mmHg)", value="")
        
        with col1:
            skin_thickness = st.text_input("Skin Thickness (mm)", value="")
        with col2:
            insulin = st.text_input("Insulin Level (µU/ml)", value="")
        with col3:
            bmi = st.text_input("BMI (Body Mass Index)", value="")
        
        with col1:
            dpf = st.text_input("Diabetes Pedigree Function", value="")
        with col2:
            age = st.text_input("Age (years)", value="")
        
        diabetes_result = ""
        
        if st.button("🔍 Get Prediction", key="diabetes_btn"):
            # Validate all inputs
            errors = []
            
            pregnancies_val, err = validate_input(pregnancies, "Pregnancies")
            if err:
                errors.append(err)
            
            glucose_val, err = validate_input(glucose, "Glucose")
            if err:
                errors.append(err)
            
            bp_val, err = validate_input(blood_pressure, "Blood Pressure")
            if err:
                errors.append(err)
            
            skin_val, err = validate_input(skin_thickness, "Skin Thickness")
            if err:
                errors.append(err)
            
            insulin_val, err = validate_input(insulin, "Insulin")
            if err:
                errors.append(err)
            
            bmi_val, err = validate_input(bmi, "BMI")
            if err:
                errors.append(err)
            
            dpf_val, err = validate_input(dpf, "Diabetes Pedigree Function")
            if err:
                errors.append(err)
            
            age_val, err = validate_input(age, "Age")
            if err:
                errors.append(err)
            
            if errors:
                for error in errors:
                    st.error(error)
            else:
                try:
                    # Calculate feature categories
                    bmi_features = calculate_bmi_category(bmi_val)
                    glucose_features = calculate_glucose_category(glucose_val)
                    insulin_feature = calculate_insulin_category(insulin_val)
                    
                    # Prepare input
                    user_input = [
                        pregnancies_val, glucose_val, bp_val, skin_val,
                        insulin_val, bmi_val, dpf_val, age_val,
                        bmi_features['underweight'],
                        bmi_features['overweight'],
                        bmi_features['obese_class1'],
                        bmi_features['obese_class2'],
                        bmi_features['obese_class3'],
                        insulin_feature,
                        glucose_features['low'],
                        glucose_features['normal'],
                        glucose_features['prediabetic'],
                        glucose_features['diabetic']
                    ]
                    
                    # Make prediction
                    prediction = models['diabetes'].predict([user_input])
                    probability = models['diabetes'].predict_proba([user_input])
                    
                    # Display results
                    st.markdown("---")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if prediction[0] == 1:
                            st.markdown(
                                "<div class='result-danger'><h3>⚠️ High Risk of Diabetes</h3>"
                                "<p>The prediction indicates a high risk of diabetes.</p></div>",
                                unsafe_allow_html=True
                            )
                            risk_score = probability[0][1] * 100
                        else:
                            st.markdown(
                                "<div class='result-success'><h3>✅ Low Risk of Diabetes</h3>"
                                "<p>The prediction indicates a low risk of diabetes.</p></div>",
                                unsafe_allow_html=True
                            )
                            risk_score = probability[0][0] * 100
                    
                    with col2:
                        st.metric("Risk Score", f"{risk_score:.1f}%")
                    
                    st.markdown(
                        "💡 **Recommendation**: Consult with a healthcare professional for proper diagnosis and guidance."
                    )
                
                except Exception as e:
                    st.error(f"❌ Error during prediction: {str(e)}")

# Heart Disease Prediction
elif selected == 'Heart Disease Prediction':
    st.title("❤️ Heart Disease Prediction")
    
    if 'heart' not in models:
        st.error("❌ Heart disease model is not available. Please ensure the model file exists.")
    else:
        st.markdown(
            "Enter your cardiac health metrics to predict heart disease risk. All fields are required."
        )
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.text_input("Age (years)", value="", key="heart_age")
        with col2:
            sex = st.text_input("Sex (0=Female, 1=Male)", value="")
        with col3:
            cp = st.text_input("Chest Pain Type (0-3)", value="")
        
        with col1:
            trestbps = st.text_input("Resting Blood Pressure (mmHg)", value="")
        with col2:
            chol = st.text_input("Serum Cholesterol (mg/dl)", value="")
        with col3:
            fbs = st.text_input("Fasting Blood Sugar > 120 (0/1)", value="0")
        
        with col1:
            restecg = st.text_input("Resting ECG (0-2)", value="")
        with col2:
            thalach = st.text_input("Maximum Heart Rate Achieved", value="")
        with col3:
            exang = st.text_input("Exercise Induced Angina (0/1)", value="0")
        
        with col1:
            oldpeak = st.text_input("ST Depression by Exercise", value="")
        with col2:
            slope = st.text_input("ST Segment Slope (0-2)", value="")
        with col3:
            ca = st.text_input("Major Vessels by Fluoroscopy (0-4)", value="")
        
        with col1:
            thal = st.text_input("Thalassemia (0=Normal, 1=Fixed, 2=Reversible)", value="")
        
        if st.button("🔍 Get Prediction", key="heart_btn"):
            # Validate all inputs
            errors = []
            
            age_val, err = validate_input(age, "Age")
            if err:
                errors.append(err)
            
            sex_val, err = validate_input(sex, "Sex")
            if err:
                errors.append(err)
            
            cp_val, err = validate_input(cp, "Chest Pain Type")
            if err:
                errors.append(err)
            
            trestbps_val, err = validate_input(trestbps, "Resting Blood Pressure")
            if err:
                errors.append(err)
            
            chol_val, err = validate_input(chol, "Cholesterol")
            if err:
                errors.append(err)
            
            fbs_val, err = validate_input(fbs, "Fasting Blood Sugar")
            if err:
                errors.append(err)
            
            restecg_val, err = validate_input(restecg, "Resting ECG")
            if err:
                errors.append(err)
            
            thalach_val, err = validate_input(thalach, "Maximum Heart Rate")
            if err:
                errors.append(err)
            
            exang_val, err = validate_input(exang, "Exercise Induced Angina")
            if err:
                errors.append(err)
            
            oldpeak_val, err = validate_input(oldpeak, "ST Depression")
            if err:
                errors.append(err)
            
            slope_val, err = validate_input(slope, "ST Slope")
            if err:
                errors.append(err)
            
            ca_val, err = validate_input(ca, "Major Vessels")
            if err:
                errors.append(err)
            
            thal_val, err = validate_input(thal, "Thalassemia")
            if err:
                errors.append(err)
            
            if errors:
                for error in errors:
                    st.error(error)
            else:
                try:
                    # Prepare input
                    user_input = [
                        age_val, sex_val, cp_val, trestbps_val, chol_val, fbs_val,
                        restecg_val, thalach_val, exang_val, oldpeak_val, slope_val, ca_val, thal_val
                    ]
                    
                    # Make prediction
                    prediction = models['heart'].predict([user_input])
                    probability = models['heart'].predict_proba([user_input])
                    
                    # Display results
                    st.markdown("---")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if prediction[0] == 1:
                            st.markdown(
                                "<div class='result-danger'><h3>⚠️ High Risk of Heart Disease</h3>"
                                "<p>The prediction indicates a high risk of heart disease.</p></div>",
                                unsafe_allow_html=True
                            )
                            risk_score = probability[0][1] * 100
                        else:
                            st.markdown(
                                "<div class='result-success'><h3>✅ Low Risk of Heart Disease</h3>"
                                "<p>The prediction indicates a low risk of heart disease.</p></div>",
                                unsafe_allow_html=True
                            )
                            risk_score = probability[0][0] * 100
                    
                    with col2:
                        st.metric("Risk Score", f"{risk_score:.1f}%")
                    
                    st.markdown(
                        "💡 **Recommendation**: Consult with a cardiologist for proper evaluation and guidance."
                    )
                
                except Exception as e:
                    st.error(f"❌ Error during prediction: {str(e)}")

# Kidney Disease Prediction
elif selected == 'Kidney Disease Prediction':
    st.title("🫘 Kidney Disease Prediction")
    
    if 'kidney' not in models:
        st.error("❌ Kidney disease model is not available. Please ensure the model file exists.")
    else:
        st.markdown(
            "Enter your renal health metrics to predict kidney disease risk. All fields are required."
        )
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            age = st.text_input('Age (years)', value="", key="kidney_age")
        with col2:
            blood_pressure = st.text_input('Blood Pressure (mmHg)', value="")
        with col3:
            specific_gravity = st.text_input('Specific Gravity', value="")
        with col4:
            albumin = st.text_input('Albumin (0-5)', value="")
        with col5:
            sugar = st.text_input('Sugar (0-5)', value="")
        
        with col1:
            red_blood_cells = st.text_input('Red Blood Cells (0/1)', value="0")
        with col2:
            pus_cell = st.text_input('Pus Cell (0/1)', value="0")
        with col3:
            pus_cell_clumps = st.text_input('Pus Cell Clumps (0/1)', value="0")
        with col4:
            bacteria = st.text_input('Bacteria (0/1)', value="0")
        with col5:
            blood_glucose_random = st.text_input('Blood Glucose Random (mg/dL)', value="")
        
        with col1:
            blood_urea = st.text_input('Blood Urea (mg/dL)', value="")
        with col2:
            serum_creatinine = st.text_input('Serum Creatinine (mg/dL)', value="")
        with col3:
            sodium = st.text_input('Sodium (mEq/L)', value="")
        with col4:
            potassium = st.text_input('Potassium (mEq/L)', value="")
        with col5:
            hemoglobin = st.text_input('Hemoglobin (g/dL)', value="")
        
        with col1:
            packed_cell_volume = st.text_input('Packed Cell Volume (%)', value="")
        with col2:
            white_blood_cell_count = st.text_input('WBC Count (cells/µL)', value="")
        with col3:
            red_blood_cell_count = st.text_input('RBC Count (millions/µL)', value="")
        with col4:
            hypertension = st.text_input('Hypertension (0/1)', value="0")
        with col5:
            diabetes_mellitus = st.text_input('Diabetes Mellitus (0/1)', value="0")
        
        with col1:
            coronary_artery_disease = st.text_input('Coronary Artery Disease (0/1)', value="0")
        with col2:
            appetite = st.text_input('Appetite (0/1)', value="0")
        with col3:
            pedal_edema = st.text_input('Pedal Edema (0/1)', value="0")
        with col4:
            anemia = st.text_input('Anemia (0/1)', value="0")
        
        if st.button("🔍 Get Prediction", key="kidney_btn"):
            # Validate all inputs
            errors = []
            
            age_val, err = validate_input(age, "Age")
            if err:
                errors.append(err)
            
            bp_val, err = validate_input(blood_pressure, "Blood Pressure")
            if err:
                errors.append(err)
            
            sg_val, err = validate_input(specific_gravity, "Specific Gravity")
            if err:
                errors.append(err)
            
            albumin_val, err = validate_input(albumin, "Albumin")
            if err:
                errors.append(err)
            
            sugar_val, err = validate_input(sugar, "Sugar")
            if err:
                errors.append(err)
            
            rbc_val, err = validate_input(red_blood_cells, "Red Blood Cells")
            if err:
                errors.append(err)
            
            pc_val, err = validate_input(pus_cell, "Pus Cell")
            if err:
                errors.append(err)
            
            pcc_val, err = validate_input(pus_cell_clumps, "Pus Cell Clumps")
            if err:
                errors.append(err)
            
            bacteria_val, err = validate_input(bacteria, "Bacteria")
            if err:
                errors.append(err)
            
            bgr_val, err = validate_input(blood_glucose_random, "Blood Glucose")
            if err:
                errors.append(err)
            
            bu_val, err = validate_input(blood_urea, "Blood Urea")
            if err:
                errors.append(err)
            
            sc_val, err = validate_input(serum_creatinine, "Serum Creatinine")
            if err:
                errors.append(err)
            
            sodium_val, err = validate_input(sodium, "Sodium")
            if err:
                errors.append(err)
            
            potassium_val, err = validate_input(potassium, "Potassium")
            if err:
                errors.append(err)
            
            hemo_val, err = validate_input(hemoglobin, "Hemoglobin")
            if err:
                errors.append(err)
            
            pcv_val, err = validate_input(packed_cell_volume, "Packed Cell Volume")
            if err:
                errors.append(err)
            
            wbc_val, err = validate_input(white_blood_cell_count, "WBC Count")
            if err:
                errors.append(err)
            
            rcc_val, err = validate_input(red_blood_cell_count, "RBC Count")
            if err:
                errors.append(err)
            
            hyper_val, err = validate_input(hypertension, "Hypertension")
            if err:
                errors.append(err)
            
            dm_val, err = validate_input(diabetes_mellitus, "Diabetes Mellitus")
            if err:
                errors.append(err)
            
            cad_val, err = validate_input(coronary_artery_disease, "Coronary Artery Disease")
            if err:
                errors.append(err)
            
            app_val, err = validate_input(appetite, "Appetite")
            if err:
                errors.append(err)
            
            ped_val, err = validate_input(pedal_edema, "Pedal Edema")
            if err:
                errors.append(err)
            
            anem_val, err = validate_input(anemia, "Anemia")
            if err:
                errors.append(err)
            
            if errors:
                for error in errors:
                    st.error(error)
            else:
                try:
                    # Prepare input
                    user_input = [
                        age_val, bp_val, sg_val, albumin_val, sugar_val,
                        rbc_val, pc_val, pcc_val, bacteria_val,
                        bgr_val, bu_val, sc_val, sodium_val,
                        potassium_val, hemo_val, pcv_val,
                        wbc_val, rcc_val, hyper_val,
                        dm_val, cad_val, app_val,
                        ped_val, anem_val
                    ]
                    
                    # Make prediction
                    prediction = models['kidney'].predict([user_input])
                    probability = models['kidney'].predict_proba([user_input])
                    
                    # Display results
                    st.markdown("---")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if prediction[0] == 1:
                            st.markdown(
                                "<div class='result-danger'><h3>⚠️ High Risk of Kidney Disease</h3>"
                                "<p>The prediction indicates a high risk of kidney disease.</p></div>",
                                unsafe_allow_html=True
                            )
                            risk_score = probability[0][1] * 100
                        else:
                            st.markdown(
                                "<div class='result-success'><h3>✅ Low Risk of Kidney Disease</h3>"
                                "<p>The prediction indicates a low risk of kidney disease.</p></div>",
                                unsafe_allow_html=True
                            )
                            risk_score = probability[0][0] * 100
                    
                    with col2:
                        st.metric("Risk Score", f"{risk_score:.1f}%")
                    
                    st.markdown(
                        "💡 **Recommendation**: Consult with a nephrologist for comprehensive kidney function evaluation."
                    )
                
                except Exception as e:
                    st.error(f"❌ Error during prediction: {str(e)}")
