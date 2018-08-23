from sklearn.datasets import fetch_20newsgroups

dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
documents = dataset.data

#-----------------------#

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

no_features = 1000

tf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tf = tfidf_vectorizer.fit_transform(documents)
tf_feature_names = tfidf_vectorizer.get_feature_names()

#-----------------------#

from sklearn.decomposition import NMF, LatentDirichletAllocation

no_topics = 10
nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tf)

#-----------------------#

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                            for i in topic.argsort()[:-no_top_words - 1:-1]])
        print(message)
    print()

#------------------------#

no_top_words = 3
display_topics(nmf, tf_feature_names, no_top_words)
