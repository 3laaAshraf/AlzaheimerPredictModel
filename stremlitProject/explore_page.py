import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def show_explore_page():
    #df = pd.DataFrame(data)
    df = pd.read_csv('alzheimers_disease_data.csv')
    # Title and Subheading
    st.markdown("""
    <h1 style="color: Moccasin; text-align: center;">
        Explore Alzheimer's Disease Prediction
    </h1>
    """, unsafe_allow_html=True)
    st.markdown("### Diagnosis Results Distribution")

    # Define the Response categories and count occurrences
    categories = [0, 1]
    counts = df.Diagnosis.value_counts().tolist()

    # Choose a color palette from Seaborn for the pie chart
    colors = sns.color_palette("muted")

    # Plot the pie chart with the counts of each response category
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(counts, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)
    ax.set_title('Diagnosis Distribution')

    # Display the pie chart in Streamlit
    st.pyplot(fig)

    # Add observations about the target distribution
    st.markdown("""
    ### Observations
    - The chart visualizes the split between two categories: '0' and '1'.
    - Category `0` accounts for `64.6%` of the total cases.
    - Category `1` makes up `35.4%` of the total cases          
    """)


    st.subheader('Distribution of Smoking by Diagnosis Categories')
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Diagnosis', hue='Smoking')
    plt.title(f'Distribution of Smoking by Diagnosis Categories')
    st.pyplot(fig)
    st.markdown("""
    ### Observations
    - In both diagnosis `0` and `1`, the proportion of `non-smokers` is much higher         
    """)


    st.title('Relationship between Diabetes and Diagnosis')
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Diagnosis', hue='Diabetes')
    plt.title(f'Distribution of Diabetes by Diagnosis Categories')
    st.pyplot(fig)
    st.markdown("""
    ### Observations
    - In both diagnoses `0` and `1`, the proportion of `non-diabetics` is much higher.         
    """)

    st.title('Relationship between Depression and Diagnosis')
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Diagnosis', hue='Depression')
    plt.title(f'Distribution of Depression by Diagnosis Categories')
    st.pyplot(fig)
    st.markdown("""
    ### Observations
    - In both diagnoses `0` and `1`, the proportion of `non-Depression` is much higher..         
    """)
    
    st.title('Relationship between Smoking and Diagnosis')
    smoking_diagnosis_counts = df.groupby(['Diagnosis', 'Smoking']).size().reset_index(name='Count')

    # Plotting Pie Charts for Smoking in each Diagnosis group (Healthy = 0, Alzheimer = 1)
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Pie Chart for Healthy (Diagnosis == 0)
    healthy_smoking = smoking_diagnosis_counts[smoking_diagnosis_counts['Diagnosis'] == 0]
    ax[0].pie(healthy_smoking['Count'], labels=healthy_smoking['Smoking'], autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99'])
    ax[0].set_title('Smoking Distribution in Healthy Group (Diagnosis = 0)')

    # Pie Chart for Alzheimer (Diagnosis == 1)
    alzheimer_smoking = smoking_diagnosis_counts[smoking_diagnosis_counts['Diagnosis'] == 1]
    ax[1].pie(alzheimer_smoking['Count'], labels=alzheimer_smoking['Smoking'], autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99'])
    ax[1].set_title('Smoking Distribution in Alzheimer Group (Diagnosis = 1)')

    # Display the pie charts
    st.pyplot(fig)
    st.markdown("""
    ## Observations       
    """)
    st.markdown("""
    #### For do not have Alzheimer's
    - Percentage of smokers who do not have Alzheimer's disease is `29.0%`..
    - Percentage of non-smokers who do not have Alzheimer's disease is `71.0%`..         
    """)
    st.markdown("""
    #### For have Alzheimer's
    - Percentage of smokers who have Alzheimer's disease is `28.6%`..
    - Percentage of non-smokers who have Alzheimer's disease is `71.4%`..         
    """)


    st.title('Relationship between Gender and Diagnosis')
    smoking_diagnosis_counts = df.groupby(['Diagnosis', 'Gender']).size().reset_index(name='Count')

    # Plotting Pie Charts for Smoking in each Diagnosis group (Healthy = 0, Alzheimer = 1)
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Pie Chart for Healthy (Diagnosis == 0)
    healthy_smoking = smoking_diagnosis_counts[smoking_diagnosis_counts['Diagnosis'] == 0]
    ax[0].pie(healthy_smoking['Count'], labels=healthy_smoking['Gender'], autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99'])
    ax[0].set_title('Smoking Distribution in Healthy Group (Diagnosis = 0)')

    # Pie Chart for Alzheimer (Diagnosis == 1)
    alzheimer_smoking = smoking_diagnosis_counts[smoking_diagnosis_counts['Diagnosis'] == 1]
    ax[1].pie(alzheimer_smoking['Count'], labels=alzheimer_smoking['Gender'], autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99'])
    ax[1].set_title('Smoking Distribution in Alzheimer Group (Diagnosis = 1)')

    # Display the pie charts
    st.pyplot(fig)
    
    st.markdown("""
    ## Observations       
    """)

    st.markdown("""
    #### For do not have Alzheimer's
    - Percentage of males who do not have Alzheimer's `51.4%`..
    - Percentage of females who do not have Alzheimer's `48.6%`..         
    """)
    st.markdown("""
    #### For have Alzheimer's
    - Percentage of males who have Alzheimer's `49.2%`..
    - Percentage of females who have Alzheimer's `50.8%`..         
    """)
    st.title('Original Dataset : ')
    df.drop(['PatientID', 'DoctorInCharge'], axis=1, inplace=True)
    st.dataframe(df.head(19))

    NewDataframe=df;
    df_display = NewDataframe.replace({1: "Yes", 0: "No"})
    df_display['Gender'] = df_display['Gender'].replace({"Yes": 'male', "No": 'female'})
    df_display['EducationLevel'] = df_display['EducationLevel'].replace({"No": 'None',"Yes": 'High School',2: 'Bachelor\'s',3: 'Higher'})
    df_display['Ethnicity'] = df_display['Ethnicity'].replace({"No": 'Caucasian',"Yes": 'African American',2: 'Asian',3: 'Other'})

    st.title('Detailed Dataset : ')
    st.dataframe(df_display.head(19))