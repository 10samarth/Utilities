import os
import shutil

file_types = {
    'Images': ['.jpg', '.png', '.gif', '.jpeg', '.heic', '.webp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.epub', '.doc'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.gz'],
    'Data': ['.csv', '.json'],
    'Diagrams': ['.drawio', '.svg', '.excalidraw']
}

def rename_file_if_exists(dest_folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    
    new_filename = filename
    while os.path.exists(os.path.join(dest_folder, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    
    return new_filename

def organize_folder():
    folder_path = '/Users/samarthgoudar/Downloads'
    
    for filename in os.listdir(folder_path):
        file_ext = os.path.splitext(filename)[1].lower()
        
        for folder, extensions in file_types.items():
            if file_ext in extensions:

                dest_folder = os.path.join(folder_path, folder)
                
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                src_file = os.path.join(folder_path, filename)
                
                # Rename the file if it already exists in the destination
                new_filename = rename_file_if_exists(dest_folder, filename)

                dest_file = os.path.join(dest_folder, new_filename)
                shutil.move(src_file, dest_file)
                print(f'Moved: {filename} -> {new_filename} in {folder}')
                
                break

organize_folder()
