import os
import shutil
import zipfile

# Extract and merge zip files
def extract_and_merge_zip(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # Extract zip contents to a temporary directory
        zip_ref.extractall('temp')
        
        # Move or merge extracted files and directories to main working directory
        for item in os.listdir('temp'):
            src = os.path.join('temp', item)
            dst = os.path.join('main_directory', item)
            if os.path.exists(dst):
                # Merge directories if destination already exists
                if os.path.isdir(src) and os.path.isdir(dst):
                    merge_directories(src, dst)
                else:
                    # If destination exists and it's not a directory, rename it
                    base, ext = os.path.splitext(dst)
                    new_dst = f"{base}_1{ext}"
                    shutil.move(src, new_dst)
            else:
                # If destination doesn't exist, move the item
                shutil.move(src, dst)
    
    # Clean up temporary directory
    shutil.rmtree('temp')

# Merge directories
def merge_directories(src, dst):
    # Iterate over files in source directory and move them to destination
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, item)
        if os.path.exists(dst_item):
            # If destination item exists, handle conflicts intelligently
            if os.path.isdir(src_item):
                # If source item is a directory, recursively merge directories
                merge_directories(src_item, dst_item)
            else:
                # If source item is a file, rename it before moving
                base, ext = os.path.splitext(dst_item)
                new_dst_item = f"{base}_1{ext}"
                shutil.move(src_item, new_dst_item)
        else:
            # If destination item doesn't exist, move the item
            shutil.move(src_item, dst)


def main():
    # Create main working directory if it doesn't exist
    if not os.path.exists('main_directory'):
        os.makedirs('main_directory')
    
    # List and sort zip files
    zip_files = sorted([f for f in os.listdir() if f.endswith('.zip')])
    
    # Extract and merge each zip file
    for zip_file in zip_files:
        extract_and_merge_zip(zip_file)
        
    # Check for duplicates and organize files as needed
if __name__ == "__main__":
    main()
