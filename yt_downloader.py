import yt_dlp
import os
import re
import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Set up futuristic theme
ctk.set_appearance_mode("dark")  # Modes: "dark", "light"
ctk.set_default_color_theme("blue")  # Other themes: "green", "dark-blue"

class YouTubeDownloader(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🚀 YouTube Downloader 🚀")
        self.geometry("600x450")
        self.resizable(False, False)

        # UI Elements
        self.label = ctk.CTkLabel(self, text="Enter YouTube URL:", font=("Orbitron", 16))
        self.label.pack(pady=10)

        self.url_entry = ctk.CTkEntry(self, width=500, font=("Consolas", 14))
        self.url_entry.pack(pady=5)

        # Format Selection (Video or Audio)
        self.format_var = ctk.StringVar(value="Video")
        self.video_button = ctk.CTkRadioButton(self, text="Video", variable=self.format_var, value="Video", font=("Orbitron", 14))
        self.audio_button = ctk.CTkRadioButton(self, text="Audio", variable=self.format_var, value="Audio", font=("Orbitron", 14))
        self.video_button.pack()
        self.audio_button.pack()

        # Progress Bar
        self.progress_bar = ctk.CTkProgressBar(self, width=500)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

        # Buttons
        self.select_folder_btn = ctk.CTkButton(self, text="Choose Save Location", command=self.select_folder)
        self.select_folder_btn.pack(pady=5)

        self.download_btn = ctk.CTkButton(self, text="Download 🚀", command=self.start_download_thread)
        self.download_btn.pack(pady=10)

        self.output_folder = ""

    def select_folder(self):
        """Allows the user to select a save folder."""
        self.output_folder = filedialog.askdirectory(title="Select Download Folder")
        if self.output_folder:
            messagebox.showinfo("Folder Selected", f"Downloads will be saved in: {self.output_folder}")

    def clean_ansi(self, text):
        """Removes ANSI escape sequences to prevent float conversion errors."""
        return re.sub(r'\x1b\[[0-9;]*m', '', text)

    def progress_hook(self, d):
        """Handles download progress updates."""
        if d['status'] == 'downloading':
            try:
                clean_percent = self.clean_ansi(d['_percent_str']).strip('%')
                percent = float(clean_percent) / 100
                self.progress_bar.set(percent)
                self.update_idletasks()  # Forces UI update
            except ValueError:
                print(f"Error parsing progress: {d['_percent_str']}")  # Debugging info
        elif d['status'] == 'finished':
            self.progress_bar.set(1)
            messagebox.showinfo("Download Complete", "Your download has finished successfully!")

    def start_download(self):
        """Starts the YouTube video/audio download process."""
        url = self.url_entry.get()
        format_type = self.format_var.get()

        if not url:
            messagebox.showerror("Error", "Please enter a valid YouTube URL!")
            return
        if not self.output_folder:
            messagebox.showerror("Error", "Please select a save location!")
            return

        options = {
            'outtmpl': os.path.join(self.output_folder, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best' if format_type == "Audio" else 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp3' if format_type == "Audio" else 'mp4',
            'progress_hooks': [self.progress_hook],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }] if format_type == "Audio" else []
        }

        # Start Download (Runs on a separate thread)
        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([url])
        except Exception as e:
            messagebox.showerror("Download Error", f"An error occurred: {e}")

    def start_download_thread(self):
        """Runs the download process in a separate thread to prevent UI freezing."""
        threading.Thread(target=self.start_download, daemon=True).start()

# Run the App
if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()
