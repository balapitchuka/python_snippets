import pytest
from phonebook import PhoneBook


@pytest.fixture
def phonebook():
    return PhoneBook()


def test_lookup_by_name(phonebook):
    phonebook.add('bob', '12345')
    assert phonebook.lookup('bob') == '12345'


def test_missing_key_raises_error(phonebook):
    phonebook = PhoneBook()
    with pytest.raises(KeyError):
        phonebook.lookup('missing')
