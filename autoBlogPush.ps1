# === CONFIGURATION ===
$obsidianPosts = "C:\Users\2006a\OneDrive\Documentos\Obsidian\03-Blog-Drafts\posts"
$hugoContent = "C:\Users\2006a\OneDrive\Documentos\abeerblogs\content\docs"
$hugoRepo = "C:\Users\2006a\OneDrive\Documentos\abeerblogs"
$imagesScript = "C:\Users\2006a\OneDrive\Documentos\abeerblogs\images.py"

# === STEP 1: Sync blog posts ===
Write-Host "Syncing blog posts..."
robocopy $obsidianPosts $hugoContent /E /MIR /XF _index.md

# === STEP 2: Process images using Python script ===
Write-Host "Processing images and converting wiki-links..."
python $imagesScript

# === STEP 3: Git commit + push if needed ===
Write-Host "Checking for changes..."
Set-Location $hugoRepo

git add .

if ((git status --porcelain) -ne $null) {
    git commit -m "Auto: update blog content and images"
    Write-Host "Pushing changes to GitHub..."
    git push
    Write-Host "Blog updated successfully!"
} else {
    Write-Host "No changes to commit."
}
