#!/bin/python3

from pathlib import Path
from typing import Tuple, Union
from urllib.request import urlopen, Request

# import requests as req

from ..utils import UniformResourceLocator

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}


class ImageHosting:
    '''
    Base class for Image Hosting Websites, for URL/downloaded managing
    '''

    def __init__(self, base_url: str, api_url: str):
        '''
        initialization of this class

        Args:
            base_url (str): prefix of URL of Image Hosting API, or URL of image info page
            api_url (str): prefix of API URL provided by the Image Hosting Website
        '''
        self.base_url = UniformResourceLocator(base_url)
        self.api_url = UniformResourceLocator(api_url)

    def parse(self, hashes: str) -> Tuple[str, str]:
        '''
        parse the image info obtained by API or image page
        it should be implemented by derived class

        Args:
            hashes (str): hashed path of target images

        Returns:
            Tuple[str, str]: filename & CDN url
        '''
        ...

    def download(self, dest_dir: Path, filename: str, url: str) -> Path:
        '''
        download the image to destination directory

        Args:
            dest_dir (Path): destination directory to store the image
            filename (str): filename of image without parent path, or decoded by APIs of Image Hosting Website
            url (str): the direct URL to image

        Returns:
            Path: a path object of downloaded image
        '''
        img = dest_dir / filename

        if not img.exists():
            resp = urlopen(url)
            with open(img, 'wb') as f:
                f.write(resp.content)

        return img

    def open(self, url: str):
        '''
        load online image into the memory

        Args:
            url (str): the url of pure online image

        Returns:
            a file-like object
        '''
        return urlopen(Request(url, headers=headers))

    def upload(self, src: Union[Path, str]) -> str:
        '''
        upload image
        it should be implemented by derived class

        Args:
            src (Union[Path, str]): path of source image

        Returns:
            str: the hashed path from the website
        '''
        ...

    def __call__(self, hashes: str):
        '''
        interface to download image

        Args:
            dest_dir (str): destination directory to store the image
            hashes (str): hashed path of target images

        Returns:
            a file-like object
        '''
        _, url = self.parse(hashes)
        return self.open(url)


# EOF
