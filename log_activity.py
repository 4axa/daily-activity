import os
import datetime
import subprocess

# Устанавливаем рабочую директорию
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Логирование активности
log_file = "activity_log.txt"
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    with open(log_file, "a") as log:
        log.write(f"Activity logged at: {today}\n")
    print("Activity logged successfully!")
except Exception as e:
    print(f"Error writing to log file: {e}")

# Добавление изменений в Git
try:
    subprocess.run(["git", "add", log_file], check=True)
    subprocess.run(["git", "commit", "-m", f"Daily log update for {today}"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Changes committed and pushed to GitHub.")
except subprocess.CalledProcessError as e:
    print(f"Error with Git operations: {e}")
