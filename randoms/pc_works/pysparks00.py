from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("test").getOrCreate()

df=spark.read.csv("data/titanic.csv",inferSchema=True, header=True)
df.printSchema()
x1=df.select("Survived").rdd.flatMap(lambda x:x).collect()
print(len(x1))
print(df.columns)
print(df.count())

x=[1,4,2,4,5]
y=[t*2**4 for t in x]
print(y)