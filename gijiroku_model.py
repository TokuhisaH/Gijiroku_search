
from gensim.models import word2vec

years=["196","197","198","199","200","201"]

for year in years:
    data = word2vec.LineSentence("gijiroku"+year+"0utf8.txt")
    print(year+"0load ok")
    model = word2vec.Word2Vec(data,size=100)
    model.save("gijiroku"+year+"0.model")

print("ok")

