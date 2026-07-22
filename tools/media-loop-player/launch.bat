@echo off
setlocal
set "HERE=%~dp0"
set "INDEX=%HERE%index.html"

set "CHROME=%ProgramFiles%\Google\Chrome\Application\chrome.exe"
if not exist "%CHROME%" set "CHROME=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
if not exist "%CHROME%" set "CHROME=%LocalAppData%\Google\Chrome\Application\chrome.exe"

if exist "%CHROME%" (
    start "" "%CHROME%" --kiosk --autoplay-policy=no-user-gesture-required "%INDEX%"
) else (
    echo Chrome not found in the usual locations, opening with your default browser instead.
    echo For a true full-screen kiosk experience, install Chrome or edit launch.bat with your browser's path.
    start "" "%INDEX%"
)
