# PowerShell script to setup GitHub repository

Write-Host "Setting up 2048 GitHub repository..." -ForegroundColor Green

# Check if git is available
$gitInstalled = Get-Command git -ErrorAction SilentlyContinue
if (-not $gitInstalled) {
    Write-Host "ERROR: Git is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Git from https://git-scm.com/download/win" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Initialize repository
Write-Host "`nInitializing Git repository..." -ForegroundColor Cyan
git init

# Add files
Write-Host "Adding files..." -ForegroundColor Cyan
git add .

# Create commit
Write-Host "Creating initial commit..." -ForegroundColor Cyan
git commit -m "Initial commit: 2048 game implementation"

# Check if gh CLI is available
$ghInstalled = Get-Command gh -ErrorAction SilentlyContinue
if (-not $ghInstalled) {
    Write-Host "`nWARNING: GitHub CLI (gh) is not installed" -ForegroundColor Yellow
    Write-Host "Please create the repository manually on GitHub, then run:" -ForegroundColor Yellow
    Write-Host "git branch -M main" -ForegroundColor White
    Write-Host "git remote add origin https://github.com/YOUR_USERNAME/2048.git" -ForegroundColor White
    Write-Host "git push -u origin main" -ForegroundColor White
} else {
    Write-Host "`nCreating GitHub repository..." -ForegroundColor Cyan
    gh repo create 2048 --public --source=. --remote=origin --push
    Write-Host "`nDone! Repository created and pushed to GitHub." -ForegroundColor Green
}

Read-Host "`nPress Enter to exit"
