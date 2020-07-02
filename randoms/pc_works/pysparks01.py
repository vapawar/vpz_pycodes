from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("pysql_base_example").getOrCreate()
df=spark.read.json("data/people.json")

#show the content of the DataFrame
df.show()

##Print the schema in a tree format
df.printSchema()

##select name and age
df.select("name","age").show()
df.select("age", "name").show()
##select age+12
df.select(df["name"],df["age"]+12).show()
##filter ages > 25
df.filter(df["age"]>25).show()

##Count people by age
df.groupBy("age").count().show()

##views local and golbal
df.createOrReplaceTempView("test")
spark.sql("select * from test where age > 25").show()
df.createOrReplaceGlobalTempView("gtest")
spark.sql("SELECT * FROM global_temp.gtest where age < 30 ").show()

from pyspark import Row
sc = spark.sparkContext   
lines = sc.textFile("data/people.txt")
parts=lines.map(lambda l:l.split(","))
people=parts.map(lambda p:Row(name=p[0],age=int(p[1])))
schema_people=spark.createDataFrame(people)
schema_people.show()
schema_people.select("name").show()
schema_people.createOrReplaceTempView("people")
teenagers=spark.sql("select * from people where age < 21 and age > 12")
teenNames=teenagers.rdd.map(lambda l:"Name: "+l.name).collect()
print(teenNames)
for name in teenNames:
    print(name)