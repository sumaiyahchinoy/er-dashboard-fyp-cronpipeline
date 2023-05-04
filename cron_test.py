import schedule
import time
from IndusDC import clean_data
    
schedule.every(4).minutes.do(clean_data) #change this to 6 hours

while(1):
    schedule.run_pending()
    time.sleep(1)