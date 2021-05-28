# <img src="https://github.com/crystal-ctrl/nlp_project/blob/main/Covipedia.png" width="150"/>   COVIPEDIA

### A Recommendation System for Navigating COVID-19 Research Articles

NLP Unsupervised ML project

## Abstract

The goal of this project is build a recommendation system for scientists and researchers to navigate the current surge of papers about COVID-19, find what is relevant to their work, and uncover the hidden semantic relationships. Using the [COVID-19 Open Research Dataset](https://www.semanticscholar.org/cord19), I used the abstract of the subset of articles from January 2020 to May 2021 (about 260,000 articles) as text in this project. With the LDA model, I assigned each documents with dominant topic and their relevance to the topic and grouped articles by topics for recommendation system. So researchers can look up articles based on topic that is related to their work. Lastly, I deployed a Strealit [app](https://covipedia.herokuapp.com/) on Heroku with a smaller dataset that recommends top 20 related articles for the selected topic. 

## Backstory

Because of the rapid increase in scientific literature around COVID19, it is hard to keep up with the newest publications. Scientists and researchers are overwhelmed by the volume and struggle to find articles that are relevant for their work. In addition, the limitations of scientific conferences makes it even harder to collaborate and stay up to date. However, it is crucial for scientists to be aware of ongoing research to find relevant publications. 

So, the goal of this project is **to build an unsupervised NLP model (Topic modeling and/or recommendation system) that helps researchers to navigate the current surge of papers about COVID-19, find what is relevant to their work, and uncover the hidden semantic relationships.** 

Impact hypothesis: With the machine learning model, scientists would be able to prevent duplication of research effort and to identify gaps in the current literature to set as their new goals.

## Data

The data used in this project would be the [COVID-19 Open Research Dataset](https://www.semanticscholar.org/cord19), which is a collection of over 500,000 scholarly articles about the novel coronavirus for use by the global research community.

I took the subset of articles from January 2020 to May 2021, which is about 260,000 articles and used the abstract of the articles as text in this project.

## Methodology 

**Text Preprocessing**

1. Filtered out non-English articles with *langdetect*
2. Used *egex* and *string* for simple cleaning
3. Used *ScispaCy*'s (a *spaCy* package) "en_core_sci_lg" model for biomedical, scientific and clinical vocabulary
4. Used *gensim* for phrase detection
5. Removed stopwords with *NLTK*, used Lemmatization, kept noun, adjective, verb, adverb with postag

**Data Transformation**

1. Dictionary - with *gensim.corpora*
2. Corpus

**Topic Modeling**

I built my topic model using *LDA* from *gensim* since I want to discover latent relationships in corpus. 

I first tried 10 number of topics for my base model. But the topics are either too general or overlapping. So I used coherence score to find the optimal number of topics, which is 28 (coherence score: 0.523 vs baseline coherence score: 0.483).

## Findings

**Model Interpretation and Visualization**

For interpretation, I used pyLDAvis to see the topic similarity and relative frequency of the topic in the corpus. Looking at the most frequent keyboards and some example of the articles, the final model has more meaningful topic mixtures. 

**Model Application**

With the LDA model, I assigned each documents with dominant topic and their relevance to the topic and grouped articles by topics for recommendation system. So researchers can look up articles based on topic that is related to their work. 

I used Streamlit to develop the application and deployed the [app](https://covipedia.herokuapp.com/) on Heroku with a smaller dataset (due to size limit on GitHub).

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

## Communication

The topic model visualization with pyLDAvis is saved as a html file, you can download it from [here](https://github.com/crystal-ctrl/nlp_project/blob/main/Images/lda.html) to see.

Try out the Heroku app for [COVIPEDIA](https://covipedia.herokuapp.com/)~

To learn more, see my blog post and [presentation slides](https://github.com/crystal-ctrl/nlp_project/blob/main/presentation.pdf).



