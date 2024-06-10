from pytube import YouTube

def download_video(url, path):
    try:
        yt = YouTube(url)
        ys = yt.streams.get_highest_resolution()
        
        print(f"Video Title: {yt.title}")
        print(f"Stream Details: {ys}")
        
        print(f"Downloading: {yt.title}")
        ys.download(path)
        print("Download completed!")
        
        file_path = f"{path}/{yt.title}.mp4"
        print(f"File saved at: {file_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    path = input("Enter the download path (or leave empty for current directory): ")
    if not path:
        path = "."

    download_video(url, path)
