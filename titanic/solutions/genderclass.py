import csv as csv
import numpy as np

# Open up the csv file in to a Python object
test_file=open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()  # The next() command just skips the

fare_ceiling=40
