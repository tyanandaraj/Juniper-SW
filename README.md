# Juniper-SW

- to run the current GUI, run "maingui.py"
- refer to "pyqtesting.py" for various qt examples with comments

Testing in Windows:
1. Download Python3 and PyQt libraries (refer to tutorials on youtube in resources in channel on discord)
2. Download all files from the GUI folder in the repo
3. Open test.ui in Qt Designer and make any necessary changes
4. Save test.ui
5. Open cmd prompt and navigate to directory containing GUI folder files
6. Run this script: pyuic5 -x test.ui -o maingui.py           # this updates maingui.py code with changes from Qt designer

