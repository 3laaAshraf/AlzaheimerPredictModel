import streamlit as st
import pickle
import numpy as np

# Load the saved model and preprocessing parameters
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor_loaded = data["model"]

IS = {
        "Yes": 1,
        "No": 0,
    }
genderType = {
        "Male": 1,
        "Female": 0,
    }
EduLevel = {
        "None": 0,
        "High School": 1,
        "Bachelor\'s": 2,
        "Higher": 3,
    }
EthnicityType = {
    "Caucasian":0,
    "African American":1,
    "Asian":2,
    "Other":3
}

# Define the Streamlit page
def show_predict_page():
    # st.title("Alzheimer's Disease Prediction")
    st.markdown("""
    <h1 style="color: YellowGreen; text-align: center;">
        Alzheimer's Disease Prediction
    </h1>
    """, unsafe_allow_html=True)
    st.write("""### We need some information to predict the likelihood of Alzheimer's disease""")
    
    # Input fields for user data
    st.markdown("""
        <style>
            /* Style the input box */
            div[data-testid="stNumberInput"] input {
                background-color: LemonChiffon;  /* Input box background color */
                color: black;  /* Text color */
                font-weight: bold;
                caret-color: black;
            }

            /* Style the increment and decrement buttons */
            div[data-testid="stNumberInput"] button {
                background-color: MediumSeaGreen;  /* Button background color */
                color: white;  /* Button text color */
                border: none;  /* Remove default border */
                padding: 5px;  /* Button padding */
                font-size: 16px;  /* Adjust font size */
                font-weight: bold;  /* Pointer cursor on hover */
                caret-color: black;
            }

            /* Hover effect for buttons */
            div[data-testid="stNumberInput"] button:hover {
                background-color: blue;  /* Darker green on hover */
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            div[data-baseweb="select"] > div {
            background-color: LemonChiffon;
            color:black;
            font-weight: bold;  /* Make text bold */
            border: 0px solid green;  /* Border color */
            border-radius: 10px; 
            caret-color: black;
            }
            
        }
        </style>
    """, unsafe_allow_html=True)

# Number input widget
    age = st.number_input("What is your Age?", value=50)

    #age = st.number_input("What is your Age?", value=50)
    GenderType = st.selectbox("What is your Gender?", genderType.keys())
    ethnicity_Type = st.selectbox("What is your Ethnicity?", EthnicityType.keys())
    Edu = st.selectbox("Education Level:", EduLevel.keys())
    bmi = st.number_input("What is your BMI?", step=0.1,format="%.2f")
    isSmoke = st.selectbox("Do you smoke?", IS.keys())
    alcohol_consumption = st.number_input("What is your Alcohol Consumption (units/week)?",step=0.1,format="%.2f" )
    physical_activity = st.number_input("What is your Physical Activity (hours/week)?", step=0.1,format="%.2f")
    diet_quality = st.number_input("Rate your Diet Quality (1-5 scale)", step=0.1,format="%.2f")
    sleep_quality = st.number_input("Rate your Sleep Quality (1-5 scale)", step=0.1,format="%.2f")
    FamilyHistoryAlzheimers=st.selectbox("Do you FamilyHistoryAlzheimers?", IS.keys())
    CardiovascularDisease=st.selectbox("Do you CardiovascularDisease?", IS.keys())
    Diabetes=st.selectbox("Do you Diabetes?", IS.keys())
    Depression=st.selectbox("Do you Depression?", IS.keys())
    HeadInjury=st.selectbox("Do you HeadInjury?", IS.keys())
    Hypertension=st.selectbox("Do you Hypertension?", IS.keys())

    systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)",step=1,format="%d")
    diastolic_bp = st.number_input("Diastolic Blood Pressure (mmHg)", step=1,format="%d")

    cholesterol_total = st.number_input("Total Cholesterol (mg/dL)", step=0.1,format="%.2f")
    cholesterol_ldl = st.number_input("LDL Cholesterol (mg/dL)", step=0.1,format="%.2f")
    cholesterol_hdl = st.number_input("HDL Cholesterol (mg/dL)", step=0.1,format="%.2f")
    cholesterol_triglycerides = st.number_input("Triglycerides (mg/dL)", step=0.1,format="%.2f")
    mmse = st.number_input("MMSE Score", step=0.1,format="%.2f")
    functional_assessment = st.number_input("Functional Assessment (1-5 scale)", step=0.1,format="%.2f")
    MemoryComplaints=st.selectbox("Do you MemoryComplaints?", IS.keys())
    BehavioralProblems=st.selectbox("Do you BehavioralProblems?", IS.keys())
    adl = st.number_input("ADL Score", step=0.1,format="%.2f")
    Confusion=st.selectbox("Do you Confusion?", IS.keys())
    Disorientation=st.selectbox("Do you Disorientation?", IS.keys())
    PersonalityChanges=st.selectbox("Do you PersonalityChanges?", IS.keys())
    DifficultyCompletingTasks=st.selectbox("Do you DifficultyCompletingTasks?", IS.keys())
    Forgetfulness=st.selectbox("Do you forget?", IS.keys())
    

    # Button to trigger prediction
    ok = st.button("Get Prediction")

    if ok:
        try:
            # Combine all inputs into a single list
            
                # Map user inputs into a dictionary with model feature names
            input_dict = {
                "Age": age,
                "Gender": genderType[GenderType],
                "Ethnicity": EthnicityType[ethnicity_Type],
                "EducationLevel": EduLevel[Edu],
                "BMI": bmi,
                "Smoking": IS[isSmoke],
                "AlcoholConsumption": alcohol_consumption,
                "PhysicalActivity": physical_activity,
                "DietQuality": diet_quality,
                "SleepQuality": sleep_quality,
                "FamilyHistoryAlzheimers": IS[FamilyHistoryAlzheimers],
                "CardiovascularDisease": IS[CardiovascularDisease],
                "Diabetes": IS[Diabetes],
                "Depression": IS[Depression],
                "HeadInjury": IS[HeadInjury],
                "Hypertension": IS[Hypertension],
                "SystolicBP": systolic_bp,
                "DiastolicBP": diastolic_bp,
                "CholesterolTotal": cholesterol_total,
                "CholesterolLDL": cholesterol_ldl,
                "CholesterolHDL": cholesterol_hdl,
                "CholesterolTriglycerides": cholesterol_triglycerides,
                "MMSE": mmse,
                "FunctionalAssessment": functional_assessment,
                "MemoryComplaints": IS[MemoryComplaints],
                "BehavioralProblems": IS[BehavioralProblems],
                "ADL": adl,
                "Confusion": IS[Confusion],
                "Disorientation": IS[Disorientation],
                "PersonalityChanges": IS[PersonalityChanges],
                "DifficultyCompletingTasks": IS[DifficultyCompletingTasks],
                "Forgetfulness": IS[Forgetfulness],
            }

            # Ensure inputs match the model's expected feature order
            ordered_inputs = [input_dict[feature] for feature in regressor_loaded.feature_names_]

            # Convert to NumPy array and reshape for prediction
            Z1 = np.array(ordered_inputs).reshape(1, -1)

            # Convert to NumPy array and reshape for prediction
            #Z1 = np.array(inputs).reshape(1, -1)  # Ensure it's a 2D array

            # Predict result
            Result = regressor_loaded.predict(Z1)
            if Result==0:
                st.markdown("""
                <style>
                    .custom-subheader {
                        color: Gold !important;  # Change this to any color you like
                    }
                </style>
                <h3 class="custom-subheader">Great news! , Your results dont show signs of Alzheimer’s</h3>
                 """, unsafe_allow_html=True)
                #st.subheader("Great news! , Your results dont show signs of Alzheimer’s")
                
            else:
                st.markdown("""
                <style>
                    .custom-subheader {
                        color: red !important;  # Change this to any color you like
                    }
                </style>
                <h3 class="custom-subheader">I'am so sorry , Your results show signs of Alzheimer’</h3>
                 """, unsafe_allow_html=True)
                #st.subheader("I'am so sorry , Your results show signs of Alzheimer’s")
            # Display result
            #st.subheader(f"The likelihood of Alzheimer's disease is: {Result[0]:.2f}")

        except ValueError as e:
            st.error(f"An error occurred: {e}")


