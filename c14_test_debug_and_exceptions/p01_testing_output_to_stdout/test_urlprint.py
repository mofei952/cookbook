from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import urlprint


class TestURLPrint(TestCase):
    def test_url_gets_to_output(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            urlprint.urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)


# cd c14_test_debug_and_exceptions\p01_testing_output_to_stdout
# python -m unittest