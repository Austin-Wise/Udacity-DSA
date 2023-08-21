"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def unique_directory(input_set: set, transaction_log: list) -> set:
    """
    Compiles set of  unique phone numbers from transaction log.
    :param input_set: input set of unique phone numbers
    :param transaction_log: input transaction log
    :return: set of unique phone numbers
    """
    for record in transaction_log:
        # 'sender' phone number
        input_set.add(record[0])
        # 'receiver' phone number
        input_set.add(record[1])
    return input_set


num_set = unique_directory(unique_directory(set(), calls), texts)

print(f'There are {len(num_set)} different telephone numbers in the records.')
