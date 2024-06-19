from pyspark.sql.functions import from_json, col
from kafka_configuration import getSparkSchema
from parse_html_content import get_cleaned_html

def consume_streams_and_save_to_redshift(df):
    df = df.selectExpr("CAST(value AS STRING) as json_str")
    df = df.withColumn("json_data", from_json("json_str", getSparkSchema()))

    clean_html_udf = get_cleaned_html()

    df = df.select(col("json_data.title"),
        col("json_data.location"),
        col("json_data.company_name"), 
        col("json_data.date_posted"), 
        col("json_data.job_type"), 
        clean_html_udf(col("json_data.description")).alias("cleaned_description")
    )

    query = df.writeStream \
        .outputMode("update") \
        .foreachBatch(lambda batch_df, batch_id: batch_df.write \
            .format("com.mongodb.spark.sql.DefaultSource") \
            .mode("append") \
            .option("uri", "mongodb+srv://USERNAME:PASSWORD@HOST_NAME/?retryWrites=true&w=majority&appName=Cluster0") \
            .option("database", "job_description_dataset") \
            .option("collection", "job_description") \
            .save()
        ).start()

    query.awaitTermination()
