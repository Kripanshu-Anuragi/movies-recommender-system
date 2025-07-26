import os
import requests

def download(url, dest):
    if not os.path.exists(dest):
        print(f"Downloading: {dest}")
        r = requests.get(url)
        if r.status_code == 200:
            with open(dest, "wb") as f:
                f.write(r.content)
            print("Download complete!")
        else:
            print(f"Failed to download {url} with status code {r.status_code}")
    else:
        print(f"Already exists: {dest}")

download("https://drive.google.com/uc?export=download&id=1jA3CPFagJ44GvmSDcKNIqQ-KEYwnM2Ii", "app/models/similarity.pkl")
download("https://drive.google.com/uc?export=download&id=1ONEDm5kYwXt19WcV9Pp6qrxPw3itdRr7", "app/models/movie_dict.pkl")
