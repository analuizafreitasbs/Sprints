# EU FIZ NO GOOGLE COLAB, POIS NA LINHA DE COMANDO NORMAL DEMOROU DEMAIS PARA RODAR E
# ESTOU ENTREGANDO UM POUCO DEPOIS, POIS FOQUEI NO DESAFIO E NA FACULDADE, ISSO FOI ACORDADO COM O MONITOR 

!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!pip install pyspark

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/usr/local/lib/python3.10/dist-packages/pyspark"

# Baixar o arquivo README.md
!wget https://github.com/analuizafreitasbs/Sprints/blob/main/Readme.md -O README.md

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Word Count") \
    .getOrCreate()

text_file = spark.read.text("README.md").rdd

# Contar ocorrências de palavras do meu readme do git
from operator import add

counts = text_file.flatMap(lambda line: line.value.split(" ")) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(add)

output = counts.collect()

for (word, count) in output:
    print(f"{word}: {count}")