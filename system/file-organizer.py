import os
import shutil

def organize_files(source_dir, destination_dir):
    # Create a dictionary to map file extensions to folder names
    file_formats = {
        '.txt': 'Files',
        '.jpg': 'Images',
        '.png': 'Images',
        '.jfif': 'Images',
        '.html': 'Sources',
        '.ipynb': 'Sources',
        '.ppt': 'Files',
        '.json': 'Sources',
        '.zip': 'Archives',
        '.rar': 'Archives',
        '.webp': 'Images',
        '.pdf': 'Files',
        '.docx': 'Files',
        '.doc': 'Files',
        '.jpeg': 'Images',
        '.mp3': 'Audios',
        '.mov': 'Videos',
        '.mp4': 'Videos',
        '.m4a': 'Videos',

        # You can add more file formats and corresponding folder names as needed
    }

    # Create folders for each file format if they don't exist
    for folder_name in file_formats.values():
        folder_path = os.path.join(destination_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Organize files
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in file_formats:
                format_folder = file_formats[file_extension]
                format_folder_path = os.path.join(destination_dir, format_folder)
                shutil.move(file_path, os.path.join(format_folder_path, filename))

if __name__ == "__main__":
    # Any directory file you want to organize
    source_directory = "C:\\Users\\0000\\-----"
    # Destination of the organized folders
    destination_directory = "C:\\Users\\0000\\-----"

    organize_files(source_directory, destination_directory)
    print("File format organizer has completed.")