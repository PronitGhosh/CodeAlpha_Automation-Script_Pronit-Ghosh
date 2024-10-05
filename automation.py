import os
import shutil
from pathlib import Path
print("Press 1 for File organisation")
print("Press 2 for data cleaning / file deletion")
choice=int(input("Enter your choice"))
folder_to_organize =input("Enter the path: ")
extensions_folders = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
    'audio': ['.mp3', '.wav', '.flac'],
    'videos': ['.mp4', '.mov', '.avi'],
    'archives': ['.zip', '.tar', '.rar', '.gz'],
    'scripts': ['.py', '.js', '.sh', '.bat'],
}
if choice==1:
 for folder in extensions_folders.keys():
    os.makedirs(os.path.join(folder_to_organize, folder), exist_ok=True)

 for item in os.listdir(folder_to_organize):
    item_path = os.path.join(folder_to_organize, item)
    
    # Only organize files, not directories
    if os.path.isfile(item_path):
        file_extension = Path(item).suffix  # Get the file extension
        moved = False

        # Move the file based on its extension
        for folder, extensions in extensions_folders.items():
            if file_extension in extensions:
                shutil.move(item_path, os.path.join(folder_to_organize, folder, item))
                moved = True
                break
        
        # If the file type doesn't match any folder, move it to an "others" folder
        if not moved:
            other_folder = os.path.join(folder_to_organize, 'others')
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(other_folder, item))

 print("File organization completed.")
elif choice==2:
    file_name=input("Enter the command :")
    if 'images' in file_name:
         for item in os.listdir(folder_to_organize):
           item_path = os.path.join(folder_to_organize, item)
           if os.path.isfile(item_path):
              file_extension = Path(item).suffix  # Get the file extension
              image_extentions=extensions_folders.get('images',[])
              if file_extension in image_extentions:
                  os.remove(item_path)
         print("Deleted images")
    elif 'documents' in file_name:
         for item in os.listdir(folder_to_organize):
           item_path = os.path.join(folder_to_organize, item)
           if os.path.isfile(item_path):
              file_extension = Path(item).suffix  # Get the file extension
              image_extentions=extensions_folders.get('documents',[])
              if file_extension in image_extentions:
                  os.remove(item_path)
         print("Deleted documents")          
    elif 'audio' in file_name:
         for item in os.listdir(folder_to_organize):
           item_path = os.path.join(folder_to_organize, item)
           if os.path.isfile(item_path):
              file_extension = Path(item).suffix  # Get the file extension
              image_extentions=extensions_folders.get('audio',[])
              if file_extension in image_extentions:
                  os.remove(item_path)
         print("Deleted audio files")             
    elif 'video' in file_name:
         for item in os.listdir(folder_to_organize):
           item_path = os.path.join(folder_to_organize, item)
           if os.path.isfile(item_path):
              file_extension = Path(item).suffix  # Get the file extension
              image_extentions=extensions_folders.get('videos',[])
              if file_extension in image_extentions:
                  os.remove(item_path)
         print("Deleted videos")      
