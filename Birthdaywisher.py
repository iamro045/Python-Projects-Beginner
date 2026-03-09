import pandas as pd
import datetime as dt
import smtplib

# 1. Setup - Update these with your info
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

# 2. Read the CSV
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# 3. Check if today is a birthday
if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]
    
    # 4. Send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # Secure the connection
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person.email,
            msg=f"Subject: Happy Birthday!\n\nHappy Birthday {person['name']}! Have a great day!"
        )
    print(f"Birthday email sent to {person['name']}!")
  
