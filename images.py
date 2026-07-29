import os
import re
import shutil

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"C:\Users\2006a\abeerblogs\content\docs"
attachments_dir = r"C:\Users\2006a\OneDrive\Documents\Obsidian\ZettelKasten\Assests\Images"
static_images_dir = r"C:\Users\2006a\abeerblogs\static\images"

os.makedirs(static_images_dir, exist_ok=True)

used_images_in_posts = set()
pattern = re.compile(r'!\[\[([^]]*\.(?:png|jpg|jpeg|gif|webp))\]\]')

# Step 1: Process each markdown file in the posts directory (using os.walk to support subfolders)
for root, _, files in os.walk(posts_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Step 2: Find all image links in the format ![[path/image.png]]
            images = pattern.findall(content)
            
            # Step 3: Replace image links and ensure URLs are correctly formatted
            for image in images:
                original_filename = os.path.basename(image)
                used_images_in_posts.add(original_filename)
                
                # Sanitize filename: replace spaces with hyphens for web compatibility
                sanitized_filename = original_filename.replace(' ', '-')
                
                # Prepare the Markdown-compatible link
                markdown_image = f"![Image Description](/images/{sanitized_filename})"
                content = content.replace(f"![[{image}]]", markdown_image)
                
                # Step 4: Copy the image to the Hugo static/images directory if it exists
                image_source = os.path.join(attachments_dir, original_filename)
                image_destination = os.path.join(static_images_dir, sanitized_filename)
                
                if os.path.exists(image_source):
                    shutil.copy(image_source, image_destination)
                    print(f"Copied: {original_filename} -> {sanitized_filename}")
                else:
                    print(f"Warning: Image not found: {image_source}")

            # Step 5: Write the updated content back to the markdown file
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(content)

# Step 6: Automatically remove unused/orphan images from Hugo static/images directory
if os.path.exists(static_images_dir):
    sanitized_used_images = {img.replace(' ', '-') for img in used_images_in_posts}
    for existing_img in os.listdir(static_images_dir):
        if existing_img not in sanitized_used_images:
            try:
                os.remove(os.path.join(static_images_dir, existing_img))
                print(f"Removed unused image from site: {existing_img}")
            except OSError:
                pass

print("Markdown files processed and images copied successfully.")