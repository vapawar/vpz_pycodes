from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

spark=SparkSession.builder.appName("test").getOrCreate()
data=spark.read.load("data/US_Accidents_May19.csv",format="csv",inferSchema=True,Header=True)
# df.printSchema()
data.createOrReplaceTempView("data")
df2 = spark.sql("select * from data limit 9999")
df2.groupBy("City").count().show(False)

