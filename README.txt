# 📚 Phodu Club PDF Downloader

Automates bulk downloading of revision PDFs from Phodu Club using Selenium by mimicking real user interaction.

---

## 🚀 Features

* ✅ Automatically downloads all PDFs (Physics, Chemistry, Maths)
* ✅ Works with protected/signed URLs
* ✅ Bypasses manual download process
* ✅ Uses real browser session (no API hacks)
* ✅ Saves files locally for offline access

---

## ⚙️ Requirements

* Python **3.10+**
* Google Chrome (latest version)
* ChromeDriver (matching your Chrome version)

---

## 🛠️ Setup Instructions

### 1. Install Python

Check if Python is installed:

```bash
python --version
```

---

### 2. Install dependencies

```bash
pip install selenium
```

---

### 3. Download ChromeDriver

1. Check your Chrome version:

   * Open Chrome → `chrome://settings/help`

2. Download matching ChromeDriver:
   👉 https://googlechromelabs.github.io/chrome-for-testing/

3. Extract the zip file

4. Place `chromedriver.exe` in the same folder as your script

---

### 4. Project Structure

```
project-folder/
│── script.py
│── chromedriver.exe
```

---

## ▶️ How to Run

```bash
python script.py
```

---

## ⚠️ Important Notes

* You must **log in manually on the Phodu website** when the browser opens
* Wait a few seconds before interacting (to avoid bot detection)
* After logging in, **do not touch the browser** — the script will continue automatically

---

## 📂 Output

All downloaded PDFs will be saved in:

```
phodu_downloads/
```

---

## ❗ Common Issues

### 1. Module not found error

```bash
pip install selenium
```

---

### 2. ChromeDriver mismatch

Ensure:

```
Chrome version == ChromeDriver version
```

---

### 3. PDFs opening but not downloading

Make sure this is set in the script:

```python
"plugins.always_open_pdf_externally": True
```

---

### 4. Cloudflare / bot detection

* Wait before logging in
* Interact like a normal user
* Avoid rapid clicking

---

## 🧠 How It Works

* Uses Selenium to control a real browser
* Logs in via user interaction
* Extracts signed PDF URLs from the page
* Forces Chrome to download files automatically

---

## 📌 Disclaimer

This project is for **educational purposes only**.
Respect the website’s terms of service when using this script.

---

## ⭐ Future Improvements

* [ ] Auto file naming (chapter-wise)
* [ ] Separate folders by subject
* [ ] Faster downloads
* [ ] Headless mode support

---

## 🙌 Author

Built by Divyansh

---

## ⭐ If this helped you, consider starring the repo!
