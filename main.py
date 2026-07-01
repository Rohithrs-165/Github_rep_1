from dotenv import load_dotenv
import os

def email_verification():
    try:
        load_dotenv()
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")

        if client_id is None or client_secret is None:
            print("Credentials not found")
            return
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            print("Email verification success")
            print("Email:", email)
        else:
            raise ValueError("Invalid email id")
    except ValueError as e:
        print(e)

    except Exception as e:
        print("Something went wrong:", e)

email_verification()