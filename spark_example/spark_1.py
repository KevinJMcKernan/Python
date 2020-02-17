import sys
 
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

if __name__ == "__main__":

	file_1_path = str(sys.argv[1])
	print(f'\tFile 1: {file_1_path}') # number of records.

	file_2_path = str(sys.argv[2])
	print(f'\tFile 2: {file_2_path}') # fields per record.

	spark = SparkSession.builder.config("spark.driver.memory", "4g").appName("Read CSVs").getOrCreate()

	df1 = spark.read.csv(file_1_path, header=True, sep=",").cache()

	df2 = spark.read.csv(file_2_path, header=True, sep=",").cache()

	print(type(df1))

	df1.show()
	df2.show()
	join_df = df1.join(df2, df1.file_1_field_0 == df2.file_2_field_0)

	join_df.show()
	join_df.write.csv('join')

