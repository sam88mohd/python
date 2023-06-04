#!/usr/bin/env python3

import os, glob
import supplier_image_upload

def get_contents(file):
    filename, _ = os.path.splitext(os.path.basename(file))
    with open(file, 'r') as f:
        reader = f.readlines()
        reader = [r.strip() for r in reader]
        data = {
            'name': reader[0],
            'weight': int(reader[1].replace(" lbs", "")),
            'description': reader[2],
            'image_name': filename + ".jpeg"
        }

    return data


def main():
    url = "http://localhost/fruits/"
    for file in glob.glob("supplier-data/descriptions/*.txt"):
        content = get_contents(file)
        supplier_image_upload.upload_file(url, content, True)

if __name__ == "__main__":
    main()
