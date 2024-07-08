import os
from pathlib import Path
from openai import OpenAI
import requests
client = OpenAI(api_key="example-key")
DIFY_API_KEY = "example-key"

def translate_text(api_key=DIFY_API_KEY, user_id="mark-doc", inputs={'input_text': 'Hello, how are you?', 'target_language': 'es'}):
    url = 'https://api.dify.ai/v1/workflows/run'
    headers = {
      'Authorization': f'Bearer {api_key}',
      'Content-Type': 'application/json'
    }
    data = {
      'inputs': inputs,
      'response_mode': 'blocking',
      'user': user_id
    }
    response = requests.post(url, headers=headers, json=data)
    
    try:
        # Check if the response status code indicates success (200 OK)
        response.raise_for_status()
        # Attempt to decode the JSON response
        json_response = response.json()
        return json_response['data']['outputs']
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (e.g., 404 Not Found, 401 Unauthorized)
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as req_err:
        # Handle other requests-related errors (e.g., connection errors)
        print(f'Request error occurred: {req_err}')
    except json.decoder.JSONDecodeError:
        # Handle JSON decode errors (e.g., empty response body)
        print('Failed to decode JSON response')
    
    # Return None or an appropriate value in case of error
    return None

def translate_markdown_files(input_folder, output_folder, target_language="japanese"):
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    for markdown_file in input_folder.rglob("*.md"):
        relative_path = markdown_file.relative_to(input_folder)
        output_file = output_folder / relative_path
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(markdown_file, "r", encoding="utf-8") as f:
            content = f.read()
            print(f"Translating {markdown_file} to {target_language}")
            # print(content)
        
        translated_content = translate_text(inputs={'input_text': content, 'target_language': target_language})
        
        # Inside the loop, after translating the content
        if translated_content is not None:
          translated_text = translated_content['final']
          with open(output_file, "w", encoding="utf-8") as f:
            f.write(translated_text)
        else:
          print(f"Warning: No translated content for {markdown_file}. Skipping file.")
    
    print(f"Translation completed. Translated files are saved in {output_folder}")

# Example usage
# translate_markdown_files("zh_CN/explore", "jp/explore", target_language="japanese")

# ------------------------------------------------------------
# Create a new folder for the translated files
import os
import shutil

def create_empty_folders(source_dir, target_dir):
    """
    Create a set of empty folders in the target directory with the same folder structure as the source directory.

    :param source_dir: Path to the source directory.
    :param target_dir: Path to the target directory where the empty folders will be created.
    """
    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)
    
    # Walk through the source directory
    for dirpath, dirnames, filenames in os.walk(source_dir):
        # Construct the path structure in the target directory
        structure = os.path.join(target_dir, os.path.relpath(dirpath, source_dir))
        # Create each directory in the target directory
        for dirname in dirnames:
            os.makedirs(os.path.join(structure, dirname), exist_ok=True)

# Example usage
source_directory = 'zh_CN'
target_directory = 'en/.gitbook'
# create_empty_folders(source_directory, target_directory)


# ------------------------------------------------------------
import os
import re
import shutil

def check_and_move_images(markdown_dir, images_dir, target_images_dir):
    """
    Check if the images used in the markdown files exist and then move them to a specified location.
    If images are already at the specified location, then check the existence.

    :param markdown_dir: Directory containing markdown files.
    :param images_dir: Directory containing images referenced in the markdown files.
    :param target_images_dir: Target directory to move the images to.
    """
    # Regex to find markdown image syntax
    img_regex = r'<img src="(.*?)"'
    
    # Ensure the target images directory exists
    os.makedirs(target_images_dir, exist_ok=True)
    
    # Walk through the markdown directory
    print(f"Checking images in markdown files in: {markdown_dir}")
    # Walk through the markdown directory
    for root, dirs, files in os.walk(markdown_dir):
        print(f"Checking images in markdown files in: {root}")
        for file in files:
            print(f"Checking images in: {file}")
            if file.endswith(".md"):
                # Open and read the markdown file
                with open(os.path.join(root, file), 'r', encoding='utf-8') as md_file:
                    content = md_file.read()
                
                # Find all image paths in the file
                image_paths = re.findall(img_regex, content)
                modified = False  # Flag to track if content was modified
                
                for img_path in image_paths:
                    # Normalize the image path to handle relative paths
                    normalized_img_path = os.path.normpath(os.path.join(images_dir, img_path))
                    target_img_path = os.path.join(target_images_dir, os.path.basename(img_path))
                    # Check if the image is already in the target directory
                    if os.path.exists(target_img_path):
                        print(f"Image already in target location: {target_img_path}")
                    elif os.path.exists(normalized_img_path):
                        print(f"Image found: {normalized_img_path}")
                        # Move the image to the target directory
                        shutil.move(normalized_img_path, target_img_path)
                        print(f"Image moved to: {target_img_path}")
                        modified = True
                        # Update the image path in the markdown content
                        new_img_path = '/' + target_img_path.replace("\\", "/")
                        content = content.replace(img_path, new_img_path)
                        print(f"Image link replaced with: {target_img_path}")
                    else:
                        print(f"Image not found: {normalized_img_path} in {file}")
                
                # If the content was modified, write it back to the markdown file
                if modified:
                    with open(os.path.join(root, file), 'w', encoding='utf-8') as md_file:
                        md_file.write(content)

# Example usage
markdown_directory = 'en/learn-more/'
images_directory = 'en/en/en/.gitbook'
target_images_directory = 'en/.gitbook/assets/learn-more/'
check_and_move_images(markdown_directory, images_directory, target_images_directory)
