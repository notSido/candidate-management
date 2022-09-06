import json
import csv
import os
from os import path
import pandas as pd
from csv import DictReader 

def convert():
  df = pd.read_json (r'maze_2.json')
  df.to_csv (r'maze.csv', index = None)
  print('Successfully created a CSV File')


def remove_csv():
    #check if file exists and delete it if it does
    #this is just to clean up the process
  filename = 'maze.csv'
  if path.isfile(filename) is True:
    os.remove(filename)
    print('Successfully removed CSV file')
  else:
    raise Exception('File not found')
    

def add_candidate(): 
  filename = 'maze_2.json'
  listObj = []
  
  # Check if file exists
  if path.isfile(filename) is False:
    raise Exception("File not found")
  
  # Read JSON file
  with open(filename) as fp:
    listObj = json.load(fp)
  
  # Verify existing list
  print(listObj)

  print(type(listObj))
  
  listObj.append({
    "name": "John Doe",
    "birthday": "28.08.1998",
    "height": 165,
    "weight": 56.1,
    "car": True,
    "languages": ["C#", "C++", "C"]
  })
  
  # Verify updated list
  print(listObj)
  
  with open(filename, 'w') as json_file:
      json.dump(listObj, json_file, 
                          indent=4,  
                          separators=(',',': '))
  
  print('Successfully appended to the JSON file')

def add_line_csv():
  data=['Joe Mama','28.08.1998','165','56.1',True,"['C#', 'C++', 'C']"]
  with open(r'maze.csv', 'a') as f:
      writer = csv.writer(f)
      writer.writerow(data)

def retrieve_candidate():
  candidate_name = input("Enter the Candidate's Name: ")
  filename = 'maze.csv'
  
  with open(filename, 'r') as fileObject:
    reader_obj = csv.reader(fileObject)
    for row in reader_obj:
      if row[0] == candidate_name:
        print('Name: ' + row[0] + '\nDate of Birth: ' + row[1] + '\nHeight (cm): ' + row[2] + '\nWeight (kg): ' + row[3] + '\nCar?: ' + row[4] + '\nLanguages: ' + row[5])
def menu():
  print('1: Convert JSON File to CSV File \n2: Delete existing CSV file \n3: Add a new Candidate to JSON File \n4: Add a new Candidate to CSV File \n5: Retrieve Information about a Candidate')
  selection = int(input('Select your desired Operation: '))

  if selection == 1:
    convert()
  elif selection == 2:
    remove_csv()
  elif selection == 3:
    add_candidate()
  elif selection == 4:
    add_line_csv()
  elif selection == 5:
    retrieve_candidate()
  else:
    raise Exception('Invalid Input')

menu()
