# login_detector

The `login_detector` repository provides a Python-based tool to monitor and detect login events on a system. This tool can be used for logging, auditing, or detecting unauthorized access attempts.

## Features

- Monitors login events on a system.
- Tracks user logins and timestamps.
- Provides a basis for extending functionality, such as alerting on suspicious logins.

## Prerequisites

- Python 3.x installed on your system.
- Basic understanding of Python and system monitoring.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/SMaltin93/login_detector.git
   ```

2. Navigate to the directory:
   ```bash
   cd login_detector
   ```

3. Install required dependencies (if any). Check for a `requirements.txt` file and install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script manually using Python:
```bash
python login_detector.py
```

This will start monitoring and logging login events.

## Automating with Windows Task Scheduler

You can set up the `login_detector` script to run automatically on a schedule using Windows Task Scheduler.

### Steps to Schedule the Script:

1. **Open Task Scheduler**:
   - Press `Win + R` to open the Run dialog.
   - Type `taskschd.msc` and press Enter.

2. **Create a New Task**:
   - In the Task Scheduler window, click `Create Task` on the right-hand panel.

3. **General Tab**:
   - Provide a name for the task, such as `Login Detector`.
   - Select `Run whether user is logged on or not`.
   - Check `Run with highest privileges`.

4. **Triggers Tab**:
   - Click `New` to create a new trigger.
   - Select the schedule (e.g., daily, weekly, or at system startup).
   - Configure the time or event condition based on your preference and click `OK`.

5. **Actions Tab**:
   - Click `New` to create a new action.
   - Select `Start a Program`.
   - In the `Program/script` field, enter the path to your Python executable (e.g., `C:\Python39\python.exe`).
   - In the `Add arguments` field, enter the path to the `login_detector.py` script. For example:
     ```
     C:\path\to\login_detector\login_detector.py
     ```
6. **Conditions Tab**:
   - Adjust the conditions as needed (e.g., ensure the task runs even on battery power).

7. **Settings Tab**:
   - Check `Allow task to be run on demand`.
   - Ensure `If the task fails, restart every` is checked (optional for reliability).

8. **Save the Task**:
   - Click `OK` to save the task.
   - You may be prompted to enter your user credentials for authentication.

### Verify the Task:

- Open Task Scheduler and find your task in the library.
- Right-click the task and select `Run` to test it.
- Check the script's output (e.g., log files) to confirm it is running successfully.


## Author

Developed by [SMaltin93](https://github.com/SMaltin93).
```
