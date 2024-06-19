docker-compose up -d
/opt/kafka/bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic job_description_dataset

/opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic job_description_dataset --from-beginning

