# Make Files ASCII

Small python script to rename files to a ASCII variant.

Examples: 
- `Åland.txt` → `Aland.txt`
- `Curaçao.txt` → `Curacao.txt`

## Usage

This project requires Python 3.11 to be installed on your machine, and only works on Windows.

Simply execute the script with the following command:

```console
python main.py
```

Next the script will ask for some options like the location of the folder(file. After entering all parameters a preview of the renamed filenames/file-content will be shown.

## Features

- rename filenames
- rename content of files
- see a preview of the changes before renaming

## Motivation 

Some filesystems do not support special characters. For example Kaggle does only support ASCII filenames and the Apostroph `'` is also not allowed. 

Therefore it can be usefull to replace such special charachters. Additionally there migth be files that reference these filenames somehow, thus renaming the content of a file could also make sense.
