from pyspark.ml.feature import PCA
from pyspark.ml.linalg import Vectors

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("spark_PCA").getOrCreate()

data = [(Vectors.sparse(5, [(1, 1.0), (3, 7.0)]),),
        (Vectors.dense([2.0, 0.0, 3.0, 4.0, 5.0]),),
        (Vectors.dense([4.0, 0.0, 0.0, 6.0, 7.0]),)]

dataframe=spark.createDataFrame(data,["features"])
pca=PCA(k=3, inputCol="features", outputCol="pca_features")
model=pca.fit(dataframe)
result=model.transform(dataframe).select("pca_features")
result.show(truncate=False)