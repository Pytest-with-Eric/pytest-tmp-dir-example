import os
import pytest
from image_processor.core import download_image


@pytest.fixture(scope="session")
def image_file(tmp_path_factory):
    image_url = "https://unsplash.com/photos/Ejpx_sdKEKo/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjk4NzI2MDIzfA&force=true"

    # Download the image
    print("Downloading image...")
    tmp_file_path = tmp_path_factory.mktemp("data") / "img.png"
    download_image(image_url=image_url, file_path=tmp_file_path)
    yield tmp_file_path
    print("Removing image...")
    os.remove(tmp_file_path)
