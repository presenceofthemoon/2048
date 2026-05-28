@echo off
echo Initializing Git repository...
git init

echo Adding files...
git add .

echo Creating initial commit...
git commit -m "Initial commit: 2048 game implementation"

echo Creating GitHub repository...
gh repo create 2048 --public --source=. --remote=origin --push

echo Done! Repository created and pushed to GitHub.
pause
