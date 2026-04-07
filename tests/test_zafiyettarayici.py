import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Kod kapsamı için ana dizini dahil et
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ZafiyetTarayici import zafiyet_tara


class TestZafiyetTarayici(unittest.TestCase):
    @patch("subprocess.run")
    def test_zafiyet_tara_basarili(self, mock_run):
        # Mock subprocess response
        mock_result = MagicMock()
        mock_result.stdout = "Vulnerability scan completed"
        mock_run.return_value = mock_result

        sonuc = zafiyet_tara("127.0.0.1")
        self.assertIn("Vulnerability scan completed", sonuc)
        mock_run.assert_called_once()

    @patch("subprocess.run", side_effect=Exception("Connection Failed"))
    def test_zafiyet_tara_hata(self, mock_run):
        sonuc = zafiyet_tara("127.0.0.1")
        self.assertIn("[-] Tarama sırasında hata oluştu", sonuc)
        self.assertIn("Connection Failed", sonuc)


if __name__ == "__main__":
    unittest.main()
