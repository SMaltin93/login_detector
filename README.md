

# Login Detector

## Features

- Captures a photo using the device's camera.
- Sends the captured photo along with a timestamp to a specified email address.
- Provides a modular design, separating camera functionality and email sending.

## How It Works

1. **Photo Capture**:
   - The script initializes the camera using OpenCV.
   - Captures a screenshot and saves it as `Screenshot_0.png`.

2. **Email Sending**:
   - Reads the captured photo and attaches it to an email.
   - Sends the email with the photo and a timestamp to a predefined recipient.

## File Overview

### `open_cam.py`

This script:
- Initializes the camera to capture a photo.
- Saves the captured photo as `Screenshot_0.png`. 
- Invokes the `send_email` function from `send_email.py` to send the photo.

Key Functions:
- **Camera Initialization**: Captures and saves the screenshot.
- **Integration**: Reads the photo and sends it via email.

### `send_email.py`

This script:
- Reads the captured photo.
- Composes an email with the photo and a timestamp.
- Sends the email to the recipient using Gmail's SMTP server.

Key Functions:
- **read_photo()**: Reads the saved screenshot.
- **send_email(img)**: Composes and sends an email with the screenshot attached.

## Prerequisites

- Python 3.x installed on your system.
- The following Python libraries:
  - `cv2` (OpenCV)
  - `smtplib`
  - `email`
  - `datetime`

## Setup and Configuration

1. Clone this repository:
   ```bash
   git clone https://github.com/SMaltin93/login_detector.git
   ```

2. Navigate to the directory:
   ```bash
   cd login_detector
   ```

3. Install required dependencies (if not already installed):
   ```bash
   pip install opencv-python
   ```

4. Update the email configuration in `send_email.py`:
   - Replace `sen_email` with your sender email address.
   - Replace `rec_email` with the recipient email address.
   - Replace `password` with your email server password or app-specific password.

   **Note**: For Gmail accounts, enable "Allow less secure apps" or create an app password for enhanced security.

## Usage

1. Run the `open_cam.py` script:
   ```bash
   python open_cam.py
   ```

2. The script will:
   - Capture a photo using the camera.
   - Save the photo as `Screenshot_0.png`.
   - Send the photo to the specified email address.

## Example Output

- If the photo is successfully captured and sent:
  ```
  Email sent successfully with the captured photo.
  ```

- If the photo cannot be captured:
  ```
  Failed to grab frame
  ```

- If the email fails to send: 
  ```
  Error: <specific error message>
  ```

## Automating with Windows Task Scheduler

1. Open Task Scheduler (`Win + R`, then type `taskschd.msc`).
2. Create a new task and configure:
   - **General Tab**: Set the task name (e.g., `Login Detector`) and select "Run with highest privileges."
   - **Triggers Tab**: Set the trigger (e.g., at startup or on a schedule).
   - **Actions Tab**: Choose "Start a Program" and configure:
     - Program/script: `python`
     - Add arguments: Path to `open_cam.py` (e.g., `C:\path\to\open_cam.py`).

3. Save and test the task by running it.
