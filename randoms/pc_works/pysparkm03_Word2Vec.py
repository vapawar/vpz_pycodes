from pyspark.ml.feature import Word2Vec
from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("Word2Vec").getOrCreate()

docDF=spark.createDataFrame([
        ("Hi I have heard about spark".split(" "),),
        ("I wish Java could use case classes".split(" "),),
        ("logistic regression models are neat".split(" "),)
        ],["text"])

word2vec=Word2Vec(vectorSize=3, minCount=0, inputCol="text", outputCol="result")
model=word2vec.fit(docDF)

result=model.transform(docDF)
for row in result.collect():
    text, vector=row
    print("Text:[%s] \n Vector: %s\n"%(", ".join(text), str(vector)))

result.show(truncate=False)