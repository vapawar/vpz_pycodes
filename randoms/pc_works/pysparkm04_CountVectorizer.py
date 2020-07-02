from pyspark.ml.feature import CountVectorizer
from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("CountVectorizer").getOrCreate()

df=spark.createDataFrame([
        (0,"a b c".split(" ")),
        (0,"a b b c a".split(" "))
        ],["id","words"])

cv = CountVectorizer(inputCol="words", outputCol="features", vocabSize=3, minDF=2.0)
model=cv.fit(df)

result=model.transform(df)
result.show(truncate=False)