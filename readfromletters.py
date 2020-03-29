import csv
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import NMF
import nltk
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
#nltk.download('wordnet')
#sorted(list(stopwords.words("english")))[:20]

#csv_f = csv.reader(f)
texts = []
#for row in csv_f:
#    texts.append(row[1])
df = pd.read_csv('bigletters.csv',skiprows= [1])
texts=df['Text'].values.astype('U').tolist()
#print(df)
print(texts[1])
print(len(texts))

vectorizer = CountVectorizer(stop_words='english')
vecs = vectorizer.fit_transform(texts).todense()
print(vecs.shape)
#print(vecs)
vocab = np.array(vectorizer.get_feature_names())
#print(vocab.shape)
#for v in vocab[0:50]:
#    print(v)
#    print(type(v))


U, s, Vh = np.linalg.svd(vecs, full_matrices=False)
#print(U.shape, s.shape, Vh.shape)

#print(type(vocab))
#print(type(vocab[0]))

num_top_words = 8
#print(Vh)

def show_topics(a):
    top_words = lambda t: [vocab[i] for i in np.argsort(t)[:-num_top_words-1:-1]]
    topic_words = ([top_words(t) for t in a])
    return [t for t in topic_words]
    #return(topic_words[0][0][0])
thing = show_topics(Vh[:10])
for i in thing:
    print(i[0][0][:10])





clf = NMF(n_components=50, random_state = 0)
W1 = clf.fit_transform(vecs)
H1 = clf.components_
thing2 = show_topics(H1)
print("\nCLF")
int = 0
for i in thing2:
    print(int, i[:10])
    int = int + 1

plt.plot(W1[0])
#plt.plot(s)
plt.show()
