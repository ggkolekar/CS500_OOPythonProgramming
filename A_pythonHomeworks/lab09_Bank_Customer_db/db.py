import csv
from tempfile import NamedTemporaryFile
import shutil
from pathlib import Path
from Customer import Customer
import os,sys
from typing import List

class CustomerRepository:
   def __init__(self):
      self.__FILENAME = "customers.csv"

   def getcustomers(self):
      customers = {}
      with open(self.__FILENAME, 'r') as file:
         reader = csv.reader(file)
         #skip header and process next row
         header = next(reader)
         for row in reader:
            # convert row to customer object
            if(len(row) == 4):
               customer = Customer(row[0], row[1], row[2], float(row[3]))
               customers[row[0]] = customer
         file.close()

      return customers

   def getcustomerList(self):
      customers = []
      with open(self.__FILENAME, newline = "") as file:
         reader = csv.reader(file)
         # skip header and process next row
         header = next(reader)
         for row in reader:
            # convert row to customer object
            if(len(row) == 4):
               customer = Customer(int(row[0]), row[1], row[2], float(row[3]))
               customers.append(customer)

         file.close()

      return customers

   def addnewCustomer(self, customer:Customer):
      with open(self.__FILENAME, 'a',newline = '\n') as file:
         write = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         write.writerow([customer.accountNo,customer.Fname, customer.Lname, customer.balance])

   def updateCustomer(self,customer:Customer):
      tempfile = NamedTemporaryFile(mode='w', delete=False,newline='')
      fields = ['AccountNo','Fname','Lname','Balance']
      with open(self.__FILENAME, 'r') as csvfile, tempfile:
         reader = csv.DictReader(csvfile, fieldnames=fields)
         writer = csv.DictWriter(tempfile, fieldnames=fields)
         for row in reader:
            if(row['AccountNo'] == str(customer.accountNo)):
               row['Fname'], row['Lname'],row['Balance']  = customer.Fname, customer.Lname, customer.balance
            row = {'AccountNo': row['AccountNo'], 'Fname': row['Fname'], 'Lname': row['Lname'], 'Balance': row['Balance']}
            writer.writerow(row)

      shutil.move(tempfile.name, self.__FILENAME)    #temp file is saved as original filename

   def removeCustomer(self,customer:Customer):
      tempfile = NamedTemporaryFile(mode='w', delete=False,newline='')
      fields = ['AccountNo','Fname','Lname','Balance']
      with open(self.__FILENAME, 'r') as csvfile, tempfile:
         reader = csv.DictReader(csvfile, fieldnames=fields)
         writer = csv.DictWriter(tempfile, fieldnames=fields)
         for row in reader:
            if(row['AccountNo'] != str(customer.accountNo)):
               row = {'AccountNo': row['AccountNo'], 'Fname': row['Fname'], 'Lname': row['Lname'], 'Balance': row['Balance']}
               writer.writerow(row)

      shutil.move(tempfile.name, self.__FILENAME)    #temp file is saved as original filename


def main():
   #customers={}
   """
   custRepo = CustomerRepository()
   customers = custRepo.getcustomers()
   for key,value in customers.items():
      print ("key,value",key,value.Fname)

   for key in customers.keys():
      print ("key",key)

   for key in customers.values():
      print ("key",key.Fname)

   cust1 = Customer(1234, 'Peter', 'Pan', 10000)
   custRepo.addnewCustomer(cust1)

   cust2 = Customer(5678, 'Swati', 'Train', 20000)
   custRepo.addnewCustomer(cust2)

   cust3 = Customer(1234, 'Peter', 'Pan', 17000)
   custRepo.updateCustomer(cust3)

   """


main()