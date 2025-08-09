# === CONFIGURATION ===
$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$obsidianPosts = "C:\Users\2006a\OneDrive\Documentos\Obsidian\03-Blog-Drafts\posts"
$hugoContent  = "C:\Users\2006a\OneDrive\Documentos\abeerblogs\content\docs"
$hugoRepo     = "C:\Users\2006a\OneDrive\Documentos\abeerblogs"

function Invoke-RoboCopy($Source, $Destination, $Options) {
  robocopy $Source $Destination $Options
  $code = $LASTEXITCODE
  # Robocopy exit codes: 0-7 are success-ish; 8+ indicate failure
  if ($code -ge 8) {
    throw "Robocopy failed with exit code $code"
  }
}

try {
  # === STEP 1: Sync content and images ===
  robocopy $obsidianPosts $hugoContent /E /MIR /XF _index.md

  # === STEP 2: Run image normalization ===
  Set-Location $hugoRepo
  python .\images.py

  # === STEP 3: Simple Git add/commit/push ===
  git add .
  $changes = git status --porcelain
  if ($changes) {
    git commit -m "update site"
    git push
    Write-Host "Changes committed and pushed."
  } else {
    Write-Host "No changes to commit."
  }
}
catch {
  Write-Error $_
  exit 1
}
