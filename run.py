import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    while True:
        data_str = input("Please enter the following numbers: \n years of experience, development languages, foreign languages: \n ")
        applicants_data = data_str.split(",")
        if validate_data(applicants_data):
            print("Data is valid")
            break    
    return name, applicants_data

def validate_data(values):
    """
    Inside the try, converts all string values into intergers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly values.
    """
    try:
        if len(values) != 3:
            raise ValueError("Exactly 3 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data:{e}, please try again.\n")
        return False
    return True


def update_worksheet(value1, value2, value3, value4):
    """
    Update hiring worksheet.
    """
    value2 = int(value2)
    value3 = int(value3)
    value4 = int(value4)
    print("Updating worksheet...\n")
    applicants_worksheet = SHEET.worksheet("applicants")
    applicants_worksheet.append_row([value1, value2, value3, value4])
    print("Applicants worksheet updated successfully.\n")

def main():
    """
    Run all program functions
    """
    data = get_applicants_data() 
    name = data[0]
    numbers = data[1]
    update_worksheet(name, numbers[0], numbers[1], numbers[2])

print("welcome to Hiring Talent Pool Data Automation")
main()

