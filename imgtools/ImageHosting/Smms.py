#!/bin/python3

from typing import Tuple

import requests as req
from lxml import etree

from .ImageHosting import ImageHosting

xpath_filename = r'/html/head/meta[@property="og:image:alt"]/@content'
xpath_url = r'/html/head/meta[@property="og:image"]/@content'


class SmmsApp(ImageHosting):
    '''
    an object for sm.ms, which is a fress image hosting website.
    '''

    def __init__(self):
        super().__init__('https://smms.app/image/', 'https://smms.app/api/v2/')

    def parse(self, hashes: str) -> Tuple[str, str]:
        url = self.base_url / hashes
        html = etree.HTML(req.get(url()).text, None)  # use the default HTML parser from etree
        return html.xpath(xpath_filename)[0], html.xpath(xpath_url)[0]


smms_app = SmmsApp()

# EOF
