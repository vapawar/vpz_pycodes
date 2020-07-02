from pyspark.ml.linalg import Vectors
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("Pipeline").getOrCreate()
#Example: Estimator, Transformer, and Param
training=spark.createDataFrame([(1.0, Vectors.dense([0.0, 1.1, 0.1])),
    (0.0, Vectors.dense([2.0, 1.0, -1.0])),
    (0.0, Vectors.dense([2.0, 1.3, 1.0])),
    (1.0, Vectors.dense([0.0, 1.2, -0.5]))],["label", "features"])
lr=LogisticRegression(maxIter=10, regParam=0.01)
print("LogisticRegression: ", lr.explainParams())
model1=lr.fit(training)
print("Model1 was fit using params:")
print(model1.extractParamMap())
paramMap={lr.maxIter:20}
paramMap[lr.maxIter]=30
paramMap.update({lr.regParam:0.1, lr.threshold:0.55})
paramMap2={lr.probabilityCol:"myProbability"}
paramMapCombined=paramMap.copy()
paramMapCombined.update(paramMap2)
model2=lr.fit(training, paramMapCombined)
print("Model2 was fit using params:")
print(model2.extractParamMap())
test=spark.createDataFrame([
    (1.0, Vectors.dense([-1.0, 1.5, 1.3])),
    (0.0, Vectors.dense([3.0, 2.0, -0.1])),
    (1.0, Vectors.dense([0.0, 2.2, -1.5]))], ["label", "features"])
prediction=model2.transform(test)
result=prediction.select("features", "label", "myProbability", "prediction").collect()
for row in result:
    print(row.features, row.label, row.myProbability, row.prediction)


#Example: Pipeline
from pyspark.ml import Pipeline
from pyspark.ml.feature import HashingTF, Tokenizer

training_data=spark.createDataFrame([(0, "a b c d e spark", 1.0),
    (1, "b d", 0.0),(2, "spark f g h", 1.0),(3, "hadoop mapreduce", 0.0)],
    ["id","text", "label"])
tokenizer=Tokenizer(inputCol="text", outputCol="words")
hashTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
lr=LogisticRegression(maxIter=10, regParam=0.001)
pipeline=Pipeline(stages=[tokenizer, hashTF, lr])
model=pipeline.fit(training_data)

test=spark.createDataFrame([(4, "spark i j k"),(5, "l m n"),
    (6, "spark hadoop spark"),(7, "apache hadoop")], ["id", "text"])
prediction=model.transform(test)
selected=prediction.select("id","text","features","prediction")
[print(t) for t in selected.collect()]

for row in selected.collect():
    rid, text, prob, prediction = row
    print("(%d, %s) --> prob=%s, prediction=%f" % (rid, text, str(prob), prediction))