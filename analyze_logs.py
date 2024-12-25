import datetime

log_file = "activity_log.txt"
today = datetime.datetime.now()

try:
    with open(log_file, "r") as log:
        lines = log.readlines()
        recent_logs = 0
        for line in lines:
            timestamp = line.split("at: ")[1].strip()
            log_date = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            if (today - log_date).days < 7:
                recent_logs += 1

        print(f"Total activity logs: {len(lines)}")
        print(f"Activity logs in the last 7 days: {recent_logs}")
except FileNotFoundError:
    print("Log file not found. Please run log_activity.py first.")
