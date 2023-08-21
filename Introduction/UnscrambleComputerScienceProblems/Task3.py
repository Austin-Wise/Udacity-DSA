"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangladesh.
Fixed line numbers include parentheses, so Bangladesh numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangladesh. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangladesh have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangladesh are made
to fixed lines also in Bangladesh? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangladesh are calls
to other fixed lines in Bangladesh."
The percentage should have 2 decimal digits
"""


def filter_fixed(phone_number: str, area_code: str) -> bool:
    """
    Checks if fixed line number is from bngl
    :param phone_number: Fixed-line number
    :param area_code: area code for fixed number
    :return:
    """
    # is Fixed Line
    if phone_number[4] == ')':
        if phone_number[1:4] == area_code:
            return True
    return False


def bngl_outgoing(transaction_log: list):
    recipients = set()
    for record in transaction_log:
        if filter_fixed(record[0], '080'):
            recipient = record[1]
            if ')' in recipient:
                recipient = recipient.split(')')[0] + ")"
            else:
                recipient = recipient.split(' ')[0]
            recipients.add(recipient)
    return sorted(recipients)


def print_a(numbers_list):  # O(n)
    print("The numbers called by people in Bangladesh have codes:")
    for number in numbers_list:
        print(number)


print_a(bngl_outgoing(calls))


def pct_fixed_bngl(transaction_log):
    count = 0
    for i in transaction_log:
        if filter_fixed(i[0], '080'):
            count += 1
    return round(count / len(transaction_log) * 100, 2)


def print_b(bngl_call_pct):
    print(f"{bngl_call_pct} percent of calls from fixed lines in Bangladesh "
          f"are calls to other fixed lines in Bangladesh.")


print_b(pct_fixed_bngl(transaction_log=calls))
