import datetime
import re

time_now = datetime.datetime.strptime('28/Jul/1995:13:32:25','%d/%b/%Y:%H:%M:%S') # Using this for sampling purposes, uncomment line bellow for real application
# time_now = datetime.datetime.now()  # .__format__("%d/%b/%Y:%H:%M:%S")

# Determine which log file to look through based on current time
filename = time_now.__format__("%Y_%m_%d_%H") + ".log"

with open (filename, "r") as logfile: # TODO apply per-block based file reading instead of uploading entire file to memory
    data = logfile.readlines()

data.reverse()

last_messages = []
regex =  re.compile('(?P<Sender>[\w\..]+) - - (?P<Time>\[(.*?)\]) (?P<Request>\"(.*?)\") (?P<Response_Code>\w+) (?P<Response_Size>\w+)')
# print data[0]
for line in data:
    # print line
    try:
        entry =  re.match(regex, line).groupdict()
        time_format_re = '[\w\/]+[\w:]+'
        # print re.search(time_format_re,entry['Time']).group()
        entry_time =  datetime.datetime.strptime(re.search(time_format_re,entry['Time']).group(), '%d/%b/%Y:%H:%M:%S') # Convert string with entry time to datetime object
        if (time_now - entry_time).total_seconds() < 10*60*60: # Check if delta is less than 10 minutes or 10*60*60 seconds
            # print line
            last_messages.append(entry)
        else:
            break
    except:
        pass

# print last_messages

for entry in last_messages:
    if entry['Response_Code'] == "500":
        print entry['Sender'] + " "  + entry['Request']
