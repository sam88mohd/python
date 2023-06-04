#!/usr/bin/env python3
from PIL import Image
import os, glob

def generate(file_path):
  file, _ =os.path.splitext(file_path)
  with Image.open(file_path) as i:
    background = Image.new("RGB", (600, 400), (255, 255, 255))
    background.paste(i, mask=i.split()[3])
    background.save(file + ".jpeg", "JPEG")

def main():
  for file in glob.glob("supplier-data/images/*.tiff"):
    generate(file)
    os.remove(file)

if __name__ == "__main__":
  main()
