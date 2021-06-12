#### <img src="https://github.com/crystal-ctrl/nlp_project/blob/main/Covipedia.png" width="150"/>   
# COVIPEDIA

### A Recommendation System for Navigating COVID-19 Research Articles

NLP Unsupervised ML project

## Goal

The goal of this project is build a recommendation system for scientists and researchers to navigate the current surge of papers about COVID-19, find what is relevant to their work, and uncover the hidden semantic relationships. Using the [COVID-19 Open Research Dataset](https://www.semanticscholar.org/cord19), I used the abstract of the subset of articles from January 2020 to May 2021 (about 260,000 articles) as text in this project. With the LDA model, I assigned each documents with dominant topic and their relevance to the topic and grouped articles by topics for recommendation system. So researchers can look up articles based on topic that is related to their work. Lastly, I deployed a Strealit app on Heroku with a smaller dataset that recommends top 20 related articles for the selected topic. 

To learn more, see my [blog post](https://medium.com/nerd-for-tech/unsupervised-topic-modeling-using-natural-language-processing-nlp-19a4d7124392) and [presentation slides](https://github.com/crystal-ctrl/nlp_project/blob/main/presentation.pdf)

The topic model visualization with pyLDAvis is saved as a html file, you can download it from [here](https://github.com/crystal-ctrl/nlp_project/blob/main/Images/lda.html) to see.

Try out the Heroku app for [COVIPEDIA](https://covipedia.herokuapp.com/)~

## Workflow

- Code (in [Workflow Folder](https://github.com/crystal-ctrl/nlp_project/tree/main/Workflow))
  - Streamlit app on Heroku
    - [main python file](https://github.com/crystal-ctrl/nlp_project/blob/main/myapp.py)
    - [Procfile](https://github.com/crystal-ctrl/nlp_project/blob/main/Procfile), [setup doc](https://github.com/crystal-ctrl/nlp_project/blob/main/setup.sh), [required library](https://github.com/crystal-ctrl/nlp_project/blob/main/requirements.txt) for Heroku
    - [Dataset](https://github.com/crystal-ctrl/nlp_project/blob/main/app_ready.csv) used in app

## Technologies

- Python (pandas, numpy)
- langdetect
- regex, string
- spaCy, scispaCy ("en_core_sci_lg" model for biomedical, scientific, and clinical vocabulary)
- NLTK
- Scikitlearn 
- Gensim
- WordCloud
- pyLDAvis
- Streamlit
- Heroku





