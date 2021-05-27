import streamlit as st
import pandas as pd
from PIL import Image

################
##   Title    ##
################

image = Image.open('Covipedia.png')
col1, col2 = st.beta_columns([3,8])
with col1:
    st.image(image, width=150)
with col2:
    st.title("COVIPEDIA")
    st.markdown("Navigate COVID-19 scientific literature with **Topics**!")

st.markdown("""---""")
################
##   Input    ##
################

st.subheader('COVID-19 Publications Related to: ')

option = st.selectbox(
    "Choose the topic to explore:",
    ("Education and Training", "Enviromental Impact", "Inhibition on COVID-19",
    "Complications of COVID-19", "Diagnositc Imaging and Surveillance", "Mental Health",
    "Information sharing and Inter-sectoral Collaboration", "ACE2 Receptor",
    "Ethical and Social Considerations", "Material Science", "Diagnositc Testings",
    "Virus Genetics, Origin, Evolution", "Pharmaceutical Interventions", "High Risk Factors",
    "Treatments and Therapeutics", "Personal Protective Equipment", "Transmission and Mortality Rate",
    "Technology Application", "Cancer", "Social Behavior Research", "Policy and Procedure",
    "Alternative Treatments and Therapies", "Medical Care", "Non-Pharmaceutical Interventions",
    "Social Network", "Long-Term Effects of COVID-19", "Data Science Tools and Algorithms",
    "Critical Care")
)
st.markdown("""---""")

################
##   Output   ##
################
st.write("**Here are the Top 20 articles related to: **", option, "(sorted by relevance)")


# import dataset
data = pd.read_csv("./app_ready.csv")

#Convert option string to topic_num
def option2num(option):
    option_map = {"Education and Training":0, "Enviromental Impact":1, "Inhibition on COVID-19":2,
    "Complications of COVID-19":3, "Diagnositc Imaging and Surveillance":4, "Mental Health":5,
    "Information sharing and Inter-sectoral Collaboration":6, "ACE2 Receptor":7,
    "Ethical and Social Considerations":8, "Material Science":9, "Diagnositc Testings":10,
    "Virus Genetics, Origin, Evolution":11, "Pharmaceutical Interventions":12, "High Risk Factors":13,
    "Treatments and Therapeutics":14, "Personal Protective Equipment":15, "Transmission and Mortality Rate":16,
    "Technology Application":17, "Cancer":18, "Social Behavior Research":19, "Policy and Procedure":20,
    "Alternative Treatments and Therapies":21, "Medical Care":22, "Non-Pharmaceutical Interventions":23,
    "Social Network":24, "Long-Term Effects of COVID-19":25, "Data Science Tools and Algorithms":26,
    "Critical Care":27}
    return option_map[option]

# function to get top 20 articles
def topic_relative_paper(topic_num):
    df = data[data['Topic_Num'] == topic_num].reset_index(drop=True)
    for i in range(len(df)):
        link = f'{df.Title[i]} \n({df.url[i]})'
        st.write(link, unsafe_allow_html=True)

# output
topic_relative_paper(option2num(option))
