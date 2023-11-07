import requests
from PIL import Image
import os


def download_image(image_url: str, file_path: str) -> bool:
    """
    Downloads an image from the specified URL and saves it to the current directory.

    Parameters
    ----------
    image_url : str
        The URL of the image to download.
    file_path : str
        The path where the downloaded image will be saved.

    Returns
    -------
    bool
        True if the image was downloaded successfully, False otherwise.
    """
    # Send an HTTP GET request to the image URL
    response = requests.get(image_url)

    # Check if the request was successful (HTTP status code 200 indicates success)
    if response.status_code == 200:
        # Get the content of the response, which contains the image data
        image_data = response.content

        # Open a file and write the image data to it
        with open(file_path, "wb") as image_file:
            image_file.write(image_data)

        print(f"Image downloaded and saved as '{file_path}'")
        return True
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
        return False


def generate_thumbnail(image_path: str) -> str:
    """
    Generates a thumbnail for the specified image using the Pillow library.

    Args:
        image_path (str): Path to the input image.

    Returns:
        str: A message indicating the success or failure of thumbnail generation.
    """
    size = (128, 128)

    # Check if the input image exists
    if not os.path.exists(image_path):
        return f"Image not found: '{image_path}'"

    # Generate a thumbnail
    try:
        with Image.open(image_path) as im:
            im = im.resize(size)  # Resize to a fixed size (disregards aspect ratio)
            file, ext = os.path.splitext(image_path)
            thumbnail_path = file + "_thumbnail.png"
            im.thumbnail(size)
            im.save(thumbnail_path, "PNG")
            print(f"Thumbnail generated for '{image_path}' as '{thumbnail_path}'")
            return thumbnail_path
    except Exception as e:
        raise e


# if __name__ == "__main__":
#     image_url = "https://unsplash.com/photos/Ejpx_sdKEKo/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjk4NzI2MDIzfA&force=true"

#     # Download the image
#     file_path = download_image(image_url)

#     # Generate a thumbnail
#     generate_thumbnail()
