import requests
from PIL import Image
import glob, os


def download_image(image_url: str) -> bool:
    """
    Downloads an image from the specified URL and saves it to the current directory.

    Parameters
    ----------
    image_url : str
        The URL of the image to download.

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

        # Specify the file path where you want to save the image
        file_path = "image.png"

        # Open a file and write the image data to it
        with open(file_path, "wb") as image_file:
            image_file.write(image_data)

        print(f"Image downloaded and saved as '{file_path}'")
        return file_path
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
        return False


def generate_thumbnail() -> None:
    """
    Generates a thumbnail for all PNG images in the current directory using the Pillow library.
    """
    size = 128, 128

    for infile in glob.glob("*.png"):
        file, ext = os.path.splitext(infile)
        with Image.open(infile) as im:
            im.thumbnail(size)
            im.save(file + ".thumbnail", "PNG")
            print(f"Thumbnail generated for '{file}' as '{file}_thumbnail.png'")


if __name__ == "__main__":
    image_url = "https://unsplash.com/photos/Ejpx_sdKEKo/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjk4NzI2MDIzfA&force=true"

    # Download the image
    file_path = download_image(image_url)

    # Generate a thumbnail
    generate_thumbnail()
