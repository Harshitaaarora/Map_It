

# 🗺️ Map_IT

**Map_IT** is a smart automation tool for quickly opening Google Maps with your desired location. No more manually opening the browser, typing the address, and pressing enter. With Map_IT, just run a script and your destination is loaded instantly—either by copying it to the clipboard or by passing it via the command line.

---

## 🚀 Features

- 🔍 Opens Google Maps instantly with the address you provide.
- 📋 Reads the address from clipboard (if no arguments are passed).
- 🧭 Two implementations:
  - `mapit_webbrowser.py`: Simple and fast using `webbrowser` and `pyperclip`.
  - `mapit_selenium.py`: Simulates real typing using a browser automation tool (Selenium).

---

## 📁 Project Structure

```

Map\_IT/
├── mapit\_webbrowser.py    # Implementation using webbrowser & pyperclip
├── mapit\_selenium.py      # Implementation using Selenium
├── requirements.txt       # Dependencies (for Selenium version)
└── README.md              # This documentation

````

---

## 💻 Installation

### ✅ For `mapit_webbrowser.py`

Install `pyperclip` (if not already installed):

```bash
pip install pyperclip
````

### ✅ For `mapit_selenium.py`

Install Selenium and make sure you have the appropriate Chrome WebDriver installed.

```bash
pip install selenium
```

Download the [ChromeDriver](https://sites.google.com/chromium.org/driver/) matching your Chrome version and ensure it's in your system PATH.

---

## ⚙️ Usage

### 📌 Option 1: Using Clipboard (Only `mapit_webbrowser.py`)

1. Copy any address (e.g., 1600 Amphitheatre Parkway Mountain View CA)
2. Run:

```bash
python mapit_webbrowser.py
```

This opens the address directly in your default browser via Google Maps.

---

### 📌 Option 2: Using Command Line Argument (Both scripts)

```bash
python mapit_webbrowser.py Statue of Liberty NY
```

or

```bash
python mapit_selenium.py Eiffel Tower Paris
```

This opens Google Maps with the specified destination.

---

## ⚙️ How They Work

### `mapit_webbrowser.py`:

* Uses `sys.argv` to check for CLI input.
* If not present, falls back to clipboard using `pyperclip`.
* Opens the map in your default web browser via `webbrowser.open()`.

### `mapit_selenium.py`:

* Uses Selenium to launch Chrome.
* Opens Google Maps.
* Locates the search input and simulates typing the destination.
* Hits "Enter" to search automatically.

---

## 🧪 Example

```bash
python mapit_webbrowser.py "India Gate"
```

Or copy "India Gate" to clipboard and run:

```bash
python mapit_webbrowser.py
```

For Selenium:

```bash
python mapit_selenium.py "India Gate"
```

---

## 🧑‍💻 Author

**Harshita Arora**
[GitHub](https://github.com/Harshitaaarora) • [LinkedIn](https://www.linkedin.com/in/harshita-arora-991138227/)

---



## 🤝 Contributions

Feel free to fork the repository and submit a pull request to improve Map\_IT. Suggestions and feature requests are welcome!

---
