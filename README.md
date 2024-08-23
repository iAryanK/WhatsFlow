# WhatsFlow

A desktop application that sends bulk messages on whatsapp. WhatsFlow is a highly efficient bulk message sender due to its unique algorithm for sending message. Also, the application has some features that makes it stand out from others.

## Table of Contents

- [Screenshots](#screenshots)
- [Installation](#installation)
- [Version Updates](#versionupdates)

## Screenshots

![screenshot](https://github.com/iAryanK/WhatsFlow/blob/main/screenshots/ui_dark.png?raw=true)  
![screenshot](https://github.com/iAryanK/WhatsFlow/blob/main/screenshots/ui_light.png?raw=true)

### APK Installation

Download the latest software from here.

[Download WhatsFlow v6.6.1](https://drive.google.com/drive/folders/1OHqlcki3WW0e82ftkBU7asfXW4tp69Ag?usp=sharing)
| -------------------------- |

### Manual Installation

1. Clone the WhatsFlow repository to your local machine using the following command:

```
git clone https://github.com/iAryanK/WhatsFlow.git
```

2. Open the project in Visual Studio Code.

3. Pip install the following modules and library:

```
pip install cutomtkinter selenium webdriver-manager get-chrome-driver
```

## version updates

v6.6.1

- minor update due to changes in whatsapp web DOM

v6.6.0 (only for windows 10 and 11)

- Auto installation of compatible chrome webdriver
- As chrome version updates, the driver version will also be updated automatically.

v5.1.1

- bugs fixed
- Codebase algorithm changed, redundant codes removed
- phone numbers can now be added with or without +91
- Login once, load once and keep sending messages without reloading whatsapp anymore.
- success failure status now visible for only text message also.
- complete text message sending assured, no more cut in messages
- no time waste in autotype letter by letter
- spaces between two phone numbers won't cause problem anymore
- No more waste of time to handle invalid numbers in sleep duration.
- handles invalid numbers and non-link numbers and valid numbers as expected.
- login time and other webdriverwait time increased to 5 minutes i.e. 300 seconds

v4.1.0

- No rush for scanning the QR code . You now get enough time to login.

v3.0

- Documents can also be sent besides image/video.
- No copy pasting image/video/document path. Select your file right from the application.
- Success/Failure status also visible in status bar.

v2.0

- Photos/videos both can be sent.
- Numbers not available on whatsapp will be bypassed automatically.
- A simple UI is also designed, so no boring powershell required.
- Text can also be bold or italic or both

v1.0

- Initiated from [this Youtube video](https://youtu.be/hs1VCXBoXbU?si=EoZ4tMI5b_BJedPP)
