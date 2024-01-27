@echo off
setlocal

@REM https://chat.openai.com/c/143bf330-901c-46ea-9115-03b450fdd07d
@REM Also install Python 3 if needed

set VENV_DIR=%USERPROFILE%\.mosamatic\MosamaticDesktop

if not exist "%USERPROFILE%\.mosamatic\" mkdir "%USERPROFILE%\.mosamatic"
cd /d "%USERPROFILE%\.mosamatic"

if not exist "%VENV_DIR%" (
    python -m venv "%VENV_DIR%"
)

call "%VENV_DIR%\Scripts\activate"

%USERPROFILE%\.mosamatic\MosamaticDesktop\bin\pip install --upgrade pip
%USERPROFILE%\.mosamatic\MosamaticDesktop\bin\pip install mosamaticdesktop

call "%VENV_DIR%\Scripts\deactivate.bat"

copy %USERPROFILE%\.mosamatic\MosamaticDesktop\Scripts\mosamatic.bat C:\Windows

echo "Installation finished."
echo "You can now run Mosamatic by typing 'mosamatic.bat' and pressing enter."

endlocal