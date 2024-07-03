import re
from collections import Counter
from pathlib import Path


def parse_log_line(line: str, count: int) -> dict:
    pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (INFO|DEBUG|ERROR|WARNING) .+"
    if not re.match(pattern=pattern, string=line):
        print(f"Invalid log-line format: line #{count}")

    date, time, level, *message = line.split()
    message = " ".join(message)
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message,
    }


def load_logs(file_path: str) -> list | None:
    logs = []

    file = Path(file_path)
    if not file.exists():
        print("File does not exist. Check the path please")
        return

    with open(file_path, "r", encoding="UTF-8") as file:
        for line in file:
            count = 1
            parsed_line = parse_log_line(line=line, count=count)
            if parsed_line:
                logs.append(parsed_line)
            count += 1

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = []
    for log in logs:
        if log["level"] == level:
            filtered_logs.append(log)
    return filtered_logs


def count_logs_by_level(logs: list) -> dict:
    return Counter([log["level"] for log in logs])


def display_log_counts(counts: dict):
    pass


if __name__ == '__main__':
    logs_list = load_logs("logs.txt")
    print(count_logs_by_level(logs_list))
