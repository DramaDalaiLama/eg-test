import schedule
import time
import upload

def action():
    upload.main()

# schedule.every(1).minutes.do(action)
schedule.every().day.at("21:05").do(action)

upload.write_log("Starting scheduled run...\n")

while True:
    schedule.run_pending()
    time.sleep(1)
