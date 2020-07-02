from pyspark.ml.feature import StopWordsRemover, NGram, Binarizer
from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("stopworkremover").getOrCreate()

seqdata=spark.createDataFrame([(0,["I","saw","the","red","balloon"]),
    (1,["Mary","had","a","little","lamb"])], ["id","raw"])
remover=StopWordsRemover(inputCol="raw", outputCol="Filtered")
remover.transform(seqdata).show(truncate=False)


wordDataFrame = spark.createDataFrame([
    (0, ["Hi", "I", "heard", "about", "Spark"]),
    (1, ["I", "wish", "Java", "could", "use", "case", "classes"]),
    (2, ["Logistic", "regression", "models", "are", "neat"])
], ["id", "words"])
ngram=NGram(n=2, inputCol="words", outputCol="ngrams")
ngramdf=ngram.transform(wordDataFrame)
ngramdf.select("ngrams").show(truncate=False)


continuousDataFrame = spark.createDataFrame([
    (0, 0.1),
    (1, 0.8),
    (2, 0.2)
], ["id", "feature"])
binarizer=Binarizer(threshold=0.1, inputCol="feature", outputCol="binarized_feature")
bnzrDataframe=binarizer.transform(continuousDataFrame)
print("binarizer threshold",binarizer.getThreshold())
bnzrDataframe.show(truncate=False)