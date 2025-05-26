
````markdown
# 🗺️ Map_IT

Map_IT is a lightweight automation tool that streamlines the process of searching for locations on Google Maps. Instead of manually opening Google Maps and typing a destination, Map_IT allows users to search for locations by either:

- Copying an address to the system clipboard
- Passing the destination as a command-line argument

With Map_IT, navigation becomes quicker, cleaner, and more efficient — perfect for power users or those who just want to save time.

---

## 🚀 Features

- 🔍 Automatically opens Google Maps with the provided destination
- 📋 Detects location from clipboard if no arguments are passed
- 🧠 Smart fallback mechanism for improved usability
- 🖥️ Simple command-line interface (CLI)
- 🐍 Built with Python for maximum compatibility

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Map_IT.git
cd Map_IT
````

2. Install the required packages:

```bash
pip install -r requirements.txt
```

> Dependencies may include:
>
> * `pyperclip`
> * `webbrowser`
> * `sys`

---

## 💡 Usage

You can use Map\_IT in two ways:

### Option 1: Using the Clipboard

Just copy any address to your clipboard and run:

```bash
python map_it.py
```

### Option 2: Using Command-Line Arguments

Provide the address as a command-line argument:

```bash
python map_it.py 1600 Amphitheatre Parkway Mountain View CA
```

---

## 🧠 How It Works

* If a destination is passed as an argument, it takes priority.
* If no arguments are passed, Map\_IT will attempt to read from the system clipboard.
* It then automatically opens the default web browser and navigates to Google Maps with the search results for the given location.

---

## 📂 File Structure

```
Map_IT/
├── map_it.py           # Main script
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

---

## 📌 Example

```bash
$ python map_it.py Statue of Liberty New York
```

✅ Opens your default browser and navigates to:
[https://www.google.com/maps/place/Statue+of+Liberty,+New+York](https://www.google.com/maps/place/Statue+of+Liberty,+New+York)

---

## 🧑‍💻 Author

**Harshita Arora**
[GitHub](https://github.com/Harshitaaarora) | [LinkedIn]([https://linkedin.com/in/your-link](https://www.linkedin.com/in/harshita-arora-991138227/))


---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

