# pan-hound

Console python utility for PAN searching in files

            |\
   \`-. _.._| \
    |_,'  __`. \
    (.\ _/.| _  |
   ,'      __ \ |
 ,'     __/||\  |
(PAN  ,/|||||/  |
   `-'_----    /
      /`-._.-'/
      `-.__.-' 

### Prerequisites

To run this project you need:

```
python2.7
```

### Installing

WIP. Just copy-paste the code and give run permissions to file:

```[username@localhost ~]$ cmod u+x pan-hound.py```

## Running

WIP. 

```[username@localhost ~]$ ./pan-hound.py -h
usage: pan-hound.py [-h] [--dir DIR] [--glob GLOB]

DESCRIPTION:
    Find PAN matches recursively in files from the given folder

optional arguments:
  -h, --help            show this help message and exit
  --dir DIR, -d DIR     folder to search in; by default current folder
  --glob GLOB, -g GLOB  glob pattern, i.e. *.html

USAGE:
    pan-hound.py -d [my_folder] -g [glob_pattern]
[username@localhost ~]$
[username@localhost ~]$ ./pan-hound.py -d path/to/folder/
17 matches in /home/username/path/to/folder/file.with.pan```