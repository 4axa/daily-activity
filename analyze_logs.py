import datetime
import matplotlib.pyplot as plt

log_file = "activity_log.txt"
dates = []

# Чтение файла логов и извлечение дат
try:
    with open(log_file, "r") as log:
        for line in log:
            # Извлечение времени из лога
            timestamp = line.split("at: ")[1].strip()
            log_date = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").date()
            dates.append(log_date)
except FileNotFoundError:
    print("Log file not found. Please run log_activity.py first.")
    exit()

# Подсчёт количества записей за каждый день
activity_count = {date: dates.count(date) for date in set(dates)}

# Вывод общей информации
today = datetime.datetime.now().date()
recent_logs = sum(1 for date in dates if (today - date).days < 7)

print("Activity Analysis:")
print(f"- Total activity logs: {len(dates)}")
print(f"- Activity logs in the last 7 days: {recent_logs}")
print("\nDaily activity count:")
for date, count in sorted(activity_count.items()):
    print(f"{date}: {count}")

# Построение графика
plt.figure(figsize=(10, 6))
plt.bar(activity_count.keys(), activity_count.values(), color="skyblue")
plt.title("Activity Logs Over Time", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Logs Count", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

# Сохранение графика в файл
output_file = "activity_graph.png"
plt.savefig(output_file)
print(f"Graph saved as {output_file}")

# Отображение графика
plt.show()
