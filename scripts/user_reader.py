from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime, sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logs/user_reader.log", "a")
   
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        pass    

sys.stdout = Logger()

# This script receives command-line arguments from gui.py to define the .xml file and tags to be queried
# CLI argument: python3 scripts/user_reader.py /home/$USER/Python/XMLReader/users.xml --tags Last-Modified
argumentsNum = len(sys.argv)
if int(argumentsNum) >= 2:
    print(f'File selected: {sys.argv[1]}')
    argument = sys.argv[3:]
    print(f'Tags received: {argument}')
    filetoread = sys.argv[1]
else:
    print('Not enough information to run!')


# Generate unique datestamp string that can be used as a valid file name when saving the report to a spreadsheet
now = datetime.datetime.now()
filedate = str(now).replace(" ", "_").replace(":", "_").replace("-", "_").replace(".", "_")
spreadsheet = str('IPO_XML_report_')
filename = str(spreadsheet + filedate + '.xlsx') # filename = IPO_XML_report_YYYY_MM_DD_HH_MM_SS.xlsx

content = []

def parse():
    for i in argument:
        userchoice = i
        print(f'userchoice is: {userchoice}')
        if userchoice == 'Tags':
            print('Select at least one tag.')
            sys.exit()
        else:
            custdf = bs_content.find_all(f"{userchoice}")
            ### Search tags ###
            users = bs_content.find_all("FullName")
            extension = bs_content.find_all("Extension")
            sipContact = bs_content.find_all("SIPContact")
            pbxAddr = bs_content.find_all("PBXAddress")
            # Create dataframe
            pd.set_option('display.max_rows', None)
            report = pd.DataFrame(list(zip(users, extension, sipContact, pbxAddr, custdf)),
                               columns=['Full Name', 'Extension', 'SIP Contact', 'PBX Address', userchoice])
            print(report)
            report.to_excel(f'results/{filename}', index=False)
            print(f'---- File {filename} created successfully.')

try:
    with open(filetoread, "r") as file:
        # To collect the .xml file, go to IPO Web Manager @ https://<IPO_IP_ADDR>:7070 --> Call Management --> Users --> Actions --> Export All
        content = file.readlines()
        content = "".join(content)
        bs_content = bs(content, features="xml")
        parse()
except FileNotFoundError:
    print('\nNo valid .xml file found.')
except NameError:
    print('No file to read.')
