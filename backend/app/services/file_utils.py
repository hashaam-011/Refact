import os
import shutil
from fastapi import UploadFile
import aiofiles
import zipfile
import io

async def save_uploaded_zip(file: UploadFile, target_dir: str) -> None:
    """Save an uploaded zip file and extract its contents."""
    # Create a temporary file to store the zip
    temp_path = os.path.join(target_dir, file.filename)

    # Save the uploaded file
    async with aiofiles.open(temp_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    # Extract the zip file
    with zipfile.ZipFile(temp_path, 'r') as zip_ref:
        zip_ref.extractall(target_dir)

    # Remove the temporary zip file
    os.remove(temp_path)

def cleanup_directory(directory: str) -> None:
    """Clean up a directory and its contents."""
    if os.path.exists(directory):
        shutil.rmtree(directory)