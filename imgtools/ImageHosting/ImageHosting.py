#!/bin/python3

from pathlib import Path
from typing import Tuple, Union

import requests as req

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

    def open(self, url: str):
        '''
        load online image into the memory

        Args:
            url (str): the url of pure online image

        Returns:
            a file-like object
        '''
        return req.get(url, headers=headers)

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

    def __call__(self, hashes: str, dest: Union[Path, str]):
        '''
        interface to download image

        Args:
            dest_dir (str): destination directory to store the image
            hashes (str): hashed path of target images
        '''
        dest = dest if isinstance(dest, Path) else Path(dest)
        _, url = self.parse(hashes)

        with req.get(url, headers=headers) as resp:
            with open(dest, 'wb') as f:
                f.write(resp.content)


# EOF
