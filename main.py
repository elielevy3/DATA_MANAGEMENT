import streamlit as st
import pandas as pd
from random import sample
from datetime import date
from annotated_text import annotated_text
from streamlit_extras.colored_header import colored_header


st.set_page_config(page_title="WEWYSE DATA MANAGEMENT TESTING", page_icon="📚")

@st.experimental_memo
def get_sample_question(data, nb_of_questions, time_param):
    return sample(range(1, len(data)), nb_of_questions)

st.markdown("# 📚 WELCOME TO WEWYSE DATA MANAGEMENT TESTING !")

st.write(' ')
with st.expander("📚 Information about the Web App", expanded = True):
    st.write("""
            - You're being evaluated as a part of WeWyse data management recruitment process
            - In case of a question, please contact Anne-Eole Meret-Conti or Benjamin Simonneau
            """)

st.write("#")

###########################################
######### QUESTIONS PRINCIPALES ###########
###########################################

# get raw data
q_prin = pd.read_csv("questions_principales.csv", sep=";")

colored_header(label="Questions principales : ", color_name="green-70",description=" ")

st.write("#")

submitted_answers = {}

for i in range(len(q_prin)):
    
    st.write("Question ", i+1, " / ", len(q_prin))
    intitule = q_prin["Question"][i]
    st.write(intitule)
    submitted_answers[intitule] = st.text_area(" ", max_chars=400, key=i+1000)
    st.write("#")

st.write("#")
st.write("#")

###########################################
######### QUESTIONS SUBSIDIAIRES ##########
###########################################



colored_header(label="Questions subsidiaires : ", color_name="orange-70",description=" ")

q_sub = pd.read_csv("questions_subsidiaires.csv", sep=";")

# colors
colors = ["#bad5ff", "#fc778f", "#90fcea", "#95fc90", "#f7f7a8", "#f7ada8", "#f7a8e6"]
categorie_colors = dict(zip(set(q_sub["categorie"]) , colors))

nb_questions_sub = 4

# get n questions
questions = get_sample_question(q_sub, nb_questions_sub, date.today())

for i, question in enumerate(questions):

    # question number
    st.write("Question ", i + 1, " / ", nb_questions_sub)
    # writing the question
    intitule = q_sub["Question"][question]
    st.write(intitule)
    annotated_text(" ",("Categorie", q_sub["categorie"][question], categorie_colors[q_sub["categorie"][question]]))
    submitted_answers[intitule] = st.text_area(" ", max_chars=400, key=i+nb_questions_sub)
    st.write("-----------------------------------")


if st.sidebar.button(label="Soumettre les réponses"):
    st.header("A ENVOYER PAR MAIL")
    df = pd.DataFrame(list(zip(submitted_answers.keys(), submitted_answers.values())), columns=["Question", "Réponses"])
    st.dataframe(df)

