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

for file_path in Path.iterdir(downloads_path):
    file_format = file_path.suffix.lower()
    file = file_path.stem + file_format
    if file_format in FILE_FORMATS:
        new_file_path = downloads_path / FILE_FORMATS[file_format] 
        new_file_path.mkdir(exist_ok=True)
        file_path.rename(new_file_path / file)