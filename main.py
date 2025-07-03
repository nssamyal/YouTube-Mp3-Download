import os
import subprocess
import requests
import yt_dlp

# Set download folder
download_path = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_path, exist_ok=True)

# Read songs list from songs.txt
try:
    with open("songs.txt", "r", encoding="utf-8") as f:
        songs = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("songs.txt not found! Please make sure it's in the same directory.")
    exit()

# Process each song
for song in songs:
    print(f"\nDownloading: {song}")
    webm_path = os.path.join(download_path, f"{song}.webm")
    mp3_path = os.path.join(download_path, f"{song}.mp3")

    # Step 1: Download as .webm
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': webm_path,
        'quiet': True,
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{song}"])
    except Exception as e:
        print(f"Failed to download: {song}\n{e}")
        continue

    # Step 2: Download thumbnail (cover art)
    try:
        info = yt_dlp.YoutubeDL({'quiet': True}).extract_info(f"ytsearch1:{song}", download=False)['entries'][0]
        thumbnail_url = info.get("thumbnail", "")
        cover_path = os.path.join(download_path, "cover.jpg")

        if thumbnail_url:
            img_data = requests.get(thumbnail_url).content
            with open(cover_path, 'wb') as handler:
                handler.write(img_data)
        else:
            cover_path = None
    except Exception:
        cover_path = None

    # Step 3: Convert to mp3 and embed cover if available
    try:
        if cover_path:
            cmd = [
                "ffmpeg", "-y", "-i", webm_path, "-i", cover_path,
                "-map", "0:a", "-map", "1",
                "-c:a", "libmp3lame", "-b:a", "192k",
                "-id3v2_version", "3",
                "-metadata:s:v", "title=Album cover",
                "-metadata:s:v", "comment=Cover (front)",
                mp3_path
            ]
        else:
            cmd = [
                "ffmpeg", "-y", "-i", webm_path,
                "-vn", "-ab", "192k", "-ar", "44100", "-f", "mp3",
                mp3_path
            ]

        subprocess.run(cmd, check=True)
        os.remove(webm_path)
        print(f"Saved: {mp3_path}")
    except Exception as e:
        print(f"Error converting {song}:\n{e}")
