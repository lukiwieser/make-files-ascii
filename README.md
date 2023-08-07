# Make Files ASCII

Convert filenames from Unicode to ASCII.

Examples: 
- `Åland.txt` → `Aland.txt`
- `Curaçao.txt` → `Curacao.txt`

You can additionally replace other characters such as `'`:
- `Côte d'Ivoire.txt` → `Cote d Ivoire.txt`

## Usage

This project requires Python 3.11 to be installed on your machine.

First install the dependencies by executing the following command in the project folder:

```console
pip install -r requirements.txt
```

Then simply execute the script with the following command:

```console
python main.py
```

Next the script will ask for some options like the location of the folder/file. 
After entering all parameters, a preview of the renamed filenames/file-content will be shown.


## Features

- rename filenames
- rename content of files
- see a preview of the changes before renaming
- optionally replace other characters e.g. Apostrophe `'` with Space ` `

## Motivation 

Some filesystems do not support special characters. 
For example, when uploading a dataset to *Kaggle*, only ASCII filenames are support, and the Apostrophe `'` is also not allowed. 

Therefore it can be useful to replace such special characters. 
Additionally there might be files that reference these filenames somehow, thus renaming the content of a file could also make sense.

## Supported Platforms

This project was tested on Windows 11 and Ubuntu 22.04.
