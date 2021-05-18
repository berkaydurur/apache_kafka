# apache_kafka
Python tabanlı Apache Kafka ile temel produce ve consume işlemlerini yapabilen bir uygulama. Sahte veri kullanmaktadır.

Bu uygulama Python dilini ve kafka-python kütüphanesi ile Kafka'ya ulaşımını kullanır. Data Faker kütüphanesi ile üretilmektedir. Consume işlemi ise shell konsolundan bir script ile gerçekleştirilir. Script datayı konsola yazdırmaktadır.

Docker file içinde container içine alınmış uygulamayı aşağıdaki komut ile build'leyebilirsiniz.
docker build -t dockerpython.
