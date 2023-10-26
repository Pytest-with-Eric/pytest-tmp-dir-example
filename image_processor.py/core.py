import requests

# The URL of the image you want to download
image_url = "https://unsplash.com/photos/green-northern-lights-at-night-Ejpx_sdKEKo"

# Send an HTTP GET request to the image URL
response = requests.get(image_url)

# Check if the request was successful (HTTP status code 200 indicates success)
if response.status_code == 200:
    # Get the content of the response, which contains the image data
    image_data = response.content

    # Specify the file path where you want to save the image
    file_path = "downloaded_image.png"

    # Open a file and write the image data to it
    with open(file_path, "wb") as image_file:
        image_file.write(image_data)

    print(f"Image downloaded and saved as '{file_path}'")
else:
    print(f"Failed to download image. Status code: {response.status_code}")
