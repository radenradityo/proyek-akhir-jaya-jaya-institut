import streamlit as st
import pandas as pd
import joblib


# Load model
model = joblib.load("model_dropout.pkl")

# Load Data
student_df = pd.read_csv("data/data.csv", sep=";")


# Judul aplikasi
st.title("Jaya Jaya Institut - Student Dropout Prediction")

st.write(
    "Prototype untuk memprediksi status mahasiswa berdasarkan "
    "informasi yang tersedia hingga Semester 1."
)

with st.expander("Student Information"):
    age_at_enrollment = st.number_input(
        "Age at Enrollment",
        min_value=17,
        max_value=100,
        value=20
    )
    admission_grade = st.number_input(
        "Admission Grade",
        min_value=0.0,
        max_value=200.0,
        value=120.0
    )



    previous_qualification_grade = st.number_input(
        "Previous Qualification Grade",
        min_value=0.0,
        max_value=200.0,
        value=120.0
    )

    application_order = st.number_input(
        "Application Order",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )

with st.expander("Student Background"):

    gender_label = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )
    gender = 0 if gender_label == "Female" else 1


    tuition_label = st.selectbox(
        "Tuition Fees Up To Date",
        ["No", "Yes"]
    )
    tuition_fees = 0 if tuition_label == "No" else 1


    marital_status_options = {
        "Single": 1,
        "Married": 2,
        "Widower": 3,
        "Divorced": 4,
        "Facto union": 5,
        "Legally separated": 6
    }

    marital_status_label = st.selectbox(
        "Marital Status",
        list(marital_status_options.keys())
    )

    marital_status = marital_status_options[marital_status_label]


    course_options = {
        "Biofuel Production Technologies": 33,
        "Animation and Multimedia Design": 171,
        "Social Service (evening attendance)": 8014,
        "Agronomy": 9003,
        "Communication Design": 9070,
        "Veterinary Nursing": 9085,
        "Informatics Engineering": 9119,
        "Equinculture": 9130,
        "Management": 9147,
        "Social Service": 9238,
        "Tourism": 9254,
        "Nursing": 9500,
        "Oral Hygiene": 9556,
        "Advertising and Marketing Management": 9670,
        "Journalism and Communication": 9773,
        "Basic Education": 9853,
        "Management (evening attendance)": 9991
    }

    course_label = st.selectbox(
        "Course",
        list(course_options.keys())
    )

    course = course_options[course_label]

with st.expander("Student Conditions"):

    attendance_label = st.selectbox(
        "Attendance",
        ["Daytime", "Evening"]
    )
    daytime_evening_attendance = 1 if attendance_label == "Daytime" else 0


    displaced_label = st.selectbox(
        "Displaced",
        ["No", "Yes"]
    )
    displaced = 1 if displaced_label == "Yes" else 0


    special_needs_label = st.selectbox(
        "Educational Special Needs",
        ["No", "Yes"]
    )
    educational_special_needs = 1 if special_needs_label == "Yes" else 0


    debtor_label = st.selectbox(
        "Debtor",
        ["No", "Yes"]
    )
    debtor = 1 if debtor_label == "Yes" else 0


    scholarship_label = st.selectbox(
        "Scholarship Holder",
        ["No", "Yes"]
    )
    scholarship_holder = 1 if scholarship_label == "Yes" else 0


    international_label = st.selectbox(
        "International Student",
        ["No", "Yes"]
    )
    international = 1 if international_label == "Yes" else 0

with st.expander("Semester 1 Academic Performance"):

    curricular_1st_credited = st.number_input(
        "Semester 1 - Credited Units",
        min_value=0,
        max_value=30,
        value=0,
        step=1
    )

    curricular_1st_enrolled = st.number_input(
        "Semester 1 - Enrolled Units",
        min_value=0,
        max_value=30,
        value=6,
        step=1
    )

    curricular_1st_evaluations = st.number_input(
        "Semester 1 - Evaluated Units",
        min_value=0,
        max_value=30,
        value=6,
        step=1
    )

    curricular_1st_approved = st.number_input(
        "Semester 1 - Approved Units",
        min_value=0,
        max_value=30,
        value=6,
        step=1
    )

    curricular_1st_grade = st.number_input(
        "Semester 1 - Average Grade",
        min_value=0.0,
        max_value=20.0,
        value=12.0,
        step=0.1
    )

    curricular_1st_without_evaluations = st.number_input(
        "Semester 1 - Units Without Evaluation",
        min_value=0,
        max_value=30,
        value=0,
        step=1
    )

with st.expander("Educational and Family Background"):

    application_mode_options = {
        "1st phase - general contingent": 1,
        "Ordinance No. 612/93": 2,
        "1st phase - special contingent (Azores Island)": 5,
        "Holders of other higher courses": 7,
        "Ordinance No. 854-B/99": 10,
        "International student (bachelor)": 15,
        "1st phase - special contingent (Madeira Island)": 16,
        "2nd phase - general contingent": 17,
        "3rd phase - general contingent": 18,
        "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
        "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
        "Over 23 years old": 39,
        "Transfer": 42,
        "Change of course": 43,
        "Technological specialization diploma holders": 44,
        "Change of institution/course": 51,
        "Short cycle diploma holders": 53,
        "Change of institution/course (International)": 57
    }

    application_mode_label = st.selectbox(
        "Application Mode",
        list(application_mode_options.keys())
    )

    application_mode = application_mode_options[application_mode_label]

    previous_qualification_options = {
        "Secondary education": 1,
        "Higher education - bachelor's degree": 2,
        "Higher education - degree": 3,
        "Higher education - master's": 4,
        "Higher education - doctorate": 5,
        "Frequency of higher education": 6,
        "12th year of schooling - not completed": 9,
        "11th year of schooling - not completed": 10,
        "Other - 11th year of schooling": 12,
        "10th year of schooling": 14,
        "10th year of schooling - not completed": 15,
        "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
        "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Professional higher technical course": 42,
        "Higher education - master (2nd cycle)": 43
    }

    previous_qualification_label = st.selectbox(
        "Previous Qualification",
        list(previous_qualification_options.keys())
    )

    previous_qualification = previous_qualification_options[
        previous_qualification_label
    ]

    nationality_options = {
        "Portuguese": 1,
        "German": 2,
        "Spanish": 6,
        "Italian": 11,
        "Dutch": 13,
        "English": 14,
        "Lithuanian": 17,
        "Angolan": 21,
        "Cape Verdean": 22,
        "Guinean": 24,
        "Mozambican": 25,
        "Santomean": 26,
        "Turkish": 32,
        "Brazilian": 41,
        "Romanian": 62,
        "Moldova (Republic of)": 100,
        "Mexican": 101,
        "Ukrainian": 103,
        "Russian": 105,
        "Cuban": 108,
        "Colombian": 109
    }

    nationality_label = st.selectbox(
        "Nationality",
        list(nationality_options.keys())
    )

    nationality = nationality_options[nationality_label]

    mothers_qualification = st.selectbox(
        "Mother's Qualification",
        sorted(student_df["Mothers_qualification"].unique())
    )

    fathers_qualification = st.selectbox(
        "Father's Qualification",
        sorted(student_df["Fathers_qualification"].unique())
    )

    mothers_occupation = st.selectbox(
        "Mother's Occupation",
        sorted(student_df["Mothers_occupation"].unique())
    )

    fathers_occupation = st.selectbox(
        "Father's Occupation",
        sorted(student_df["Fathers_occupation"].unique())
    )

with st.expander("Economic Indicators"):

    unemployment_rate = st.number_input(
        "Unemployment Rate",
        min_value=float(student_df["Unemployment_rate"].min()),
        max_value=float(student_df["Unemployment_rate"].max()),
        value=float(student_df["Unemployment_rate"].median()),
        step=0.1
    )

    inflation_rate = st.number_input(
        "Inflation Rate",
        min_value=float(student_df["Inflation_rate"].min()),
        max_value=float(student_df["Inflation_rate"].max()),
        value=float(student_df["Inflation_rate"].median()),
        step=0.1
    )

    gdp = st.number_input(
        "GDP",
        min_value=float(student_df["GDP"].min()),
        max_value=float(student_df["GDP"].max()),
        value=float(student_df["GDP"].median()),
        step=0.1
    )

st.subheader("Prediction")

input_data = pd.DataFrame([{
    "Marital_status": marital_status,
    "Application_mode": application_mode,
    "Application_order": application_order,
    "Course": course,
    "Daytime_evening_attendance": daytime_evening_attendance,
    "Previous_qualification": previous_qualification,
    "Previous_qualification_grade": previous_qualification_grade,
    "Nacionality": nationality,
    "Mothers_qualification": mothers_qualification,
    "Fathers_qualification": fathers_qualification,
    "Mothers_occupation": mothers_occupation,
    "Fathers_occupation": fathers_occupation,
    "Admission_grade": admission_grade,
    "Displaced": displaced,
    "Educational_special_needs": educational_special_needs,
    "Debtor": debtor,
    "Tuition_fees_up_to_date": tuition_fees,
    "Gender": gender,
    "Scholarship_holder": scholarship_holder,
    "Age_at_enrollment": age_at_enrollment,
    "International": international,
    "Curricular_units_1st_sem_credited": curricular_1st_credited,
    "Curricular_units_1st_sem_enrolled": curricular_1st_enrolled,
    "Curricular_units_1st_sem_evaluations": curricular_1st_evaluations,
    "Curricular_units_1st_sem_approved": curricular_1st_approved,
    "Curricular_units_1st_sem_grade": curricular_1st_grade,
    "Curricular_units_1st_sem_without_evaluations": curricular_1st_without_evaluations,
    "Unemployment_rate": unemployment_rate,
    "Inflation_rate": inflation_rate,
    "GDP": gdp
}])


if st.button("Predict Student Status"):

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    st.success(f"Predicted Status: {prediction}")

    if prediction == "Dropout":
        st.warning(
            "The model identifies this student as having "
            "the highest predicted probability of Dropout. "
            "This result can be used as an early warning for "
            "further academic support."
        )

    elif prediction == "Enrolled":
        st.info(
            "The model identifies this student as having "
            "the highest predicted probability of remaining Enrolled."
        )

    else:
        st.success(
            "The model identifies this student as having "
            "the highest predicted probability of Graduating."
        )

    st.subheader("Prediction Probability")

    dropout_probability = probabilities[0] * 100
    enrolled_probability = probabilities[1] * 100
    graduate_probability = probabilities[2] * 100

    st.write(f"**Dropout:** {dropout_probability:.2f}%")
    st.progress(float(probabilities[0]))

    st.write(f"**Enrolled:** {enrolled_probability:.2f}%")
    st.progress(float(probabilities[1]))

    st.write(f"**Graduate:** {graduate_probability:.2f}%")
    st.progress(float(probabilities[2]))