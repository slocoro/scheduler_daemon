"""
Example of what a scheduler Daemon does (e.g. like the one in Dagster). For learning purposes.
"""

import schedule
import time
import threading
import os

def print_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"Task executed at: {current_time}")

def print_hello():
    print(f"Hello!")

def setup_schedules():
    # Schedule the task to run every minute
    schedule.every(1).minutes.do(print_time)
    
    # Schedule another the task to run every two minutes
    schedule.every(2).minutes.do(print_hello)

    # Keep running the schedule continuously
    while True:
        # Runs any pending scheduled tasks
        schedule.run_pending()
        time.sleep(2)  # Sleep for 2 seconds before checking again

def run_scheduler_as_daemon():
    scheduler_thread = threading.Thread(target=setup_schedules)
    # Make it a daemon so it exits when the main program does
    scheduler_thread.daemon = True
    # Start the thread
    scheduler_thread.start()

def main():
    print("Starting the scheduling daemon...")    
    # Start the scheduler as a daemon thread
    run_scheduler_as_daemon()
    
    # Main program continues while scheduler runs in the background
    while True:
        time.sleep(10)  # Keep the main program running
        print("Main program is doing other work...")
    
if __name__ == "__main__":
    main()
