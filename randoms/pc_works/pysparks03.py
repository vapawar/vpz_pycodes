from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("testApp").getOrCreate()
sc = spark.sparkContext

dt01 = spark.read.json("data/prize.json")
spark.createDataFrame(dt01.collect()[0][0]).createOrReplaceTempView("test12")
spark.sql("select year, category,laureates from test12").show(4)

dt02=spark.read.csv("data/Sample_DataSet.csv",inferSchema=True,header=True)
dt02.createOrReplaceTempView("psdt")
spark.sql("select * from psdt where 'APPROVED AMOUNT' !=0").show(4)

dt03=spark.read.csv("data/pubs.csv",inferSchema=True,header=True)
dt03.createOrReplaceTempView("pubs")
spark.sql("select * from pubs where address3 is not null").show(8)
print("==========================")
spark.sql("select borough_code, borough_name from pubs \
          where borough_name not like 'B%' and borough_name not like '%Cro%'").show(40)
dt04=spark.read.csv("data/titanic.csv", inferSchema=True, header=True)
dt04.createOrReplaceTempView("ttnk")
dt04.filter("sex = 'male'").show(4)
spark.sql("select * from ttnk").show(8)