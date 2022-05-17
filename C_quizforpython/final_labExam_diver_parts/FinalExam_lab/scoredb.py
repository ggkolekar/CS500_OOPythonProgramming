import csv
from tempfile import NamedTemporaryFile
import shutil
from pathlib import Path
from Diver import Diver
import os,sys
from typing import List

class CustomerRepository:
   def __init__(self):
      self.__FILENAME = "customers.csv"

   def getdivers(self):
      divers = {}
      with open(self.__FILENAME, 'r') as file:
         reader = csv.reader(file)
         #skip header and process next row
         header = next(reader)
         for row in reader:
            # convert row to customer object
            if(len(row) == 4):
               diver = Customer(row[0], row[1], row[2], float(row[3]))
               divers[row[0]] = diver
         file.close()

      return divers

   def getdiverList(self):
      divers = []
      with open(self.__FILENAME, newline = "") as file:
         reader = csv.reader(file)
         # skip header and process next row
         header = next(reader)
         for row in reader:
            # convert row to customer object
            if(len(row) == 4):
               diver = Diver(int(row[0]), row[1], row[2], float(row[3]))
               divers.append(diver)

         file.close()

      return divers

   def addnewCustomer(self, diver:Diver):
      with open(self.__FILENAME, 'a',newline = '\n') as file:
         write = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         write.writerow([diver.name, diver.difficulty, diver.score1,diver.score2,diver.score3,diver.score4,diver.score5,diver.score6,diver.score7,diver.score8,diver.score9])