# CS3201-Programming-Assignment
CS3201 Programming Assignment - MAN Kai Wing


## How to compile and run the code
First, you need to have pip to download PyInstaller. Next, use the PyInstaller to compile the python code. Finally, you can send the .exe file to anyone with who you want to share.

### Installation of PIP
The pip will automatically download with python.
If you don't have, you can download it from [here](https://pip.pypa.io/en/stable/installing/).

## Installation of PyInstaller
To install the PyInstaller, you need to open the Command Prompt and run.
```sh
pip install pyinstaller
```

## To compile the code
Open the Command Prompt and go to the program’s directory and run:
```sh
pyinstaller --onefile BulletinBoardClient.py
```

After the script running, you will see the directory it should have created two folders and one file.
  - dist (directory)
  - build (directory)
  - BulletinBoardClient.spec

## run the code
Go to the dist directory. You will see the BulletinBoardClient.exe file. If you want to run the code, just double-click it. Also, you can share this application with your friends by sending the .exe file.


