# === CONFIGURATION ===
$obsidianPosts = "C:\Users\2006a\OneDrive\Documents\Obsidian\03-Blog-Drafts\posts" 
$hugoContent   = "C:\Users\2006a\abeerblogs\content\docs"
$hugoRepo      = "C:\Users\2006a\abeerblogs"
$imagesScript  = "C:\Users\2006a\abeerblogs\images.py"

# === STEP 1: Sync blog posts ===
Write-Host "Syncing blog posts..." -ForegroundColor Cyan
robocopy $obsidianPosts $hugoContent /E /MIR /XF _index.md

# === STEP 2: Process images using Python script ===
Write-Host "Processing images and converting wiki-links..." -ForegroundColor Cyan
python $imagesScript

# === STEP 3: Git commit + push if needed ===
Write-Host "Checking for changes..." -ForegroundColor Cyan
Set-Location $hugoRepo

git add .

if ((git status --porcelain) -ne $null) {
    git commit -m "Auto: update blog content and images"
    Write-Host "Pushing changes to GitHub..." -ForegroundColor Green
    git push origin main
    Write-Host "Blog updated successfully!" -ForegroundColor Green
} else {
    Write-Host "No changes to commit." -ForegroundColor Yellow
}