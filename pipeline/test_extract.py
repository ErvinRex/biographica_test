"""
Python script for testing extract functions
"""

import unittest
from unittest.mock import patch, mock_open, MagicMock

from extract import (get_gff_file_link, download_gff_file, get_meta_data, get_gff_data)

class TestGFFFunctions(unittest.TestCase):

    @patch('requests.get')
    def test_get_gff_file_link(self, mock_get):
        """
        Test that the gff file link returns
        correctly for int or string parameter request
        """
        mock_response = MagicMock()
        mock_response.text = '''
        <a href="file1.gtf.gz">file1.gtf.gz</a>
        <a href="file2.gtf.gz">file2.gtf.gz</a>
        '''
        mock_get.return_value = mock_response

        result = get_gff_file_link(42, 'beta_vulgaris')
        self.assertIn('file1.gtf.gz', result)

        result = get_gff_file_link('pre', 'hordeum_vulgare')
        self.assertIn('file1.gtf.gz', result)

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_download_gff_file(self, mock_file, mock_get):
        mock_response = MagicMock()
        mock_response.content = 'Some binary content'
        mock_get.return_value = mock_response

        download_gff_file('http://example.com/file.gtf.gz')
        mock_file.assert_called_once_with('temp_gff.gz', 'wb')
        mock_file().write.assert_called_once_with('Some binary content')