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

# applicants = SHEET.worksheet('applicants')

# data = applicants.get_all_values()

# print(data)


def get_applicants_data():
    """
    Get applicants information from the user
    """
    print("Please enter applicants information from user")
    print("name should be two names")
    print("example: James Peter")
    print("years of experience should be interger")
    print("example: 5")
    print("development languages should be interger")
    print("example: 4")
    print("foreign languages should be interger")
    print("Example: 3\n")

    data_str = input("Enter your data here: ")


    applicants_data = data_str.split(",")
    validate_data(applicants_data)


def validate_data(values):
    """
    Inside the try, converts all string values into intergers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly values.
    """
    try:
        if len(values) != 4:
            raise ValueError(
            f"Exactly 4 values required, you provided {len(values)}"
        )
    except ValueError as e:
        print(f"Invalid data:{e}, please try again.\n")

get_applicants_data()        
                
                
    
    

    

    

    










    
    
    
   
    
    
    

    

    
   
