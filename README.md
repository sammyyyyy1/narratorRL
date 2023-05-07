<div align="center">

  # narratorRL
  Image to text to speech app with LLM and AI enhanced features.

  ![](https://img.shields.io/github/license/sammyyyyy1/narratorRL)
  ![](https://img.shields.io/github/contributors/sammyyyyy1/narratorRL)
  ![](https://img.shields.io/github/last-commit/sammyyyyy1/narratorRL)

  ![](https://img.shields.io/badge/made%20for-MetHacks%202023-%239152a3?style=for-the-badge)
  ![](https://img.shields.io/badge/sleep%20lost%20collectively-16h-yellow?style=for-the-badge)

</div>

---

# Table of Contents

- [Table of Contents](#table-of-contents)
- [About](#about)
- [Installation/Usage](#installationusage)
  - [Chrome Extension](#chrome-extension)
  - [Backend Server](#backend-server)

# About

We are a group of 4 University of Waterloo Math and CS students. This project was made for the MetHacks 2023 hackathon. narratorRL targets the challenges issued by the following companies: Cohere, Domain.com, and Microsoft Cloud.

The backend of the server projects uses Python's Django framework to serve a RESTful API. The frontend is a React Native application with JavaScript.

# Installation/Usage

**Note: to install and use narratorRL, you must set up BOTH the React Native app and the Django server.**

## Django Server

1. Clone this repository and optionally create a virtual environment
2. Install the dependencies with `pip install -r requirements.txt`
3. Add a file named `env.py` in the `server` directory
   1. Generate a Django secret key (see command below) and set it to `DJANGO_SECRET_KEY`
   2. Add a Cohere secret key to `COHERE_SECRET_KEY`
4. [Install Tesseract OCR](https://github.com/tesseract-ocr/tesseract#installing-tesseract) (for all users by default, or you'll need to change the command path variable)
5. Add your device's IPv4 address to `ALLOWED_HOSTS` in `server/settings.py`
6. Start the server with `python manage.py runserver 0.0.0.0:8000`

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## Backend Server

1. Enter the `mobile` directory
2. Install the dependices with `npm install`
3. Add your device's IPv4 address to the `fetch` command in `mobile/Home.js`
3. Start Expo with `npx expo start`
4. Connect however you wish
