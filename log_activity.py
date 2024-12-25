import os

# Проверка текущей рабочей директории
print(f"Current working directory: {os.getcwd()}")

import os
import datetime

# Устанавливаем рабочую директорию
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Логирование активности
log_file = "activity_log.txt"
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(log_file, "a") as log:
    log.write(f"Activity logged at: {today}\n")

print("Activity logged successfully!")
