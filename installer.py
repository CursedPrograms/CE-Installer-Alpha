import os
import shutil
import zipfile

def extract_files(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def copy_files(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, False, None)
        else:
            shutil.copy2(s, d)

def main():
    zip_path = 'path/to/your/archive.zip'
    extract_to = 'path/to/extract'
    install_dir = 'path/to/install'
    
    extract_files(zip_path, extract_to)
    copy_files(extract_to, install_dir)

if __name__ == "__main__":
    main()