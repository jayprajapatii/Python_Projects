import os
import shutil

def move_files_by_extension(source_dir, target_dir):
    """
    Moves files from source_dir into extension-wise folders inside target_dir.
    """

    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            filepath = os.path.join(root, filename)

            if os.path.isfile(filepath):
                # Get extension (without dot, lowercase)
                ext = os.path.splitext(filename)[1][1:].lower()

                if ext == "":  # files without extension
                    ext = "no_extension"

                # Create folder for this extension
                ext_folder = os.path.join(target_dir, ext)
                os.makedirs(ext_folder, exist_ok=True)

                # Move file into extension folder
                target_path = os.path.join(ext_folder, filename)
                shutil.move(filepath, target_path)

                print(f"Moved {filename} -> {ext_folder}")


# Example usage
source_directory = r"C:\.babun"      # Your source directory
target_directory = r"C:\SortedFiles" # Folder where sorted files will be stored

move_files_by_extension(source_directory, target_directory)