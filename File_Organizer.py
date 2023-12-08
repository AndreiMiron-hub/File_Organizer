import os
from pathlib import Path
 
 
DIRECTORIES = {
    'HTML': ['.html5', '.html', '.htm', '.xhtml'],
    'IMAGES': ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp', '.png', '.bpg', 'svg',
               '.heif', '.psd'],
    'VIDEOS': ['.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mng',
               '.qt', '.mpg', '.mpeg', '.3gp'],
    'DOCUMENTS': ['.oxps', '.epub', '.pages', '.docx', '.doc', '.fdf', '.ods',
                  '.odt', '.pwi', '.xsn', '.xps', '.dotx', '.docm', '.dox',
                  '.rvg', '.rtf', '.rtfd', '.wpd', '.xls', '.xlsx', '.ppt',
                  'pptx'],
    'ARCHIVES': ['.a', '.ar', '.cpio', '.iso', '.tar', '.gz', '.rz', '.7z',
                 '.dmg', '.rar', '.xar', '.zip'],
    'AUDIO': ['.aac', '.aa', '.aac', '.dvf', '.m4a', '.m4b', '.m4p', '.mp3',
              '.msv', 'ogg', 'oga', '.raw', '.vox', '.wav', '.wma'],
    'PLAINTEXT': ['.txt', '.in', '.out'],
    'PDF': ['.pdf'],
    'PYTHON': ['.py'],
    'XML': ['.xml'],
    'EXE': ['.exe'],
    'SHELL': ['.sh']
}


FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}

downloads_path = Path.home() / 'Downloads'


for file in os.scandir(downloads_path):
    file_path = Path(file)
    file_format = file_path.suffix.lower()
    if file_format in FILE_FORMATS:
        new_file_path = Path(file_path)
        downloads_path.mkdir(exist_ok=True)
        os.rename(file_path, file_path)
 
# downloaded_images_path = downloads_path + '\\Images'
# downloaded_pdf_path = downloads_path + '\\Docs'
# downloaded_exe_path = downloads_path + '\\Executables'

# Path(downloaded_images_path).mkdir(parents=True, exist_ok=True)
# Path(downloaded_pdf_path).mkdir(parents=True, exist_ok=True)
# Path(downloaded_exe_path).mkdir(parents=True, exist_ok=True)


# for f in os.listdir(downloads_path):
#     if f.lower().endswith(('.pdf', '.txt')):
#         os.rename((downloads_path + '\\' + f), (downloaded_pdf_path + '\\' + f))
#     elif f.lower().endswith(('.png', '.jpg', '.jpeg')):
#         os.rename((downloads_path + '\\' + f), (downloaded_images_path + '\\' + f))
#     elif f.lower().endswith(('.exe')):
#         os.rename((downloads_path + '\\' + f), (downloaded_exe_path + '\\' + f))