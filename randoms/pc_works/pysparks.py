from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

logFile = "data/README.md"
logData = spark.read.text(logFile).cache()
numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

d1=spark.read.json("data/people.json")
d2=spark.read.csv("data/pima-indians-diabetes.csv")
d3=spark.read.parquet("data/users.parquet")
d4=spark.read.text("data/people.txt")

d1.printSchema()
d2.printSchema()
d3.printSchema()
d4.printSchema()
d2.select()

print(d3.select("name").show())
print(d1.schema.jsonValue().keys())

print("d1 head-2: ", d1.head(2))
print("d2 head-2: ", d2.head(2))
print("colomn 98 rows: ",d2.select("_c1").show(98))
d1.show()
d2.show()

spark.stop()