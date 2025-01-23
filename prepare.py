import subprocess
import shutil
import os
from google.colab import userdata

# Fetch user credentials and repository details from Colab's `userdata`
GITHUB_TOKEN = userdata.get("GITHUB_TOKEN")
GITHUB_USER_NAME = userdata.get("GITHUB_USER_NAME")
GITHUB_USER_EMAIL = userdata.get("GITHUB_USER_EMAIL")
GITHUB_REPO_NAME = userdata.get("GITHUB_REPO_NAME")

FOLDERS_TO_DELETE = [GITHUB_REPO_NAME, "sample_data"]


# Delete specified folders if they exist
def delete_folders(folders):
    for folder in folders:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"Deleted folder: {folder}")
            except Exception as e:
                print(f"Failed to delete folder {folder}: {e}")


# Check if all required variables are provided
if not all([GITHUB_TOKEN, GITHUB_USER_NAME, GITHUB_USER_EMAIL, GITHUB_REPO_NAME]):
    print(
        "Error: Missing required credentials or repository details. Please ensure all the following are set:"
    )
    print("- GITHUB_TOKEN")
    print("- GITHUB_USER_NAME")
    print("- GITHUB_USER_EMAIL")
    print("- GITHUB_REPO_NAME")
else:
    # Delete folders before proceeding
    delete_folders(FOLDERS_TO_DELETE)

    # Set Git configuration for the user
    try:
        subprocess.run(
            ["git", "config", "--global", "user.name", GITHUB_USER_NAME], check=True
        )
        subprocess.run(
            ["git", "config", "--global", "user.email", GITHUB_USER_EMAIL], check=True
        )

        # Clone the private GitHub repository
        repo_url = f"https://{GITHUB_USER_NAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USER_NAME}/{GITHUB_REPO_NAME}.git"
        subprocess.run(["git", "clone", repo_url], check=True)

        print(f"Successfully cloned repository: {GITHUB_REPO_NAME}")

    except subprocess.CalledProcessError as e:
        print(f"Error during Git operation: {e}")
