from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
from gensim.models import FastText
from gensim.models import KeyedVectors
from scipy.stats import spearmanr
import sys

# For Word2Vec models
#model = Word2Vec.load("publico-COMPLETO.txt.model")

# For FastText models
#model = FastText.load("FASTTEXT-MODEL")

# For either of the above when in TXT format
model = KeyedVectors.load_word2vec_format(sys.argv[1], binary=False)

pares_list = []
likert = {}

with open(sys.argv[2]) as file:
    for line in file:
        w = line.split(";")
        par = (w[0].rstrip(), w[1].rstrip())
        pares_list.append(par)
        likert.update({par:float(w[2].rstrip())})

similaridadesDoModelo = []
similaridadesDoLikert = []

# Creates file to store results

for par in pares_list:
    try:
        similarity = model.similarity(par[0], par[1])
        similaridadesDoModelo.append(similarity)
        similaridadesDoLikert.append(likert.get((par[0], par[1])))
    except:
        similaridadesDoModelo.append('NaN')
        similaridadesDoLikert.append(likert.get((par[0], par[1])))

print(spearmanr(similaridadesDoModelo, similaridadesDoLikert))