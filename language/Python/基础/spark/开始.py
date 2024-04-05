from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

sc=SparkContext(conf=conf)

print(sc.version)

sc.stop()