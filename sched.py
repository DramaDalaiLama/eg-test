import schedule
import time
import upload

def action():
    upload.main()

schedule.every(1).minutes.do(action)

# Log to file
# logfile = open("schedule.log", "w")
# logfile.write("Starting scheduled run...\n")
# logfile.close()
upload.write_log("Starting scheduled run...\n")

while True:
    schedule.run_pending()
    time.sleep(1)
