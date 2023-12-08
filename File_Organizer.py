import os
from pathlib import Path
 
downloads_path = str(Path.home() / 'Downloads')
downloaded_images_path = downloads_path + '\\Images'
downloaded_pdf_path = downloads_path + '\\Docs'
downloaded_exe_path = downloads_path + '\\Executables'

Path(downloaded_images_path).mkdir(parents=True, exist_ok=True)
Path(downloaded_pdf_path).mkdir(parents=True, exist_ok=True)
Path(downloaded_exe_path).mkdir(parents=True, exist_ok=True)

for f in os.listdir(downloads_path):
    if f.lower().endswith(('.pdf', '.txt')):
        os.rename((downloads_path + '\\' + f), (downloaded_pdf_path + '\\' + f))
    elif f.lower().endswith(('.png', '.jpg', '.jpeg')):
        os.rename((downloads_path + '\\' + f), (downloaded_images_path + '\\' + f))
    elif f.lower().endswith(('.exe')):
        os.rename((downloads_path + '\\' + f), (downloaded_exe_path + '\\' + f))