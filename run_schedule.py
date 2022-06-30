from datetime import datetime
import main

def run(*args):
    today = datetime.today()
    day = today.weekday()
    now = datetime.now()
    current_hour = int(now.strftime("%H%M"))
    
    if day == 0 or 1 or 2 or 3 or 4 and current_hour >= 900 and current_hour <= 1500:
        main()  #This job is run Monday-Friday 9am-3pm.
        print(f'this ran')

run()