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


def get_applicants_data():
    """
    Get applicants information from the user
    """
    while True:
        try:
            name = input("Please enter your name: \n")
            if len(name) < 2:
                raise ValueError("Invalid input. Please enter a name with more than 2 characters.")
        except ValueError as e:
            print(f"Invalid input: {e}, Please enter a name with more than 2 characters.")
            continue
        else:
            break

    data_str = input("Please enter the following numbers: \n years of experience, development languages, foreign languages: \n ")


    applicants_data = data_str.split(",")
    validate_data(applicants_data)

def validate_data(values):
    """
    Inside the try, converts all string values into intergers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly values.
    """
    
    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError("Exactly 3 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data:{e}, please try again.\n")

get_applicants_data()     

    

   
   
    
    
    

   
                










    
    
    
   
    
    
    

    

    
   
