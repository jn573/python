# trim all fields
#  https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
import csv
import sys

f = open('something_in.csv', 'a', newline='')
fw = csv.writer(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)

with open("something_out.csv") as csvfile:
    filereader = csv.reader(csvfile, quoting=csv.QUOTE_NONE)

    for row in filereader:
        Name = row[0]
        Country = row[1]
        Street = row[2]
        Foo = row[3].strip()

        fw.writerow([Name, Country, Street, Foo])

        # print(TIMESTAMP)

f.close()
