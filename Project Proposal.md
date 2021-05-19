# Project Proposal - UNCOVID

#### Question/need:

Because of the rapid increase in scientific literature around COVID-19, it is hard to keep up with the newest publications. In addition, the limitations of scientific conferences makes it even harder to collaborate and stay up to date. However, it is crucial for scientists to be aware of ongoing research to find relevant publications. 

So, the goal of this project is **to build an unsupervised NLP model (Topic modeling and/or recommendation system) that helps researchers to navigate the current surge of papers about COVID-19, find what is relevant to their work, and uncover the hidden semantic relationships.** 

Impact hypothesis: With the machine learning model, scientists would be able to prevent duplication of research effort and to identify gaps in the current literature to set as their new goals.

#### Data Description:

The data used in this project would be the [COVID-19 Open Research Dataset](https://www.semanticscholar.org/cord19), which is a collection of over 280,000 scholarly articles about the novel coronavirus for use by the global research community.

Each individual sample/unit is a publication. 

Features includes:

- Cord_uid : unique identifier of each paper
- title: paper's title
- doi: paper DOI (Digital Object identifier)
- abstract: paper's abstract
- Publish_time: published date (yyyy-mm-dd format)
- authors: authors of the paper
- journal: paper journal
- Pdf_json_files: path from the root of the current data dump version to the parses of the paper PDFs into JSON format (debating on using this for body of paper)
- Pmc_json_files: same as above, but corresponding to the full text XML files (debating on using this for body of paper)
- Url: link associated with the paper

#### Tools:

- Start with EDA of the data
- Do some cleaning/preprocessing (there might be paper that's in different languages since it is a global research community) 
  - NLTK, TFIDF, Tokenization, stop words removal, Stemming/Lemmetization, etc.
- Topic Modeling - 
  - Dimensionality reduction - SVD
  - LDA
- Recommendation system or Clustering

If time allows, I'll try using Streamlit to deploy my model

#### MVP Goal:

- a topic model/ recommendation system that provide researchers publications that are relevant to their work/interests.

  