import io
import unittest
from unittest.mock import patch

import example


sample_data = io.BytesIO(b'''\
"IBM",91.1\r
"AA",13.25\r
"MSFT",27.72\r
\r
''')


class Tests(unittest.TestCase):
    @patch('example.func1')
    @patch('example.func2')
    def test1(self, mock2, mock1):
        x = 1
        example.func1(x)       # Uses patched example.func
        mock1.assert_called_with(x)

    def test2(self):
        x = 2
        with patch('example.func1') as mock1, \
                patch('example.func2') as mock2:
            example.func1(x)      # Uses patched example.func
            mock1.assert_called_with(x)

    def test3(self):
        x = 3
        p = patch('example.func1')
        mock_func = p.start()
        example.func1(x)
        mock_func.assert_called_with(x)
        p.stop()

    @patch('example.urlopen', return_value=sample_data)
    def test_dowprices(self, mock_urlopen):
        p = example.dowprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p,
                         {'IBM': 91.1,
                          'AA': 13.25,
                          'MSFT': 27.72})
