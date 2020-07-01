@echo off

REM get folder name
set "lj=%~p0"
set "lj=%lj:\= %"
for %%a in (%lj%) do set wjj=%%a
set FOLDER_NAME=%wjj%

rd /s /q %FOLDER_NAME%
pyinstaller --onefile --icon=icon.ico %FOLDER_NAME%.py -n %FOLDER_NAME%.exe
copy *.xlsx dist
copy Readme.txt dist
copy test.log dist
move /Y dist %FOLDER_NAME%