# 📊 Log File Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Simple%20Tool-orange)

 **Python command-line tool** that analyzes log files and counts the number of **INFO**, **WARNING**, and **ERROR** messages.

This project demonstrates basic Python skills such as:

- 📂 File handling
- 🖥 Command-line arguments
- 📊 Log analysis

---

# 🚀 Features

- Analyze any text-based log file
- Count occurrences of:
  - INFO
  - WARNING
  - ERROR
- Lightweight and easy to use
- No external libraries required

---

# 📁 Project Structure

```
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

- Python 3

Check Python version:

```
python --version
```

or

```
python3 --version
```

---

# 📥 Installation

Clone the repository:

```
git clone https://github.com/wahjx/log-file-analyzer.git
```

Go to the project folder:

```
cd log-file-analyzer
```

---

# ▶️ Usage

Run the program with a log file:

```
python analyzer.py sample.log
```

or

```
python3 analyzer.py sample.log
```

---

# 🧾 Example Log File

Example `sample.log`:

```
INFO Server started
INFO User logged in
WARNING Disk usage high
ERROR Database connection failed
INFO Request completed
ERROR Timeout occurred
```

---

# 📊 Example Output

```
Log Analysis Results
--------------------
Errors: 2
Warnings: 1
Info: 3
```

---

# 🧠 How It Works

The program reads the log file line by line and checks for keywords:

- INFO
- WARNING
- ERROR

It then counts how many times each log level appears.

---

# 🔧 Future Improvements

Possible improvements:

- Support more log levels (DEBUG, CRITICAL)
- Export results to a file
- Visualize log statistics
- Build a simple web interface

---

# 👨‍💻 Author

**Wahj Alzaabe**

🎓 Computer Networks and Communications Graduate  
💻 Interested in networking, system analysis, and software development.

GitHub:  
https://github.com/wahjx

