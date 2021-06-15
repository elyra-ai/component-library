# Utilities used by CLAIMED

import os
import zipfile

# compresses 'path' into 'target' zipfile


def zipdir(target, path):
    print("adding "+path+" to "+target)
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                zipf.write(os.path.join(root, file))

# uncompresses 'zipfile_name' to 'target' directory


def unzip(target, zipfile_name):
    with zipfile.ZipFile(zipfile_name, 'r') as zip_ref:
        zip_ref.extractall(target)
