import os
import time

import pandas as pd
import self as self
import win32com.client as client
from datetime import datetime
from os import scandir
import dateutil.utils


def email():
    me = 'Firstname.Lastname@address.com'
    you = 'Firstname.Lastname@address.com'
    cc = 'Firstname.Lastname@address.com'
    outlook = client.Dispatch('Outlook.Application')
    message = outlook.CreateItem(0)  # 0 is the code for a mail item (see the enumerations)
    message.Display()

    message.To = you
    message.SentOnBehalfOfName = me
    message.CC = cc
    # message.BCC = 'richard.ayoade@email.com'

    message.Subject = 'ATB Availability'
    message.Body = 'Cerner ATB is not present.'

    # message.Save() # save to drafts folder
    message.Send()  # send to outbox


def email_Available():
    me = 'Firstname.Lastname@address.com'
    you = 'Firstname.Lastname@address.com'
    cc = 'Firstname.Lastname@address.com'
    outlook = client.Dispatch('Outlook.Application')
    message = outlook.CreateItem(0)  # 0 is the code for a mail item (see the enumerations)
    message.Display()

    message.To = you
    message.SentOnBehalfOfName = me
    message.CC = cc
    # message.BCC = 'richard.ayoade@email.com'

    message.Subject = 'ATB Availability'
    message.Body = 'Cerner ATB is present.'

    # message.Save() # save to drafts folder
    message.Send()  # send to outbox

Dict = {1: '01-Jan', 2: '02-Feb', 3: '03-Mar',
4: '04-Apr', 5: '05-May', 6: '06-Jun',
7: '07-Jul', 8: '08-Aug', 9: '09-Sep',
        10: '10-Oct', 11: '11-Nov', 12: '12-Dec'}


cwd = os.getcwd()
print(cwd)
path_root = "S:\\Shared With Me\\Analytics\\BI-FairfieldMedicalPRC\\AR\\ATB\\2022\\"
path_end = input("ex 05-May: ")
Directory = os.chdir(path_root + path_end)
cwd = os.getcwd()
print(cwd)

for file in os.listdir(cwd):
    if file.__contains__("FHP_Cerner_ATB"):
        # Get file's Last modification time stamp only in terms of seconds since epoch
        modTimesinceEpoc = os.path.getmtime(file)
        # Convert seconds since epoch to readable timestamp
        modificationTime = time.strftime('%Y-%m-%d', time.localtime(modTimesinceEpoc))
        ModDate = print(modificationTime)
        today = dateutil.utils.today()
        runTime = today.strftime('%Y-%m-%d')
        print(runTime)

while runTime == modificationTime:
    email_Available()
else:
    email()
