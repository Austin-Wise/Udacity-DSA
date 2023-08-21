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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def unique_directory(transaction_log: list, column: int, input_set: set = None, ) -> set:
    """
    Compiles set of  unique phone numbers from transaction log.
    :param transaction_log: input transaction log
    :param column: column to filter by
    :param input_set: Starter set to add to
    :return: set of unique phone numbers
    """
    if input_set is None:
        input_set = set()
    for record in transaction_log:
        input_set.add(record[column])
    return input_set


def potential_telemarketers(calls, texts):
    calls_receiving = unique_directory(calls, 1)
    texts_outgoing = unique_directory(texts, 0, calls_receiving)
    texts_receiving = unique_directory(texts, 1, texts_outgoing)

    calls_outgoing = unique_directory(calls, 0)

    potential_list = [i for i in calls_outgoing if i not in texts_receiving]
    return sorted(potential_list)


def print_4(refined_transaction_log):
    print("These numbers could be telemarketers: ")
    for i in refined_transaction_log:
        print(i)


print_4(potential_telemarketers(calls, texts))
