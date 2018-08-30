documents = []

file = open('Tratando Arquivos/data.txt', 'r')
i = 0
for line in file:
    documents.append(line)
    i = i + 1
    print(i)
file.close()
#-----------------------#

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

no_features = 1000

tf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tf = tf_vectorizer.fit_transform(documents)
tf_feature_names = tf_vectorizer.get_feature_names()

#-----------------------#

from sklearn.decomposition import NMF, LatentDirichletAllocation

no_topics = 20
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

no_top_words = 5
display_topics(nmf, tf_feature_names, no_top_words)
