@echo off
REM OBMC Intramurals - One-Click Startup Script (Windows)

echo.
echo 🚀 Starting OBMC Intramurals...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python is not installed
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✓ %PYTHON_VERSION% found

REM Install dependencies if needed
echo.
echo 📦 Checking dependencies...
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo    Installing Flask and Flask-CORS...
    pip install -q -r requirements.txt
    if %errorlevel% equ 0 (
        echo ✓ Dependencies installed
    ) else (
        echo ❌ Error installing dependencies
        pause
        exit /b 1
    )
) else (
    echo ✓ All dependencies already installed
)

REM Start Flask server
echo.
echo 🔥 Starting Flask server...
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
echo ✓ Server running on http://localhost:5000
echo.
echo 📝 Next Steps:
echo    1. Open index.html in your browser
echo    2. Use the registration and team checker
echo    3. Press Ctrl+C to stop the server when done
echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.

REM Start Flask
python app.py
pause
