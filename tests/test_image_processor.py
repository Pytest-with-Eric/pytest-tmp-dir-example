import os
from PIL import Image
from image_processor.core import generate_thumbnail


def test_generate_thumbnail(image_file):
    temp_file_path = image_file
    print("Generating thumbnail...")
    thumbnail_path = generate_thumbnail(image_path=temp_file_path)
    print(thumbnail_path)

    # Check if the thumbnail file exists
    assert os.path.exists(thumbnail_path)

    # Check content type
    assert thumbnail_path.endswith("_thumbnail.png")

    img = Image.open(thumbnail_path)

    # get width and height
    width, height = img.size

    # display width and height
    assert width == 128
    assert height == 128
