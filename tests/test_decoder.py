import os
from unittest import TestCase
from qreader.constants import DATA_TYPE_TEXT
from qreader.decoder import QRDecoder
from PIL import Image

__author__ = 'ewino'


class TestDecoder(TestCase):
    def _get_res_path(self, *path):
        return os.path.join(os.path.dirname(__file__), 'resources', *path)

    def test_get_first(self):
        image = Image.open(self._get_res_path('Qr-1-noborder.png'))
        decoder = QRDecoder(image)
        self.assertEqual(decoder.get_first(), (DATA_TYPE_TEXT, 'Ver1'))

    def test_get_all(self):
        image = Image.open(self._get_res_path('Qr-1-noborder.png'))
        decoder = QRDecoder(image)
        self.assertEqual(decoder.get_all(), [(DATA_TYPE_TEXT, 'Ver1')])