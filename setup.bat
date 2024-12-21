@echo off
echo ========================================
echo Python Dependency Installer and Runner
echo ========================================

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python...
    
    :: Download the Python installer (adjust the URL to the latest version as needed)
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe -OutFile python-installer.exe"
    
    :: Run the installer silently
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    
    :: Verify Python installation
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo ERROR: Python installation failed. Please install Python manually.
        pause
        exit /b
    )
    echo Python installed successfully!
)

:: Upgrade pip to the latest version
echo Upgrading pip to the latest version...
python -m pip install --upgrade pip

:: Install required dependencies
echo Installing requests and beautifulsoup4...
pip install requests beautifulsoup4

:: Check for installation success
if %errorlevel% neq 0 (
    echo ERROR: Failed to install one or more dependencies.
    pause
    exit /b
)

echo ========================================
echo All dependencies installed successfully!
echo ========================================
pause
