from datetime import datetime, date

def happy_birthday(name, birthday_date):
    return f"Hello {name}! Today {birthday_date.strftime('%B %d')} is your birthday! 🎉 Happy Birthday!"

# Get current date
today = date.today()

name = input("What is your name?: ")
birth_month = int(input("What month were you born (1-12)?: "))
birth_day = int(input("What day were you born (1-31)?: "))

# Validate inputs
if birth_month < 1 or birth_month > 12:
    print("Please enter a valid month between 1 and 12")
elif birth_day < 1 or birth_day > 31:
    print("Please enter a valid day between 1 and 31")
else:
    # Build this year's birthday
    try:
        birthday_this_year = date(today.year, birth_month, birth_day)
    except ValueError:
        print("Invalid date entered.")
        exit()

    if birthday_this_year == today:
        print(happy_birthday(name, today))
    elif birthday_this_year > today:
        days_until = (birthday_this_year - today).days
        print(f"Hi {name}! Your birthday is on {birthday_this_year.strftime('%B %d, %Y')}. That's in {days_until} days!")
    else:
        # Birthday already passed this year, calculate for next year
        birthday_next_year = date(today.year + 1, birth_month, birth_day)
        days_until = (birthday_next_year - today).days
        print(f"Hi {name}! Your next birthday is on {birthday_next_year.strftime('%B %d, %Y')}. That's in {days_until} days!")
