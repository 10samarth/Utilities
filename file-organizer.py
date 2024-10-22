import os
import shutil

folder_path = '/Users/samarthgoudar/Downloads'

file_types = {
    'Images': ['.jpg', '.png', '.gif', '.jpeg', '.heic', '.webp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.epub', '.doc'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.gz'],
    'Data': ['.csv', '.json'],
    'Diagrams': ['.drawio', '.svg', '.excalidraw']
}

def organize_folder():
    for filename in os.listdir(folder_path):
        file_ext = os.path.splitext(filename)[1].lower()
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                folder_path = os.path.join(folder_path, folder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                shutil.move(os.path.join(folder_path, filename), folder_path)
                print(f'Moved: {filename} -> {folder}')
                break

organize_folder()
