from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age_in_days = (today - birthdate).days
    years = age_in_days // 365
    months = (age_in_days % 365) // 30
    days = (age_in_days % 365) % 30
    return years, months, days

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
years, months, days = calculate_age(birthdate)
print(f"Your age is {years} years, {months} months, and {days} days.")

def days_until_birthday(birthdate):
    today = datetime.today()
    next_birthday = datetime(today.year, birthdate.month, birthdate.day)
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)
    return (next_birthday - today).days

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
days_left = days_until_birthday(birthdate)
print(f"There are {days_left} days until your next birthday.")

from datetime import timedelta

def schedule_meeting(current_datetime, duration):
    return current_datetime + timedelta(hours=duration[0], minutes=duration[1])

current_datetime_str = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%d %H:%M")
duration_str = input("Enter the meeting duration in hours and minutes (H M): ")
duration = tuple(map(int, duration_str.split()))
end_time = schedule_meeting(current_datetime, duration)
print(f"The meeting will end at {end_time.strftime('%Y-%m-%d %H:%M')}.")

from datetime import datetime
import pytz

def convert_timezone(date_time_str, from_tz, to_tz):
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
    date_time = from_zone.localize(date_time)
    return date_time.astimezone(to_zone)

date_time_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
from_tz = input("Enter your current timezone (e.g., 'US/Eastern'): ")
to_tz = input("Enter the target timezone (e.g., 'Europe/Paris'): ")
converted_time = convert_timezone(date_time_str, from_tz, to_tz)
print(f"The time in {to_tz} is {converted_time.strftime('%Y-%m-%d %H:%M')}.")

import time
from datetime import datetime

def countdown_timer(target_time):
    while datetime.now() < target_time:
        remaining_time = target_time - datetime.now()
        print(f"Time remaining: {remaining_time}", end="\r")
        time.sleep(1)

target_time_str = input("Enter the future date and time (YYYY-MM-DD HH:MM): ")
target_time = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M")
countdown_timer(target_time)

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

email = input("Enter an email address: ")
if validate_email(email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")

def format_phone_number(phone_number):
    return f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"

phone_number = input("Enter a 10-digit phone number: ")
formatted_number = format_phone_number(phone_number)
print(f"Formatted phone number: {formatted_number}")

import re

def check_password_strength(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True

password = input("Enter your password: ")
if check_password_strength(password):
    print("Your password is strong.")
else:
    print("Your password is weak. It must have at least 8 characters, one uppercase letter, one lowercase letter, and one digit.")

def find_word_occurrences(text, word):
    occurrences = [i for i in range(len(text)) if text.startswith(word, i)]
    return occurrences

text = input("Enter a text: ")
word = input("Enter a word to find: ")
occurrences = find_word_occurrences(text, word)
print(f"Word '{word}' found at positions: {occurrences}")

import re

def extract_dates(text):
    pattern = r"\b\d{4}-\d{2}-\d{2}\b"
    return re.findall(pattern, text)

text = input("Enter some text: ")
dates = extract_dates(text)
print(f"Extracted dates: {dates}")
