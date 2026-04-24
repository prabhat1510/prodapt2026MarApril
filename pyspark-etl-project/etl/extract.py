def extract_data(spark):
    orders = spark.read.csv("data/raw/orders.csv", header=True, inferSchema=True)
    customers = spark.read.csv("data/raw/customers.csv", header=True, inferSchema=True)
    products = spark.read.csv("data/raw/products.csv", header=True, inferSchema=True)
    
    return orders, customers, products