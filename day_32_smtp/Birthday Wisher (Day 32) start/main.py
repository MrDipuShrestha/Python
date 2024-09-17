# # email send demo
# import smtplib
#
# my_email = "dipstha393@gmail.com"
# password = "hkct tuav brka zmzv"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="dummy95@yahoo.com",
#         msg="Subject: First mail\n\n This is the first mail that i sent you."
#     )


# working with datetime module

import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 5:
    with open("quotes.txt") as quote:
        all_quotes = quote.readlines()
        random_quote = random.choice(all_quotes)

    my_email = "dipstha393@gmail.com"
    password = "hkct tuav brka zmzv"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="dummy95@yahoo.com",
                            msg=f"Subject: Today's quote\n\n {random_quote}"
                            )
