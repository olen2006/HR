#handling export to json and csv including stdout and wring to the file
import csv,json

def to_json_file(export_file,users):
    #https://docs.python.org/3.7/library/json.html?highlight=json#json.dump
    #https://www.datacamp.com/community/tutorials/json-data-python
    #indent=4 to make it readable
    json.dump(users, export_file, indent=4)
    export_file.close()

def to_csv_file(export_file, users):
    #write header line for the file first
    export_file.write('name,id,home,shell\n')
    #now utilize csv package
    writer = csv.writer(export_file)
    #list comprehansion
    #https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
    #https://medium.com/better-programming/list-comprehension-in-python-8895a785550b
    #https://docs.python.org/3/tutorial/datastructures.html
    rows = [[user['name'], user['id'], user['home'], user['shell']] for user in users]
    writer.writerows(rows)
    export_file.close()



