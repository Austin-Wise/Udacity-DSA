"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def unique_directory(transaction_log: list) -> set:
    """
    Compiles set of  unique phone numbers from transaction log.
    :param transaction_log: input transaction log
    :return: set of unique phone numbers
    """
    num_set = set()
    for record in transaction_log:
        # 'sender' phone number
        num_set.add(record[0])
        # 'receiver' phone number
        num_set.add(record[1])
    return num_set


def max_dur(transaction_log: list, u_dir: set) -> None:
    """
    Find max duration by phone number, print message with result to console:
    "<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016."
    :param transaction_log: input transaction log
    :param u_dir: set of unique phone numbers
    :return:
    """
    # convert set to dict to hold total duration, default all to 0
    u_dir: dict = dict.fromkeys(u_dir, 0)

    # initialize phone number and max duration to first record
    phone_number: str = calls[0][0]
    max_duration: int = int(calls[0][3])

    for record in transaction_log:
        # sum duration for sender and receiver
        u_dir[record[0]] += int(record[3])
        u_dir[record[1]] += int(record[3])

        # check previous max vs updated sender and receiver totals
        if u_dir[record[0]] >= max_duration and u_dir[record[0]] > u_dir[record[1]]:
            phone_number = record[0]
            max_duration = u_dir[phone_number]
        if u_dir[record[1]] >= max_duration and u_dir[record[1]] > u_dir[record[0]]:
            phone_number = record[1]
            max_duration = u_dir[phone_number]
    print(f"{phone_number} spent the longest time, {max_duration} seconds, on the phone during September 2016.")
    return None


max_dur(calls, unique_directory(calls))
