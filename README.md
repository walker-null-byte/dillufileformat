# Dillu File Format
## Version 1.0.0

## Brief Overview 
- Dillu File Format is a file container format, where you can put a large amount of files inside a container file and share it accross different platforms.
- The contents are not compressed.
- Very easy to encode and decode
## Note
- Avoid having UTF 16 or UTF 8 SPECIAL characters in FILE NAMES. This will lead to you being not able to extract the data.
- Avoid encoding a folder with LOTS of fragmentation. For example the game files of L4D2 will crash your PC if you try to put the contents in this file. 
- This is because L4D2 is above 30,000 files! I dont know what the devs were thinking SMH.

## Commands 
- --help/-h
- --version/-v
- --export/-e
- --extract/-x
- --list/-l

## Usage
- Place the main.py and the misc folder where the file you want to compress is

## For help 
``` python3 main.py  --help ```

## For compressing
``` python3 main.py --export <filename> ```
  or
``` python3 main.py --export <filename> <output> ```

## For listing contents
``` python3 main.py --list <filename> ```

## For extracting 
``` python3 main.py --extract <filename> ```
or
``` python3 main.py --extract <filename> <output_folder> ```
