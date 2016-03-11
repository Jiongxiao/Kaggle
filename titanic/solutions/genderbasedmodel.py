import csv as csv
import numpy as np

# Open up the csv file in to a Python object
test_file=open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()  # The next() command just skips the

prediction_file=open('genderbasedddmodel.csv','wb')
predictions_file_object=csv.writer(prediction_file)
predictions_file_object.writerow(['PassengerId','Survived'])
for row in test_file_object:
    print row
    if row[3]=='female':
        predictions_file_object.writerow([row[0],'1'])
    else:
        predictions_file_object.writerow([row[0],'0'])
test_file.close()
prediction_file.close()
