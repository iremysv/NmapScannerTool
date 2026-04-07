import sys
import os
import unittest
from io import StringIO
from unittest.mock import patch

# Kod kapsamı için ana dizini dahil et
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from AnalizMotoru import analiz_et


class TestAnalizMotoru(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_analiz_et_bilinen_port(self, mock_stdout):
        analiz_et(["80", "443"])
        cikis = mock_stdout.getvalue()
        self.assertIn("HTTP", cikis)
        self.assertIn("HTTPS", cikis)

    @patch("sys.stdout", new_callable=StringIO)
    def test_analiz_et_bilinmeyen_port(self, mock_stdout):
        analiz_et(["9999"])
        cikis = mock_stdout.getvalue()
        self.assertIn("kritik bir yapılandırma önerisi bulunamadı", cikis)


if __name__ == "__main__":
    unittest.main()
