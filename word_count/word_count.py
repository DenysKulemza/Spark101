"""
PySpark Word Count Example
A simple introduction to PySpark for counting words in a text file
"""

from pyspark.sql import SparkSession

# Step 1: Create a Spark Session
# This is the entry point for any PySpark application
spark = SparkSession.builder \
    .appName("Word Count Example") \
    .master("local[*]") \
    .getOrCreate()

# Step 2: Read the text file
# Create an RDD (Resilient Distributed Dataset) from the text file
text_rdd = spark.sparkContext.textFile("sample_text.txt")

print("=== Original Text ===")
for line in text_rdd.collect():
    print(line)

# Step 3: Transform the data
# Split each line into words, flatten the list, and convert to lowercase
words_rdd = text_rdd.flatMap(lambda line: line.lower().split())

print("\n=== All Words ===")
print(words_rdd.collect())

# Step 4: Map each word to a (word, 1) pair
word_pairs_rdd = words_rdd.map(lambda word: (word, 1))

print("\n=== Word Pairs ===")
print(word_pairs_rdd.collect())

# Step 5: Reduce by key to count occurrences of each word
word_count_rdd = word_pairs_rdd.reduceByKey(lambda a, b: a + b)

# Step 6: Sort by count in descending order
sorted_word_count = word_count_rdd.sortBy(lambda x: x[1], ascending=False)

# Step 7: Display the results
print("\n=== Word Count Results ===")
print(f"{'Word':<20} {'Count':<10}")
print("-" * 30)
for word, count in sorted_word_count.collect():
    print(f"{word:<20} {count:<10}")

# Step 8: Save the results (optional)
sorted_word_count.saveAsTextFile("word_count_output")

# Stop the Spark session
spark.stop()
