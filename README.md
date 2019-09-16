# My Super Maze by @RoroTiti

![Screenshots](https://i.imgur.com/MRtyN3A.png)

## How to run the app ? (Windows guide)

- Move to the right working directory
```
cd "C:/the/app/directory"
```

- Initialize a virtualenv **(recommended)**
```
pip install virtualenv # if not already installed
virtualenv venv
```

- Enabling the virtual environment
```
.\venv\Scripts\activate
```

- Installing the app dependencies
```
pip install -r .\requirements.txt
```

- Generating a maze file (if not already present)
```
python .\main.py gen
```

- Finally, starting the game !
```
python .\main.py
```

# Making a maze file
You can build a maze file by respecting the following conditions:

- A wall is materialized by ``#`` (dash) character
- A path is materialized by `` `` (space) character
- The guardian is materialised by ``G`` (capital G) character


- The (0;1) block must be a path
- The (15;14) block must be the guardian


- **Not any check is made in order to validate the mz file. You must ensure by yourself that your file is valid.**

# Working environment
- Windows 10
- Python 3.7.4
- PyGame 1.9.6