@echo off
rem Double-click on Windows: syncs this computer with GitHub using Git Bash (comes with Git for Windows, x64 or ARM64).
cd /d "%~dp0..\.."
"%ProgramFiles%\Git\bin\bash.exe" scripts/sync/sync.sh %*
pause
