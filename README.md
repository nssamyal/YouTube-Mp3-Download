# YouTube-Mp3-Download

# YouTube to MP3 Downloader with Cover Art 🎵

This Python script lets you automatically download songs from YouTube as high-quality MP3 files, along with embedded cover art.

---

# Features
- Download songs from a simple `songs.txt` list
- Converts YouTube audio to `.mp3`
- Automatically embeds YouTube thumbnail as album art (if available)
- Skips creating folders manually (creates `downloads/` directory automatically)

---

#Requirements
- Python 3.7+
- [ffmpeg](https://ffmpeg.org/download.html) (must be in your system PATH)
- pip packages: `yt-dlp`, `requests`

Install dependencies:
```bash
pip install yt-dlp requests
```

---

#Project Structure
```
Youtube_AudioDownloader/
│
├── main.py              # Main script
├── songs.txt            # Put song titles here, one per line
├── downloads/           # Output folder for mp3 files
└── README.md            # You're reading this
```

---

#Usage

1. **Make sure `ffmpeg` is installed** and added to PATH:
   ```bash
   ffmpeg -version
   ```

2. **Create `songs.txt`** in the same folder as `main.py`:
   ```
   Let Me Love You
   Peaches Justin Bieber
   Shape of You
   ```

3. **Run the script**:
   ```bash
   python main.py
   ```

---

#Disclaimer
This project is for **educational purposes only**. Download content responsibly and in accordance with YouTube’s Terms of Service.

---

#credits
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)
- YouTube Search & Thumbnails

Enjoy your music! 🎧
