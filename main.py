"""Updates data, starts the web server, and starts the scheduler."""

from apscheduler.schedulers.background import BackgroundScheduler
import bottle
from datetime import datetime, timedelta

import communities, schools, daily_cases, daily_status

def update_data():
    """Updates the data in the JSON files."""

    print("Updating data...")

    communities.update()
    schools.update()
    daily_cases.update()
    daily_status.update()
    
    print("Data successfully updated!")

if __name__ == "__main__":
    # start scheduler to update data every 24 hours
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(update_data, trigger="interval", days=1, start_date=datetime.now() + timedelta(seconds=1))
    sched.start()

    # start web server
    bottle.run(host="0.0.0.0", ports=1234)