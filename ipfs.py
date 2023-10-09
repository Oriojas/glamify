import io
import os

from lighthouseweb3 import Lighthouse

LH_TOKEN = os.environ["LH_TOKEN"]

# Replace "YOUR_API_TOKEN" with your actual Lighthouse API token
lh = Lighthouse(token=LH_TOKEN)

# Regular file upload
source_file_path = "./path/to/your/file/or/directory"
upload = lh.upload(source=source_file_path)
print("Regular File Upload Successful!")

# File upload with tags
tagged_source_file_path = "input_img/"
tag = "test_img"
upload_with_tag = lh.upload(source=tagged_source_file_path, tag=tag)
print("File Upload with Tag Successful!")