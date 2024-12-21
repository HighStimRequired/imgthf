:: Run the Python script
python imgthf.py

if %errorlevel% neq 0 (
    echo ERROR: Failed to run imgthf.py. Please check the script for errors.
    pause
    exit /b
)

echo ========================================
echo Script executed successfully!
echo ========================================
pause