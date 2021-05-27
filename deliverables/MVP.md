# MVP

After pre-processing 250k+ abstract of scientific articles, I built my topic modeling using gensim LDA with 10 topics as base model. However, the topics seem to be general and overlapping. As seen in the wordcoulds, topic 5 and 8 are very similar, as well as topic 6 and 9.

![](https://github.com/crystal-ctrl/nlp_project/blob/main/wordcloud.png)

With the large database and long runtime, it's challenging to interpret topics for each models with different number of topics. So I used topic coherence score to evaluate each models tuning number of topics. It shows that 28 number of topics gives the best coherence score (0.523) comparing to baseline of 10 topics (0.483).

![](https://github.com/crystal-ctrl/nlp_project/blob/main/coherence_score.png)

With the final model, I used pyLDAvis to visualize the topics and terms frequency in each topic for better interpretation.

![](https://github.com/crystal-ctrl/nlp_project/blob/main/pyLDAvis_topic1.png)

The topics are more specific and made more sense. For example, topic 1 appears to be about high risk group, while topic 26 seems to be about cancer. 

For the next step, I'll try to build recommendation system by using topic space/similarity.