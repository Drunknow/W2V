from janome.tokenizer import Tokenizer
from gensim.models import word2vec
import re

with open('sample.txt','r') as file:
    text = file.read()
    text = re.sub(r'[a-zA-Z\d]+', '', text)
    text = re.sub(r'[年月]*日', '', text)
    text = re.sub(r'[\(\):;]','', text)
t = Tokenizer()

def extract_words(text):
    tokens = t.tokenize(text)
    return [token.base_form for token in tokens 
        if token.part_of_speech.split(',')[0] in['名詞', '動詞']]

sentences = text.split('。')
# それぞれの文章を単語リストに変換(処理に数分かかります)
word_list = [extract_words(sentence) for sentence in sentences]

# 結果の一部を確認 
for word in word_list[0]:
    print(word)

model = word2vec.Word2Vec(word_list, size=100,min_count=5,window=5,iter=100)


while 1:
    print()
    print("単語：", end="")
    try:
        ret = model.wv.most_similar(positive=[input()]) 
        for item in ret:
            print("　-", item[0], item[1])
    except:
        print("存在しない単語です")
