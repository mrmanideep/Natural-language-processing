import re

def find_email_addresses(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def find_phone_numbers(text):
    pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(pattern, text)

def find_dates(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    return re.findall(pattern, text)

# Sample text for testing
test_text = """
Contact us at support@example.com or sales@shop.com.
Call us at 123-456-7890 or 987.654.3210.
Our meeting is scheduled for 12/25/2023.
"""

# Finding patterns
emails = find_email_addresses(test_text)
phones = find_phone_numbers(test_text)
dates = find_dates(test_text)

# Display results
print("Emails:", emails)
print("Phone Numbers:", phones)
print("Dates:", dates)

