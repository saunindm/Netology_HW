import unittest

from secretary import add_new_doc, delete_doc, show_all_docs_info, documents
from unittest.mock import patch


fixture1 = [
    ('1234 567809', 'passport', 'Tom', '1'),
    ('32-3', 'invoice', 'Harry', '2'),
    ('45634', 'insurance', 'Ben', '3'),
    ('32-4', 'invoice', 'Osiris', '5')
]


class TestSecretary(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp ===> START TEST')

    @patch('builtins.input')
    def test_add_new_doc(self, mocked_input):
        mocked_input.side_effect = ['1234 567809', 'passport', 'Tom', '1']
        result = add_new_doc()
        self.assertEqual(result, '1')

    @patch('builtins.input')
    def test_add_new_doc1(self, mocked_input):
        mocked_input.side_effect = ['32-4', 'invoice', 'Osiris', '5']
        result = add_new_doc()
        self.assertEqual(result, '5')

    @patch('builtins.input')
    def test_delete_doc(self, mocked_input):
        mocked_input.return_value = '11-2'
        result, deleted = delete_doc()
        self.assertEqual(result, '11-2')
        self.assertTrue(deleted)

    def test_show_all_docs_info(self):
        result = show_all_docs_info()
        self.assertEqual(len(result), len(documents))

    def tearDown(self) -> None:
        print('tearDown ===> STOP TEST')
