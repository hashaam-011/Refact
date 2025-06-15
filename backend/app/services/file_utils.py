import zipfile
import os
from fastapi import UploadFile

async def save_uploaded_zip(file: UploadFile, dest_folder: str):
    file_path = os.path.join(dest_folder, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)

    os.remove(file_path)