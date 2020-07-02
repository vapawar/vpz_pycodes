from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("TF_IDF_Tokenizer").getOrCreate()

senetnceData=spark.createDataFrame([(0.0, "Hi I heard about Spark"),
                                    (0.0, "I wish Java could use case classes"),
                                    (1.0, "Logistic regression models are neat")],
                                    ["label", "sentence"])
tokenizer=Tokenizer(inputCol="sentence", outputCol="words")
wordsData=tokenizer.transform(senetnceData)
wordsData.show(truncate=False)

hashTF=HashingTF(inputCol="words", outputCol="rawfeatures", numFeatures=20)
featurizedData=hashTF.transform(wordsData)
featurizedData.show(truncate=False)

idf=IDF(inputCol="rawfeatures", outputCol="features")
idfmodel=idf.fit(featurizedData)
rescaledData=idfmodel.transform(featurizedData)
rescaledData.select("label", "features").show(truncate=False)