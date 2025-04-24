from pyspark.sql import SparkSession
from pyspark.sql import Row


def run() -> None:
    spark = (
        SparkSession.builder
        .appName('practice-spark')
        .getOrCreate())

    # What it gives you:
    # 1. Schema inferred from the CSV file
    # 2. Column names(from header)
    # 3. High - level APIs for filtering, grouping, joining, SQL ops
    # 4. Optimized execution with Catalyst & Tungsten
    pokemons = spark.read.option('header', 'true').csv('./pokemon_data.csv')
    pokemons.printSchema()
    pokemons.show(5)

    print('-------------------------------------------------------------')
    # RDD example - manual work less optimized, lambda function for filter and map
    rdd = spark.sparkContext.textFile("./pokemon_data.csv")
    header = rdd.first()
    rdd_no_header = rdd.filter(lambda row: row != header)
    parsed_rdd = rdd_no_header.map(lambda line: line.split(","))
    parsed_rdd.take(5)

    fields = header.split(",")
    row_rdd = parsed_rdd.map(lambda x: Row(**dict(zip(fields, x))))
    df_from_rdd = spark.createDataFrame(row_rdd)
    df_from_rdd.printSchema()
    df_from_rdd.show(5)

    # Transformation - spark lazy evaluation (generating a plan for execution)
    transformed = pokemons.filter("HP > 75").orderBy('HP', ascending=False).select('Name', 'HP')

    # Increasing and decreasing num of partitions in Spark
    products = spark.read.option('header', 'true').csv('./products.csv')
    products = products.repartition(10)
    products.getNumPartitions()
    products = products.coalesce(5)
    products.getNumPartitions()
    print('stop here')


if __name__ == '__main__':
    run()
