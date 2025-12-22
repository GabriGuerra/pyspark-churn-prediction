import os
import findspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

def main():
    # Ajuste os caminhos abaixo conforme o seu ambiente local
    os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
    os.environ["SPARK_HOME"] = "/content/spark-3.5.1-bin-hadoop3"  # Exemplo, mude para seu caminho real

    findspark.init()

    spark = SparkSession.builder \
        .appName("Atividade Spark") \
        .master("local[*]") \
        .getOrCreate()

    spark.conf.set("spark.sql.repl.eagerEval.enabled", True)

    # Caminho do arquivo CSV
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'churn-bigml-20.csv')

    df = spark.read.csv(data_path, header=True, inferSchema=True)

    print("\nMostrando as 5 primeiras linhas:")
    df.show(5)

    print("\nMédia de Total day calls por Area code:")
    df.groupBy("Area code") \
      .agg(avg("Total day calls").alias("media_total_day_calls")) \
      .show()

    print("\nMédia de Total day minutes por Area code:")
    df.groupBy("Area code") \
      .agg(avg("Total day minutes").alias("media_total_day_minutes")) \
      .show()

    print("\nRegistros com Total night calls < 55:")
    df.filter(df["Total night calls"] < 55).show()

    spark.stop()

if __name__ == "__main__":
    main()
