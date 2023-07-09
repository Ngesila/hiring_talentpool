import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hiring_talentpool')

#applicants = SHEET.worksheet('applicants')

#data = applicants.get_all_values()

#print(data)

def get_applicants_data():
    """
    Get applicants information from the user
    """
    print("Please enter applicants information from user")
    print("Name should be two names")
    print("Example: James Peter")
    print("years of experience should be interger")
    print("Example: 5")
    print("Development languages should be interger")
    print("Example: 4")
    print("Foreign languages should be interger")
    print("Example: 3")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

get_applicants_data()


