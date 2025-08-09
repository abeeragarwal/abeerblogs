import os
import re
import shutil
from urllib.parse import urlparse

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"C:\Users\2006a\OneDrive\Documentos\abeerblogs\content\docs"
attachments_dir = r"C:\Users\2006a\OneDrive\Documentos\Obsidian\ZettelKasten\Assests\Images"
static_images_dir = r"C:\Users\2006a\OneDrive\Documentos\abeerblogs\static\images"
config_path = r"C:\Users\2006a\OneDrive\Documentos\abeerblogs\hugo.yaml"

# Ensure target directory exists
os.makedirs(static_images_dir, exist_ok=True)

# Determine site subpath from baseURL (e.g., /abeerblogs)
site_subpath = ""
try:
    with open(config_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().lower().startswith("baseurl:"):
                # line like: baseURL: "https://user.github.io/abeerblogs/"
                _, value = line.split(":", 1)
                base = value.strip().strip('"\'\n ')
                parsed = urlparse(base)
                path = parsed.path or "/"
                # normalize to no trailing slash
                if path.endswith("/"):
                    path = path[:-1]
                site_subpath = path
                break
except Exception:
    # Fallback for safety
    site_subpath = ""

# Build the URL prefix for images (works with GitHub Pages subdir)
# If site_subpath is '', this becomes '/images'; if '/abeerblogs', becomes '/abeerblogs/images'
images_url_prefix = f"{site_subpath}/images" if site_subpath else "/images"

# File extensions to support
IMAGE_EXT_PATTERN = r"png|jpe?g|gif|webp"

# Compile regexes
# Obsidian wikilinks: [[file.png]]
wikilink_re = re.compile(r"\[\[([^\]]+\.(?:" + IMAGE_EXT_PATTERN + r"))\]\]", re.IGNORECASE)
# Markdown image: ![alt](path/to/file.png)
md_image_re = re.compile(r"!\[[^\]]*\]\(([^)]+\.(?:" + IMAGE_EXT_PATTERN + r"))\)", re.IGNORECASE)


def url_encode_spaces(path: str) -> str:
    return path.replace(" ", "%20")


def find_image_source(basename: str) -> str | None:
    """Search for image by basename within attachments_dir recursively."""
    # Try direct path first
    direct = os.path.join(attachments_dir, basename)
    if os.path.exists(direct):
        return direct
    # Walk recursively
    for root, _, files in os.walk(attachments_dir):
        if basename in files:
            return os.path.join(root, basename)
    return None


def normalize_to_basename(p: str) -> str:
    # Strip quotes and whitespace
    p = p.strip().strip('"\' ')
    # Convert backslashes to forward slashes, then take basename
    p = p.replace("\\", "/")
    return os.path.basename(p)


# Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if not filename.lower().endswith(".md"):
        continue

    filepath = os.path.join(posts_dir, filename)
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    original_content = content

    # Fix accidental double exclamation (e.g., '!![' -> '![')
    content = content.replace("!![", "![")

    # First handle Obsidian wikilinks [[file.ext]] -> ![Image Description](<prefix>/file.ext)
    wikilinks = wikilink_re.findall(content)
    for link in wikilinks:
        basename = normalize_to_basename(link)
        src_path = find_image_source(basename)
        if src_path:
            shutil.copy(src_path, static_images_dir)
        # Rewrite link
        new_link = f"![Image Description]({images_url_prefix}/{url_encode_spaces(basename)})"
        content = content.replace(f"[[{link}]]", new_link)

    # Then handle existing Markdown image links to normalize their paths
    # We will replace any path (dirs allowed) with just the basename and our URL prefix
    def replace_md_image(match: re.Match) -> str:
        src = match.group(1)
        basename = normalize_to_basename(src)
        # Copy if available
        src_path = find_image_source(basename)
        if src_path:
            shutil.copy(src_path, static_images_dir)
        # Build normalized URL
        normalized = f"{images_url_prefix}/{url_encode_spaces(basename)}"
        # Reconstruct the whole image tag preserving alt text
        full = match.group(0)
        # Replace only the URL inside parentheses
        return full.replace(src, normalized)

    content = md_image_re.sub(replace_md_image, content)

    # Write back only if changes were made
    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")
