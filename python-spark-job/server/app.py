from kafka_configuration import initKafkaStreaming, read_from_kafka
from process_message import consume_streams_and_save_to_redshift

if __name__ == "__main__":
    spark = initKafkaStreaming()
    df = read_from_kafka(spark)
    consume_streams_and_save_to_redshift(df)
