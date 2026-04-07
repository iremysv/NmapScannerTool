import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Kod kapsamı için ana dizini dahil et
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ScannerTool import nmap_calistir


class TestScannerTool(unittest.TestCase):
    @patch("ScannerTool.analiz_et")
    @patch("ScannerTool.rapor_yaz")
    @patch("subprocess.run")
    def test_nmap_calistir_ports(self, mock_run, mock_rapor, mock_analiz):
        # Mock subprocess response with open ports
        mock_result = MagicMock()
        mock_result.stdout = "80/tcp open http\n443/tcp open https"
        mock_run.return_value = mock_result

        sonuc = nmap_calistir(["nmap", "-F", "127.0.0.1"], "127.0.0.1", "hizli_tarama")

        # Check if the output is returned
        self.assertEqual(sonuc, "80/tcp open http\n443/tcp open https")

        # Check if reports and analysis are called
        mock_rapor.assert_called_once_with("127.0.0.1", sonuc)
        mock_analiz.assert_called_once_with(["80", "443"])

    @patch("ScannerTool.rapor_yaz")
    @patch("subprocess.run", side_effect=Exception("Nmap bulunamadı"))
    def test_nmap_calistir_hata(self, mock_run, mock_rapor):
        # We don't want to actually print error to terminal during tests
        with patch("builtins.print") as mock_print:
            sonuc = nmap_calistir(["nmap", "127.0.0.1"], "127.0.0.1", "test")
            self.assertIsNone(sonuc)
            mock_print.assert_any_call("[-] Hata oluştu: Nmap bulunamadı")


if __name__ == "__main__":
    unittest.main()
