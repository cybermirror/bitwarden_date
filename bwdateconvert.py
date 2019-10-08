# -*- coding: utf-8 -*-

import re
import datetime


def seconds_to_strdate(matched):
    # Convert a date number in seconds from the timestamp(0), ie 1970-01-01
    # a str in format yyyy-mm-dd
    seconds_from_epoch = int(matched.group('seconds'))
    if seconds_from_epoch > 0:
        date_convert = datetime.date.fromtimestamp(seconds_from_epoch)
    else:
        # fromtimestamp() method can handle +ve number only
        # For -ve numbers, need another way to handle
        epoch_shift = datetime.date.fromtimestamp(0).toordinal()
        date_convert = datetime.date.fromordinal(
            seconds_from_epoch // 86400 + epoch_shift)
    return matched.group('match_prefix') + date_convert.isoformat() + \
        matched.group('match_suffix')


inputfilename = 'bwtest.json'
outputfilename = 'bwtest_converted.json'

with open(inputfilename, 'rt', encoding='utf-8') as inputfile:
    full_content = inputfile.read()

repattern = r'(?P<match_prefix>"name": "(.*[dD]ate.*|.*日期.*|[bB]irthday)'
repattern += r'",\s+"value": ")(?P<seconds>-?\d{5,})'
repattern += r'(?P<match_suffix>",)'
repattern1 = r'"name": ".*[dD]ate.*|[bB]irthday",\s+"value": ".+",'

converted_content = re.sub(repattern, seconds_to_strdate, full_content)
with open(outputfilename, 'wb') as outputfile:
    outputfile.write(bytes(converted_content, encoding='utf-8'))
