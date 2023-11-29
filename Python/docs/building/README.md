# How to build a python executable

1. Pyinstaller Installation

'pip install pyinstaller'
</br>
2. Ensure all the tests pass
'pip install pytest'
'pytest tests/'
</br>

3. Build
'pyinstaller --onefile abc.py'

## Result
The build should be found in the made dist directory.
Don't forget to move the exe file along with the model file.

