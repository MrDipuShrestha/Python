import pandas
from datetime import datetime
import random
import smtplib

my_email = "dipstha393@gmail.com"
password = "hkct tuav brka zmzv"

date = datetime.now()
today_tuple = (date.month, date.day)

data = pandas.read_csv("birthdays.csv")
data_dictonary = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in data_dictonary:
    birthday_person = data_dictonary[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_person["email"],
                                msg=f"Subject: Happy Birthday!!!\n\n{contents}"
                                )
