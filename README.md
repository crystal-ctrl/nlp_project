# <img src="https://github.com/crystal-ctrl/nlp_project/blob/main/Covipedia.png" width="200"/>   COVIPEDIA

### A Recommendation System for Navigating COVID-19 Research Articles

NLP Unsupervised ML project

## Abstract

The goal of this project is build a recommendation system for scientists and researchers to navigate the current surge of papers about COVID-19, find what is relevant to their work, and uncover the hidden semantic relationships. 

Lastly, I deployed a Strealit [app](https://covipedia.herokuapp.com/) on Heroku with a smaller dataset that recommends top 20 related articles for the selected topic. 



## Backstory

Because of the rapid increase in scientific literature around COVID19, it is hard to keep up with the newest publications. Scientists and researchers are overwhelmed by the volume and struggle to find articles that are relevant for their work. In addition, the limitations of scientific conferences makes it even harder to collaborate and stay up to date. However, it is crucial for scientists to be aware of ongoing research to find relevant publications. 

So, the goal of this project is **to build an unsupervised NLP model (Topic modeling and/or recommendation system) that helps researchers to navigate the current surge of papers about COVID-19, find what is relevant to their work, and uncover the hidden semantic relationships.** 

Impact hypothesis: With the machine learning model, scientists would be able to prevent duplication of research effort and to identify gaps in the current literature to set as their new goals.



## Data

The data used in this project would be the [COVID-19 Open Research Dataset](https://www.semanticscholar.org/cord19), which is a collection of over 500,000 scholarly articles about the novel coronavirus for use by the global research community.



## Methodology 





## Workflow

- Code (in [Workflow Folder](https://github.com/crystal-ctrl/nlp_project/tree/main/Workflow))
  - Streamlit app on Heroku
    - [main python file](https://github.com/crystal-ctrl/nlp_project/blob/main/myapp.py)
    - [Procfile](https://github.com/crystal-ctrl/nlp_project/blob/main/Procfile), [setup doc](https://github.com/crystal-ctrl/nlp_project/blob/main/setup.sh), [required library](https://github.com/crystal-ctrl/nlp_project/blob/main/requirements.txt) for Heroku
    - [Dataset](https://github.com/crystal-ctrl/nlp_project/blob/main/app_ready.csv) used in app
    - 



## Technologies

- Python (pandas, numpy)
- langdetect
- spaCy, scispaCy ("en_core_sci_lg" model for biomedical, scientific, and clinical vocabulary)
- NLTK
- Scikitlearn 
- Gensim
- WordCloud
- pyLDAvis
- Streamlit
- Heroku

## Approaches Used

Data Pre-processing

- Filter out non-english articles





Topic Model

- LDA (Gensim)

Topic Visualization

- WordCloud
- pyLDAvis



## Communication

The topic model visualization with pyLDAvis is saved as a html file, you can download it from [here](https://github.com/crystal-ctrl/nlp_project/blob/main/Images/lda.html) to see.

Try the Heroku app for [COVIPEDIA](https://covipedia.herokuapp.com/).

To learn more, see my blog post and presentation slides.



