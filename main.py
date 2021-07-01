"""Updates data, starts the web server, and starts the scheduler."""

from apscheduler.schedulers.background import BackgroundScheduler
import bottle
from datetime import datetime, timedelta

import communities, schools, daily_cases, daily_status, episode_date, reported_date
data_to_update = [communities, schools, daily_cases, daily_status, episode_date, reported_date]

def update_data():
    """Updates the data in the JSON files."""

    print("Updating data...\n")

    for data in data_to_update:
        print(f"Updating {data.__name__}")
        data.update()
    
    print("Data successfully updated!")

if __name__ == "__main__":
    # start scheduler to update data every 24 hours
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(update_data, trigger="interval", days=1, start_date=datetime.now() + timedelta(seconds=1))
    sched.start()

    # start web server
    bottle.run()