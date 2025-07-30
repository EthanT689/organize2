import os
import shutil
import logging

# Configure logging
logging.basicConfig(
    filename='file_organizer.log',       # Log file name
    level=logging.INFO,                   # Log level (INFO and above)
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

source_folder = r'C:\Users\Ethan\Downloads'  # Change to your actual folder

file_types = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    "Videos": ['.mp4', '.mkv', '.mov'],
    "Music": ['.mp3', '.wav', '.aac'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
}

def organize_files():
    try:
        for filename in os.listdir(source_folder):
            file_path = os.path.join(source_folder, filename)

            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1].lower()

                moved = False
                for folder, extensions in file_types.items():
                    if file_ext in extensions:
                        folder_path = os.path.join(source_folder, folder)
                        os.makedirs(folder_path, exist_ok=True)
                        try:
                            shutil.move(file_path, os.path.join(folder_path, filename))
                            logging.info(f'Moved: {filename} --> {folder}')
                            moved = True
                        except Exception as e:
                            logging.error(f'Failed to move file {filename}: {e}')
                        break

                if not moved:
                    other_path = os.path.join(source_folder, "Others")
                    os.makedirs(other_path, exist_ok=True)
                    try:
                        shutil.move(file_path, os.path.join(other_path, filename))
                        logging.info(f'Moved: {filename} --> Others')
                    except Exception as e:
                        logging.error(f'Failed to move file {filename}: {e}')
    except Exception as e:
        logging.critical(f'Failed to organize files in folder {source_folder}: {e}')
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    organize_files()
    print("✅ Files organized! Check 'file_organizer.log' for details.")
