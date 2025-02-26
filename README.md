# 🚀 YouTubeDownloader

A **futuristic, multi-threaded YouTube downloader** built with `yt-dlp` and `customtkinter`.  
Supports **video & audio downloads**, real-time **progress tracking**, and a **modern UI**.

---

## 📌 Table of Contents
- [✨ Features](#features)
- [📦 Installation](#installation)
  - [1️⃣ Install Python & Dependencies](#install-python-dependencies)
  - [2️⃣ Install FFmpeg (Required)](#install-ffmpeg-required)
- [🚀 Usage](#usage)
- [🛠️ Troubleshooting](#troubleshooting)
- [⚙️ Tech Stack](#tech-stack)
- [🤝 Contributing (Optional)](#contributing-optional)
- [📜 License (Optional)](#license-optional)
---

## 🌟 Features

✅ **Download YouTube videos & audio (MP4/MP3)**  
✅ **Futuristic UI** using `customtkinter`  
✅ **Real-time progress bar** (fixes freezing issues)  
✅ **Multi-threading** for a smooth experience  
✅ **Choose custom download location**  
✅ **FFmpeg integration for merging video/audio**  

---

## 📦 Installation

### **1️⃣ Install Python & Dependencies**
Ensure you have **Python 3.7+** installed. Then, install the required dependencies:

```bash
pip install yt-dlp customtkinter
```
### **2️⃣ Install FFmpeg (Required)**
FFmpeg is needed to merge video & audio. Install it:

#### **Windows:**
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/)  
2. Extract it to `C:\ffmpeg`  
3. Add `C:\ffmpeg\bin` to the system **PATH**  

#### **Linux/macOS:**
Run the following commands:

```bash
# Ubuntu/Debian
sudo apt install ffmpeg  

# macOS (Homebrew)
brew install ffmpeg  
```

## 🚀 Usage

1.  Run the script:

    ```bash
    python youtube_gui.py
    ```

2.  Enter the YouTube URL in the input box.

3.  Select the desired format (Video or Audio).

4.  Choose the save location using the "Choose Save Location" button.

5.  Click "Download 🚀" and monitor the real-time progress.

(Optional: Add screenshots or GIFs here)

---

## 🛠️ Troubleshooting

- ❌ **Progress Bar Stuck at 0%?**
  - ✔️ Ensure FFmpeg is installed correctly and added to your system's PATH.

- ❌ **Download Errors?**
  - ✔️ Update `yt-dlp`:

    ```
    pip install -U yt-dlp
    ```
  - ✔️ Verify the YouTube URL is correct.
  - ✔️ Check your internet connection.

- ❌ **UI Freezing?**
  - ✔️ The app uses multi-threading. Ensure you're running it with Python 3.7+.
  - ✔️ Close other resource-intensive applications.

---

## ⚙️ Tech Stack

- 🟢 Python 3.7+
- 🟢 `yt-dlp` (YouTube downloading backend)
- 🟢 `customtkinter` (Modern UI)
- 🟢 FFmpeg (Video/audio merging)

---

## 🤝 Contributing (Optional)

If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.




