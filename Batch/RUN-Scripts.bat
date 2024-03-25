@echo off

taskkill /f /im pythonw.exe
cd "C:\Users\Matt\Documents\Scripts\Python"
for /r "." %%a in (*.py) do start "" pyw "%%~fa"

exit