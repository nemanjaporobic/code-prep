from pyspark.sql import SparkSession
from pyspark.sql import Row


def run() -> None:
    spark = (
        SparkSession.builder
        .appName('practice-spark')
        .getOrCreate())

    employee_data = [
        (1, 'Alice', 'HR', 5000, ['red', 'blue']),
        (2, 'Bob', 'IT', 6000, ['green']),
        (3, 'Charlie', 'HR', 4500, ['blue', 'green', 'red']),
        (4, 'David', 'IT', 7000, ['yellow', 'red', 'blue']),
        (5, 'Eve', 'Sales', 5500, ['pink', 'red'])
    ]

    employees = spark.createDataFrame(employee_data, ['id', 'name', 'dept', 'salary', 'fav_colors'])

    sale_data = [
        (1, 'East', 100),
        (2, 'East', 200),
        (3, 'West', 150),
        (4, 'East', 50),
        (5, 'West', 300)
    ]

    sales = spark.createDataFrame(sale_data, ['id', 'region', 'sale'])

    orders_data = [
        (100, 1, '2024-01-01'),
        (101, 2, '2024-01-03'),
        (102, 3, '2024-01-05'),
        (103, 1, '2024-01-07'),
        (104, 10, '2024-02-02'),
    ]
    orders = spark.createDataFrame(orders_data, ['id', 'employee_id', 'order_date'])

    customers = spark.createDataFrame([
        (1, 'Alice'),
        (2, 'Bob'),
        (3, 'Charlie')
    ], ['id', 'name'])

    transactions = spark.createDataFrame([
        (101, 1, '2024-01-01', 200),
        (102, 2, '2024-01-05', 400),
        (103, 1, '2024-01-15', 150),
        (104, 1, '2024-01-22', 100)
    ], ['id', 'customer_id', 'order_date', 'amount'])

    web_logs = spark.createDataFrame([
        (1, "2024-01-01 10:00:00"),
        (1, "2024-01-01 10:05:00"),
        (1, "2024-01-01 11:00:00"),
        (2, "2024-01-01 09:00:00"),
        (2, "2024-01-01 09:45:00")
    ], ['customer_id', 'timestamp'])

    print('finish')


if __name__ == '__main__':
    run()
    # df_hr = df.filter(col("dept") == "HR")
    # df_with_bonus = df.withColumn("bonus", col("salary") * 0.1)
    # avg_salary = df.groupBy("dept").agg(avg("salary").alias("avg_salary"))

    # window_spec = Window.partitionBy("region").orderBy(col("sale").desc())
    # df_ranked = df.withColumn("rank", row_number().over(window_spec))

    # name_length_udf = udf(name_length, IntegerType())
    # df_udf = df.withColumn("name_len", name_length_udf(col("name")))
    # df_builtin = df.withColumn("name_len", length(col("name")))

    # df_exploded = df.withColumn("color", explode("favorite_colors"))
    # df_color_count = df_exploded.groupBy("color").count()

    # joined_df = orders_df.join(customers_df, on="cust_id", how="inner")
    # unknown_cust_orders = orders_df.join(customers_df, on="cust_id", how="left_anti")
    # no_order_customers = customers_df.join(orders_df, on="cust_id", how="left_anti")

