'''Q1'''
'''MongoDB is a popular open-source, document-oriented NoSQL (non-relational) database. It provides a flexible and 
scalable approach to storing and managing data, especially when dealing with unstructured or semi-structured data.

Non-relational databases, also known as NoSQL databases, differ from traditional relational databases (SQL databases) 
in several ways:

1. Data model: NoSQL databases use various data models, such as key-value, document, column-family, or graph, 
allowing greater flexibility in organizing and representing data compared to the tabular structure of SQL databases.

2. Schema flexibility: NoSQL databases typically have dynamic or schema-less data models, which means each record 
can have different attributes or fields. This adaptability is useful when dealing with evolving data structures.

3. Scalability: NoSQL databases are designed to scale horizontally, meaning they can handle increasing amounts of 
data and traffic by distributing data across multiple servers, which is beneficial in high-demand applications.

4. Performance: NoSQL databases often prioritize speed and low-latency operations, making them suitable for real-time 
data processing and high-throughput applications.

5. CAP theorem: NoSQL databases favor availability and partition tolerance over strict consistency (CAP theorem), 
which means they may not provide immediate consistency but offer high availability even during network partitions.

When to prefer MongoDB over SQL databases:

1. **Flexible Data Model**: If your data is semi-structured or frequently changing, MongoDB's document-oriented 
data model allows you to store data without needing a fixed schema. This is particularly useful for projects where 
data requirements may evolve over time.

2. **Scalability and Performance**: MongoDB excels in distributed, high-traffic environments. If your application 
demands horizontal scalability and low-latency reads and writes, MongoDB may be a better fit than traditional SQL 
databases.

3. **Large Volumes of Unstructured Data**: When dealing with large volumes of unstructured or complex data, such as 
JSON-like documents or nested data, MongoDB's document-based storage is more natural to work with compared to the 
rigid structure of SQL databases.

4. **Aggregation and Analytics**: MongoDB's flexible data model and support for aggregation pipelines make it 
well-suited for performing complex data analytics and aggregation tasks.

5. **Cloud-Native Applications**: For cloud-based applications, MongoDB's horizontal scaling capabilities and 
native integration with cloud services make it a popular choice.

6. **Rapid Development**: MongoDB's simplicity and ease of use can lead to faster development cycles, making it 
an attractive option for projects with tight deadlines.

However, it's important to note that each database type has its strengths and weaknesses, and the choice between 
MongoDB and SQL databases (like MySQL, PostgreSQL, etc.) depends on the specific requirements and nature of your 
application. For highly structured and relational data, strict ACID transactions, and mature tooling for complex 
queries, SQL databases may still be the preferred choice. Always consider your project's specific needs and 
constraints before deciding on a database solution.'''

'''Q2'''
'''MongoDB offers several key features that make it a popular choice for developers working with NoSQL databases:

1. **Document-Oriented**: MongoDB stores data in flexible, JSON-like BSON (Binary JSON) documents. Each document can 
have different fields and data types, allowing easy representation of complex and nested data structures.

2. **Schema Flexibility**: MongoDB has a dynamic schema, which means that documents within a collection do not need 
to follow a predefined schema. New fields can be added to documents without affecting other documents in the collection.

3. **High Performance**: MongoDB's design prioritizes performance, making it suitable for high-throughput applications 
and real-time data processing. It uses memory-mapped files for efficient data access and indexes to speed up queries.

4. **Horizontal Scalability**: MongoDB can scale horizontally by sharding data across multiple servers. This approach 
allows it to handle large amounts of data and heavy traffic by distributing the load.

5. **Replication and High Availability**: MongoDB supports automatic replication, creating copies of data across 
multiple servers. If the primary server fails, one of the replicas can take over as the new primary, ensuring high 
availability and data redundancy.

6. **Rich Query Language**: MongoDB provides a powerful query language that supports a wide range of operations, 
including filtering, sorting, aggregation, and geospatial queries. It allows for complex queries and analytics.

7. **Indexing**: MongoDB supports various types of indexes (e.g., single field, compound, geospatial, text) to 
optimize query performance. Properly indexed queries can significantly improve read performance.

8. **Aggregation Framework**: MongoDB offers a versatile aggregation framework for data processing tasks. It allows 
users to perform complex data transformations, aggregations, and computations directly within the database.

9. **Geospatial Capabilities**: MongoDB has built-in support for geospatial data and geospatial queries, making it 
suitable for location-based applications and services.

10. **Ad Hoc Queries**: MongoDB supports ad hoc queries, allowing developers to query data using field names and values
 with a flexible syntax, making it easy to explore and analyze data.

11. **GridFS**: MongoDB includes GridFS, a specification for storing and retrieving large files (e.g., images, videos) 
as chunks in the database. It allows efficient storage and retrieval of large binary data.

12. **Security Features**: MongoDB provides various security features, including authentication, access control, 
encryption at rest, and field-level encryption. These features help ensure data security and privacy.

13. **Native Aggregation**: MongoDB's native aggregation framework enables complex data processing operations within 
the database, reducing the need for external data processing tools.

Overall, MongoDB's combination of flexibility, performance, scalability, and ease of use has made it a popular 
choice for a wide range of applications, from small-scale projects to large, distributed systems. Its document-oriented 
approach and support for various data types make it particularly suitable for applications with evolving data structures 
and large volumes of unstructured or semi-structured data.'''

'''Q3'''
'''To connect to MongoDB from Python, you'll need to use a MongoDB driver. The most popular driver for Python is "PyMongo." Make sure you have PyMongo installed before running the code. You can install it using pip:'''

pip install pymongo

'''Now, let's write a Python script to connect to MongoDB, create a database, and a collection:'''
import pymongo

# Replace these values with your MongoDB connection string
# If MongoDB is running on localhost, the default port is 27017
mongo_uri = "mongodb://localhost:27017/"

# Connect to MongoDB server
client = pymongo.MongoClient(mongo_uri)

# Create a new database (replace 'my_database' with your desired database name)
db_name = "my_database"
database = client[db_name]

# Create a new collection within the database (replace 'my_collection' with your desired collection name)
collection_name = "my_collection"
collection = database[collection_name]

# Insert some sample data into the collection
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]

# Insert data into the collection
collection.insert_many(data)

# Close the connection to MongoDB
client.close()

print(f"Connected to MongoDB, and the '{collection_name}' collection in the '{db_name}' database has been created.")

'''Make sure you have MongoDB running on your local machine on the default port (27017) while executing the script. 
The code will connect to the MongoDB server, create a database named "my_database," and a collection named "my_collection." 
It will then insert some sample data into the collection and close the connection.
Remember to replace the connection string with your actual MongoDB server URI if it's hosted on a different machine or port.'''

'''Q4'''
import pymongo

# Replace this with your MongoDB connection string
mongo_uri = "mongodb://localhost:27017/"

# Connect to MongoDB server
client = pymongo.MongoClient(mongo_uri)

# Specify the database and collection names
db_name = "my_database"
collection_name = "my_collection"
database = client[db_name]
collection = database[collection_name]

# Function to insert one record into the collection
def insert_one_record(data):
    result = collection.insert_one(data)
    print(f"Inserted record with _id: {result.inserted_id}")

# Function to insert multiple records into the collection
def insert_many_records(data_list):
    result = collection.insert_many(data_list)
    print(f"Inserted {len(result.inserted_ids)} records with the following _ids: {result.inserted_ids}")

# Sample data to insert
one_record = {"name": "David", "age": 28, "city": "Chicago"}

many_records = [
    {"name": "Eva", "age": 24, "city": "Boston"},
    {"name": "Frank", "age": 32, "city": "Seattle"}
]

# Insert one record into the collection
insert_one_record(one_record)

# Insert multiple records into the collection
insert_many_records(many_records)

# Find and print the inserted records
print("\nInserted Records:")
for record in collection.find():
    print(record)

# Find and print one inserted record
print("\nOne Inserted Record:")
one_inserted_record = collection.find_one({"name": "David"})
print(one_inserted_record)

# Close the connection to MongoDB
client.close()
'''In this code, we've created two functions, insert_one_record() and insert_many_records(), to demonstrate 
inserting single and multiple records into the MongoDB collection. We then use the find() method to retrieve 
and print all inserted records and the find_one() method to retrieve and print one specific inserted record.
Remember to replace the connection string with your actual MongoDB server URI if it's hosted on a different machine 
or port. Also, ensure that the previously created database and collection names match the names used in this code.'''

'''Q5'''
'''In MongoDB, the find() method is used to query the database and retrieve documents that match specific criteria. 
It allows you to perform various types of queries, including filtering documents based on specific field values, 
using comparison operators, and performing complex queries using logical operators.'''
import pymongo

# Replace this with your MongoDB connection string
mongo_uri = "mongodb://localhost:27017/"

# Connect to MongoDB server
client = pymongo.MongoClient(mongo_uri)

# Specify the database and collection names
db_name = "my_database"
collection_name = "my_collection"
database = client[db_name]
collection = database[collection_name]

# Sample data to insert (if not already inserted)
sample_data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]
collection.insert_many(sample_data)

# Example of using the find() method to query the database
# Query to find documents where the 'city' field is 'New York'
query = {"city": "New York"}

# Executing the query using find() and printing the results
results = collection.find(query)
print("Documents with 'city' field equal to 'New York':")
for document in results:
    print(document)

# Close the connection to MongoDB
client.close()
'''In this code, we first connect to the MongoDB server and then specify the database and collection names. 
We insert some sample data (if not already inserted) into the collection. We then use the find() method to query 
the database for documents where the 'city' field is equal to 'New York'. The results are printed using a loop to 
iterate through the returned cursor. This code will display all the documents that match the specified query criteria.'''

'''Q6'''
'''In MongoDB, the sort() method is used to sort the results of a query in ascending or descending order based on one or 
more fields. Sorting is particularly useful when you want to retrieve data in a specific order, such as alphabetical 
order, numerical order, or based on timestamps.'''
import pymongo

# Replace this with your MongoDB connection string
mongo_uri = "mongodb://localhost:27017/"

# Connect to MongoDB server
client = pymongo.MongoClient(mongo_uri)

# Specify the database and collection names
db_name = "my_database"
collection_name = "students"
database = client[db_name]
collection = database[collection_name]

# Sample data to insert (if not already inserted)
sample_data = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 88},
    {"name": "Eva", "score": 96}
]
collection.insert_many(sample_data)

# Example of using the sort() method to sort the data by the 'score' field in descending order
query = {}  # Empty query to retrieve all documents
sort_field = "score"  # Sort based on the 'score' field
sort_order = -1  # Sort in descending order

# Executing the query with sort() and printing the sorted results
results = collection.find(query).sort(sort_field, sort_order)
print("Sorted by 'score' field in descending order:")
for document in results:
    print(document)

# Close the connection to MongoDB
client.close()
'''In this example, we connect to the MongoDB server and specify the database and collection names. We insert some 
sample data (if not already inserted) into the "students" collection. We then use the sort() method to query the 
database for all documents and sort them based on the 'score' field in descending order. The results are printed using 
a loop to iterate through the returned cursor. This code will display all the documents sorted by the 'score' field 
in descending order, from the highest score to the lowest score.'''

'''Q7'''
'''Certainly! Let's go through the use cases for `delete_one()`, `delete_many()`, and `drop()` methods in MongoDB:

1. `delete_one()`:

- Use: The `delete_one()` method is used to delete a single document that matches the specified filter criteria from the collection.
- Syntax: `collection.delete_one(<filter>)`
- `<filter>`: Specifies the criteria for selecting the document to delete. It is a dictionary representing the query filters.

Use Cases:
   - When you want to remove a specific document based on a given condition or filter.
   - When you need to ensure that only one matching document is deleted, even if multiple documents in the collection satisfy the filter condition. The method will delete the first matching document found.

2. `delete_many()`:

- Use: The `delete_many()` method is used to delete multiple documents that match the specified filter criteria from the collection.
- Syntax: `collection.delete_many(<filter>)`
- `<filter>`: Specifies the criteria for selecting the documents to delete. It is a dictionary representing the query filters.

Use Cases:
   - When you want to remove multiple documents that meet a specific condition or filter.
   - When you need to delete all documents that match the given filter condition.

3. `drop()`:

- Use: The `drop()` method is used to remove an entire collection from the database, effectively deleting all the documents within that collection.
- Syntax: `collection.drop()`

Use Cases:
   - When you want to completely remove an entire collection from the database, including all its documents.
   - When you need to reset or clean up the collection entirely and do not need the data anymore.
   - Note: The `drop()` operation is irreversible, and the collection cannot be recovered once it is dropped.

Example Scenarios:

1. Suppose you have a "users" collection, and a user requests to delete their account from your application. You can use `delete_one()` to remove their user document from the collection based on their unique user ID.

2. In an e-commerce application, you decide to delete all orders older than a certain date. You can use `delete_many()` with a filter to remove all the outdated order documents.

3. At the end of a project or when you need to reset a database for testing, you might use `drop()` to completely remove a collection that is no longer needed.

Remember to use these methods with caution, especially `drop()`, as it permanently removes data from the collection or the entire collection itself. Always double-check your filter criteria to ensure you're targeting the right documents for deletion.'''