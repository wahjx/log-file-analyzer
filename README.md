# 📊 Log File Analyzer

![Python](https://img.shields.io/badge/Python-3-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

Python command-line tool that analyzes log files and counts log levels such as:

* DEBUG
* INFO
* WARNING
* ERROR
* CRITICAL
* NOTICE

This project demonstrates basic Python skills such as:

📂 File handling
🖥 Command-line arguments
📊 Log analysis
📁 Data export (JSON / CSV)

---

# 🚀 Features

* Analyze any text-based log file
* Detect common log levels automatically
* Count occurrences of:

DEBUG
INFO
WARNING
ERROR
CRITICAL
NOTICE

* Sort results by name or count
* Export results to JSON
* Export results to CSV
* Lightweight and easy to use
* No external libraries required

---

# 📁 Project Structure

```text
log-file-analyzer
│
├── analyzer.py
├── sample.log
├── README.md
└── requirements.txt
```

---

# ⚙️ Requirements

You only need:

Python 3

Check Python version:

```bash
python --version
```

or

```bash
python3 --version
```

---

# 📥 Installation

Clone the repository:

```bash
git clone https://github.com/wahjx/log-file-analyzer.git
```

Go to the project folder:

```bash
cd log-file-analyzer
```

---

# ▶️ Usage

Run the program with a log file:

```bash
python analyzer.py sample.log
```

or

```bash
python3 analyzer.py sample.log
```

---

# 📂 Analyze Multiple Files

```bash
python analyzer.py sample.log system.log app.log
```

---

# 📊 Sort Results by Count

```bash
python analyzer.py sample.log --sort count --descending
```

---

# 📁 Export Results

Export to JSON:

```bash
python analyzer.py sample.log --json results.json
```

Export to CSV:

```bash
python analyzer.py sample.log --csv results.csv
```

---

# 🧾 Example Log File

Example `sample.log`:

```
INFO Server started
INFO User logged in
WARNING Disk usage high
ERROR Database connection failed
DEBUG Fetching user profile
CRITICAL System overheating
NOTICE Backup completed
```

---

# 📊 Example Output

```
File: sample.log

Log Analysis Results
--------------------
Total lines: 7
Matched log lines: 7

CRITICAL: 1
DEBUG: 1
ERROR: 1
INFO: 2
NOTICE: 1
WARNING: 1
```

---

# 🧠 How It Works

The program reads the log file line by line and detects log levels using pattern matching.

It then counts how many times each log level appears and displays a summary of the results.

---

# 🔧 Future Improvements

Possible improvements:

* Support custom log patterns
* Filter logs by keyword or date
* Visualize log statistics with charts
* Build a simple web interface

---

# 👨‍💻 Author

**Wahj Alzaabe**

🎓 Computer Networks and Communications Graduate
💻 Interested in networking, system analysis, and software development.

GitHub
https://github.com/wahjx
