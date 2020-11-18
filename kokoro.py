from janome.tokenizer import Tokenizer
from gensim.models import word2vec
import re

with open('sample.txt','r') as file:
    text = file.read()

t = Tokenizer()
results = []
r = []

lines = text.split("\n")
for line in lines:
    s = line
    s = re.sub(r'[a-zA-Z\d ]+', '', s)
    s = re.sub(r'[年月]*日', '', s)
    s = re.sub(r'[\(\):;]','', s)
    tokens = t.tokenize(s)

    for tok in tokens:
        w = tok.surface
        r.append(w)
       
    
print(r)

wakati_file = 'kokoro.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))

data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data,
    size=200, window=10, hs=1, min_count=2, sg=1)
model.save('kokoro.model')
print('ok') 