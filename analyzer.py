import sys
import os


def analyze_log(file_path):
    log_counts = {}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(maxsplit=1)
                level = parts[0]

                if level.isupper():
                    log_counts[level] = log_counts.get(level, 0) + 1

        if not log_counts:
            print("No log levels found in the file.")
            return

        print("Log Analysis Results")
        print("--------------------")
        for level, count in sorted(log_counts.items()):
            print(f"{level}: {count}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' was not found.")
    except Exception as error:
        print(f"Unexpected error: {error}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <logfile>")
        return

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' is not a valid file.")
        return

    analyze_log(file_path)


if __name__ == "__main__":
    main()