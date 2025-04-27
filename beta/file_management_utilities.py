"""
file_management_utilities.py
Provides file management utilities like moving, deleting, and renaming files.
"""

import os
import shutil
import glob

def move_files(source_folder, destination_folder, pattern="*.txt"):
    """
    Move files matching a pattern from source to destination folder.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    files_moved = 0
    for filepath in glob.glob(os.path.join(source_folder, pattern)):
        shutil.move(filepath, destination_folder)
        files_moved += 1
    print(f"Moved {files_moved} files from {source_folder} to {destination_folder}")

def delete_files(folder, pattern="*.tmp"):
    """
    Delete files matching a pattern from a folder.
    """
    files_deleted = 0
    for filepath in glob.glob(os.path.join(folder, pattern)):
        os.remove(filepath)
        files_deleted += 1
    print(f"Deleted {files_deleted} files from {folder}")

def rename_files(folder, prefix="file"):
    """
    Rename all files in a folder with a given prefix.
    """
    count = 0
    for idx, filepath in enumerate(glob.glob(os.path.join(folder, "*"))):
        ext = os.path.splitext(filepath)[1]
        new_filename = f"{prefix}_{idx}{ext}"
        new_filepath = os.path.join(folder, new_filename)
        os.rename(filepath, new_filepath)
        count += 1
    print(f"Renamed {count} files in {folder}")

def search_files(folder, pattern="*.json"):
    """
    Search for files matching a pattern.
    """
    files = glob.glob(os.path.join(folder, pattern))
    print(f"Found {len(files)} files matching {pattern} in {folder}")
    return files

def create_backup_folder(folder, backup_name="backup"):
    """
    Create a backup copy of a folder.
    """
    if not os.path.exists(folder):
        print(f"Folder {folder} does not exist. Cannot create backup.")
        return
    
    backup_path = f"{folder}_{backup_name}"
    if not os.path.exists(backup_path):
        shutil.copytree(folder, backup_path)
        print(f"Backup created at {backup_path}")
    else:
        print(f"Backup folder {backup_path} already exists.")

def simulate_file_management_operations():
    """
    Simulate file operations.
    """
    test_folder = "test_files"
    backup_folder = "test_files_backup"

    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
        with open(os.path.join(test_folder, "sample1.txt"), 'w') as f:
            f.write("Sample file 1.")
        with open(os.path.join(test_folder, "sample2.txt"), 'w') as f:
            f.write("Sample file 2.")
        with open(os.path.join(test_folder, "sample3.tmp"), 'w') as f:
            f.write("Temporary file.")

    print("\n--- Running File Management Simulations ---")
    search_files(test_folder)
    create_backup_folder(test_folder)
    move_files(test_folder, "moved_files", pattern="*.txt")
    delete_files(test_folder, pattern="*.tmp")
    rename_files("moved_files", prefix="document")

