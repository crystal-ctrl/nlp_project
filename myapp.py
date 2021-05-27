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
data = pd.read_csv("./app_ready.csv", sep=r'\s*,\s*',
                           header=0, encoding='ascii', engine='python')

#Convert option string to topic_num
def option2num(option):
    option_map = {"Education and Training":0.0, "Enviromental Impact":1.0, "Inhibition on COVID-19":2.0,
    "Complications of COVID-19":3.0, "Diagnositc Imaging and Surveillance":4.0, "Mental Health":5.0,
    "Information sharing and Inter-sectoral Collaboration":6.0, "ACE2 Receptor":7.0,
    "Ethical and Social Considerations":8.0, "Material Science":9.0, "Diagnositc Testings":10.0,
    "Virus Genetics, Origin, Evolution":11.0, "Pharmaceutical Interventions":12.0, "High Risk Factors":13.0,
    "Treatments and Therapeutics":14.0, "Personal Protective Equipment":15.0, "Transmission and Mortality Rate":16.0,
    "Technology Application":17.0, "Cancer":18.0, "Social Behavior Research":19.0, "Policy and Procedure":20.0,
    "Alternative Treatments and Therapies":21.0, "Medical Care":22.0, "Non-Pharmaceutical Interventions":23.0,
    "Social Network":24.0, "Long-Term Effects of COVID-19":25.0, "Data Science Tools and Algorithms":26.0,
    "Critical Care":27.0}
    return option_map[option]

# function to get top 20 articles
def topic_relative_paper(topic_num):
    df = data[ data['Topic_Num'] == topic_num ].reset_index(drop=True)
        for i in range(20):
            link = f'{df.Title[i]} \n({df.url[i]})'
            st.write(link, unsafe_allow_html=True)

# output
# st.write(option2num(option))
topic_relative_paper(option2num(option))
