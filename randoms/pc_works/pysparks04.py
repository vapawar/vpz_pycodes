from pyspark.sql import SparkSession

spark=SparkSession.builder.getOrCreate()

#df=spark.read.load("data/users.parquet")
#df.select("name", "favorite_color").write.save("namesandfcolors.parquet")
#
#df=spark.read.load("data/people.json", format="json")
#df.select("name","age").write.save("nameandage.parquet",format="parquet")
print("success.........................................................")

df=spark.read.load("data/peoples.csv",format="csv", sep=",", inferSchema=True, Header=True)

df=spark.read.load("data/users.orc")
(df.
 write.
 format("orc").
 option("orc.bloom.filter.columns","favorite_color")
 .option("orc.dictionary.key.threshold",1.0)
 .save("userswithopts.orc"))

df=spark.sql("select * from parquet.`data/users.parquet`")

df.show(12)

df.write.bucketBy(42,"name").sortBy("age").saveAsTable("ppl_bkted")
df.write.partitionBy("favorite_color").format("parquet").save("namesPartByColor.parquet")

df=spark.read.parquet("data/users.parquet")
(df
 .write
 .partitionBy("favorite_color")
 .bucketBy(42, "name")
 .saveAsTable("people_partitioned_bucketed"))