from unittest import TestCase
from unittest.mock import patch, Mock

from server import index


class Test1(TestCase):

    @patch('server.render_template')
    def test_index(self, patched_render_template: Mock):
        patched_render_template.return_value = True
        index()
        patched_render_template.assert_called_once()
