# === CONFIGURATION ===
$obsidianPosts = "C:\Users\2006a\OneDrive\Documentos\Obsidian\03-Blog-Drafts\posts"
$obsidianImages = "C:\Users\2006a\OneDrive\Documentos\Obsidian\ZettelKasten\Assests\Images"
$hugoContent = "C:\Users\2006a\OneDrive\Documentos\abeerblogs\content\docs"
$hugoImages = "C:\Users\2006a\OneDrive\Documentos\abeerblogs\static\images"
$hugoRepo = "C:\Users\2006a\OneDrive\Documentos\abeerblogs"

# === STEP 1: Sync content and images ===
robocopy $obsidianPosts $hugoContent /E /MIR
robocopy $obsidianImages $hugoImages /E /MIR

# === STEP 2: Rewrite image paths in Markdown files ===
Get-ChildItem -Path $hugoContent -Recurse -Include *.md | ForEach-Object {
    (Get-Content $_.FullName) |
    ForEach-Object { $_ -replace '\(\.\.\/\.attachments\/(.*?)\)', '(/images/$1)' } |
    Set-Content $_.FullName
}

# === STEP 3: Git commit + push if needed ===
Set-Location $hugoRepo

git add .

if ((git status --porcelain) -ne $null) {
    git commit -m "Auto: update blog content and images"
    git push
} else {
    Write-Host "No changes to commit."
}
