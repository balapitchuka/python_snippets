import unittest
from phonebook import PhoneBook


class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = PhoneBook()

    def tearDown(self):
        pass

    def test_lookup_by_name(self):
        self.phonebook.add('bob', "12345")
        number = self.phonebook.lookup('bob')
        self.assertEqual(number, '12345')

    def test_lookup_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add('bob', '12345')
        self.phonebook.add('blue', '23456')
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_duplicate_entries(self):
        self.phonebook.add('bob', '12345')
        self.phonebook.add('blue', '12345')
        self.assertFalse(self.phonebook.is_consistent())

    def test_is_consistent_with_duplicate_prefix(self):
        self.phonebook.add('bob', '12345')
        self.phonebook.add('blue', '1234')
        self.assertFalse(self.phonebook.is_consistent())

    @unittest.SkipTest
    def test_skip_test_example(self):
        """This testcase is skipped because of decorator"""
        pass
