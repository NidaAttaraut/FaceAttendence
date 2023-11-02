# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:09:41 2023

@author: 
"""

import datetime,gspread,random
from oauth2client.service_account import ServiceAccountCredentials
from gspread.exceptions import SpreadsheetNotFound
import emailing as em 
import os

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

#creds = ServiceAccountCredentials.from_json_keyfile_name("/content/drive/MyDrive/Colab Notebooks/Face-recognition-based-attendance-system-master/face recognition source code/credentials.json", scope)
creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/Abbasali/OneDrive/Desktop/Face-recognition-based-attendance-system-master/face recognition source code/credentials.json"
, scope)

#"C:\Users\Abbasali\OneDrive\Desktop\Face-recognition-based-attendance-system-master\face recognition source code\credentials.json"
client = gspread.authorize(creds)

sheet = client.open("spreadsheet1").sheet1
"""import gspread
from oauth2client.service_account import ServiceAccountCredentials


try:
    # Open the spreadsheet by its ID
    spreadsheet = gc.open_by_key('1LlS-CiQTKhTf-jSEavnMLtP8ARIoKkh7wg7tthbRXHs')
    sheet = spreadsheet.get_worksheet(0)  # Access a specific worksheet
except gspread.exceptions.SpreadsheetNotFound:
    print("The specified spreadsheet was not found.")"""

# Open the spreadsheet using the ID
'''spreadsheet = client.open_by_key('1kjvvnx6zpYpOu6-d56Rc98RB1Sh_QRhsnYirNAyf7O8')

# Use the spreadsheet as needed
sheet = spreadsheet.sheet1

# Print the names of all the sheets in the spreadsheet
print("Sheet names: %s" % [sheet.title for sheet in spreadsheet.worksheets()])'''


'''try:
    spreadsheet = client.open('Face Recognition').sheet1
except SpreadsheetNotFound:
    print("Spreadsheet not found or you do not have permission to access it.")'''


max_intime='16:00:00'

def enroll_person_to_sheet(name,email):
    nrows = len(sheet.col_values(1))
    pin=random.randint(999,9999)
    sheet.update_cell(nrows+1,1,name)
    sheet.update_cell(nrows+1,2,email)
    sheet.update_cell(nrows+1,3,pin)
    em.email_pin(email,pin)
    
    
def mark_all_absent():
    now=datetime.datetime.now()
    date=now.strftime('%m/%d/%Y').replace('/0','/')
    if(date[0]=='0'):
        date=date[1:]
    datecell=sheet.find(date)
    nrows = len(sheet.col_values(1))
    for row in range(2,nrows+1):
        sheet.update_cell(row,datecell.col,'absent') 
        
        
        
def write_to_sheet(name):
  now=datetime.datetime.now()
  date=now.strftime('%m/%d/%Y').replace('/0','/')
  if(date[0]=='0'):
            date=date[1:]
  time=now.strftime('%H:%M:%S')
  namecell=sheet.find(name)
  datecell=sheet.find(date)

  if(sheet.cell(namecell.row,datecell.col).value =='absent' ):
    if(time<max_intime):
      sheet.update_cell(namecell.row,datecell.col,'present') 
      print('recorded')
      em.send_email(sheet.cell(namecell.row,2).value,"present")
         
    else:
      # sheet.update_cell(namecell.row,datecell.col,'late')
      print('late')
      em.send_email(sheet.cell(namecell.row,2).value,"absent")
  # else:
  #   print('already recorded')
