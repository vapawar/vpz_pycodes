from pyspark.sql.types import StringType,StructField,StructType
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
sc = spark.sparkContext

lines = sc.textFile("data/people.txt")
parts=lines.map(lambda l:l.split(","))
people=parts.map(lambda p:(p[0],p[1].strip()))
schema_str="name age"

fields=[StructField(fname, StringType(), True) for fname in schema_str.split()]
schema=StructType(fields)

schema_people=spark.createDataFrame(people, schema)
schema_people.createOrReplaceTempView("people")
results=spark.sql("select name from people")
results.show()