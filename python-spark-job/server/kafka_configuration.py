from pyspark.sql import SparkSession
import os
from pyspark.sql.types import StructType, StructField, StringType

topic = "job_description_dataset"
kafka_brokers = "localhost:9092"

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.2.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0,org.mongodb.spark:mongo-spark-connector_2.12:3.0.1 pyspark-shell'

def initKafkaStreaming():
    spark = SparkSession.builder.appName("Kafka Pyspark Streaming Learning") \
        .master("local[*]") \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("ERROR")
    return spark

def read_from_kafka(spark):
    df = spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", kafka_brokers) \
        .option("subscribe", topic) \
        .option("startingOffsets", "latest") \
        .load()
    return df

def getSparkSchema():
    schema = StructType([
        StructField("title", StringType(), True),
        StructField("location", StringType(), True),
        StructField("company_name", StringType(), True),
        StructField("date_posted", StringType(), True),
        StructField("job_type", StringType(), True),
        StructField("description", StringType(), True)
    ])
    return schema
