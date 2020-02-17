import sys
import csv
import random

# Notes: generate csv's for testing data pipelines
script_name = sys.argv[0] # script name.
print(f'Running: {script_name}') 

print('''Note: This generates two files. 1st file will contain a list of records. 
	The second file will contain a number of records with the 1st column as the key.
	File names are random alpha_numeric strings with *_test appended.
	''')

# Arguement parsing.
try:
	num_records = int(sys.argv[1])
	print(f'\tNum records: {num_records}') # number of records.

	fields_per_record = int(sys.argv[2])
	print(f'\tFields per record: {fields_per_record}') # fields per record.

	len_each_field = int(sys.argv[3])
	print(f'\tLength of each field: {len_each_field}') # length of each record field.

	key_dupes = int(sys.argv[4])
	print(f'\tDuplicates of 1st column record key: {key_dupes}') # number of deliberate dupes for a first column value. (for testing joins.)
except:
	print(f'Error. Usage arguements: # rec, # fields in col, # len field, # count of 1st col key')

# generate alpha-numeric strings
def alpha_num_string_generator(length):
	return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUV') for i in range(int(length)))

# file names
file_1_name = str(num_records) + '_x_' + str(num_records * key_dupes) + '_records_' + 'file_1_test.csv'
file_2_name = str(num_records) + '_x_' + str(num_records * key_dupes) + '_records_' + 'file_2_test.csv'

with open(file_1_name, 'w', newline='') as file_1:
	with open(file_2_name, 'w', newline='') as file_2:
		file_1_field_names = []
		file_2_field_names = []


		for x in range(0, fields_per_record):
			field_name = 'field_' + str(x)
			file_1_field_names.append(field_name)
			file_2_field_names.append(field_name)

		file_1_writer = csv.DictWriter(file_1, fieldnames=file_1_field_names)
		file_2_writer = csv.DictWriter(file_2, fieldnames=file_2_field_names)

		file_1_writer.writeheader()
		file_2_writer.writeheader()

		record1 = {}
		record2 = {}

		for x in range(num_records):
			for idx, field in enumerate(file_1_field_names):
				value1 = alpha_num_string_generator(len_each_field)
				
				record1[field] = value1

				if(idx == 0):
					for w in range(key_dupes):
						for idx2, field2 in enumerate(file_2_field_names):
							if(idx2 == 0): 
								record2[field2] = value1
							else:
								record2[field2] = alpha_num_string_generator(len_each_field)
						file_2_writer.writerow(record2)
			file_1_writer.writerow(record1)


print('File generation complete. . . ')
