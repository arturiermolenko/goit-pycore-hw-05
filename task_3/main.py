import re
import sys

from collections import Counter
from pathlib import Path


def validate(args: list) -> str | None:
    """Validate arguments."""
    file_path = args[0]
    file = Path(file_path)
    validation_dict = {
        """Not enough arguments.
        Please, provide command in format:
        python3 main.py <path_to_logs> <log_level>(optional)
        """: not args,
        "Too many arguments. Try one more time, please": len(args) > 2,
        "Log level is incorrect. "
        "Should be one of INFO, DEBUG, ERROR, WARNING":
            len(args) == 2 and args[1].lower() not in ["info", "debug", "error", "warning"],
        "File does not exist. Check the path please": not file.exists(),
        "File type not supported. Please use .log or .txt": file.suffix not in [".log", ".txt"],
    }
    for message, condition in validation_dict.items():
        if condition:
            return message


def parse_log_line(line: str, count: int) -> dict | None:
    """Parse a log line and return a dictionary"""
    pattern = re.compile(
        r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (INFO|DEBUG|ERROR|WARNING) .+",
        re.IGNORECASE
    )
    if not re.match(pattern=pattern, string=line):
        print(f"Invalid log-line format: line #{count}. Line is cut off the results")
        return

    date, time, level, *message = line.split()
    level = level.lower()
    message = " ".join(message)
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message,
    }


def load_logs(file_path: str) -> list | None:
    """Load logs from a file."""
    with open(file_path, "r", encoding="UTF-8") as file:
        logs = list(
            map(
                lambda i_line: parse_log_line(line=i_line[1], count=i_line[0] + 1),
                enumerate(file.readlines())
            )
        )

    logs = list(filter(None, logs))

    return logs


def filter_logs_by_level(logs: list, level: str) -> None:
    """Filter logs by level."""
    filtered_logs = []
    for log in logs:
        if log["level"] == level.lower():
            filtered_logs.append(log)
    if filtered_logs:
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
    else:
        print(f"No logs found for level {level}")


def count_logs_by_level(logs: list) -> dict:
    """Count logs by level."""
    return Counter([log["level"] for log in logs])


def display_log_counts(counts: dict) -> None:
    """Display log counts in table."""
    print(
        f"""
        Log level        | Quantity
        -----------------|----------
        INFO             | {counts["info"]}
        DEBUG            | {counts["debug"]}
        ERROR            | {counts["error"]}
        WARNING          | {counts["warning"]}
        """
    )


def main():
    args = sys.argv[1:]

    validator = validate(args=args)
    if validator:
        print(validator)
        return

    path = args[0]
    logs = load_logs(file_path=path)
    counts = count_logs_by_level(logs=logs)
    display_log_counts(counts=counts)

    if len(args) == 2:
        level = args[1]
        return filter_logs_by_level(logs=logs, level=level)


if __name__ == "__main__":
    main()
