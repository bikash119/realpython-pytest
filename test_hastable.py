import pytest
from pytest_unordered import unordered
from hashtable import HashTable,BLANK

# Prepare data that can be used by testcases
@pytest.fixture
def hash_table():
    sample_data = HashTable(size=100)
    sample_data['hello']='hola'
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data

def test_should_always_pass():
    assert 2+2 == 4, "This is a dummy test"

def test_should_create_hashtable():
    assert HashTable(size=100) is not None

# How __len__ method of HashTable class
# is mapped to len() function
def test_should_report_length_of_empty_hash_table():
    assert len(HashTable(size=100)) == 0

def test_should_create_empty_value_slots():
    ## Testing internal implementation : Whitebox Testing
    assert HashTable(size=3)._pairs == [None,None,None]

def test_should_store_key_and_pairs():
    myhashtable = HashTable(size=100)
    myhashtable['BDFL']="hello"
    myhashtable[43]=43
    myhashtable[False]=True

    assert ('BDFL',"hello") in myhashtable.pairs
    assert (43,43) in myhashtable.pairs
    assert (False,True) in myhashtable.pairs
def test_should_insert_none_value(hash_table):
    hash_table["key"] = None
    assert("key",None) in hash_table.pairs

def test_should_not_increase_when_adding_elements(hash_table):
    assert hash_table.capacity == 100
    hash_table['add'] = 1
    assert hash_table.capacity == 100


def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(size=100).values


def test_should_find_value_by_key(hash_table):
    assert hash_table["hello"] == 'hola'
    assert hash_table[False] is True
    assert hash_table[98.6] == 37

def test_should_raise_error_on_missing_key(hash_table):
    with pytest.raises(KeyError) as exception_info:
        hash_table['missing_key']
    assert exception_info.value.args[0] == "missing_key"

def test_should_find_key(hash_table):
    assert "hello" in hash_table

# how __contains__ is mapped to in keyword?
def test_should_not_find_key(hash_table):
    assert "missing_key" not in hash_table

def test_should_get_value(hash_table):
    assert hash_table.get("hello") == "hola"

def test_should_none_when_missing_key(hash_table):
    assert hash_table.get("missing_key") is None

def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get("missing_key","default") == "default"

def test_should_get_value_with_default(hash_table):
    assert hash_table.get("hello","default") == "hola"

def test_should_delete_key_value_pair(hash_table):
    assert "hello" in hash_table
    assert ("hello","hola") in hash_table.pairs
    assert len(hash_table) == 3
    
    del hash_table["hello"]
    assert "hello" not in hash_table
    assert ("hello","hola") not in hash_table.pairs
    assert len(hash_table) == 2

# This decorator allows us to skip a test 
# during testcase execution
#@pytest.mark.skip
def test_should_not_shrink_when_removing_elements(hash_table):
    assert hash_table.capacity == 100
    del hash_table[False]
    assert hash_table.capacity == 100

def test_should_raise_key_error_when_deleting(hash_table):
    with pytest.raises(KeyError) as exception_info:
        del hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

def test_should_update_value(hash_table):
    assert hash_table["hello"] == "hola"

    hash_table["hello"] = "hajime"
    assert hash_table["hello"] == "hajime"
    assert hash_table[98.6] == 37
    assert hash_table[False] == True
    assert len(hash_table) == 3

def test_should_return_pairs(hash_table):
    assert ("hello","hola") in hash_table.pairs
    assert (98.6,37) in hash_table.pairs
    assert (False,True) in hash_table.pairs

def test_should_return_copy_of_pairs(hash_table):
    assert hash_table.pairs is not hash_table.pairs

def test_should_not_include_blank_pairs(hash_table):
    assert None not in hash_table.pairs

def test_should_return_duplicate_values():
    hash_table = HashTable(size=100)
    hash_table["Alice"]=42
    hash_table["Bob"]=42
    hash_table["Joe"]=42
    assert [42,42,42] == sorted(hash_table.values)

def test_should_get_values(hash_table):
    assert unordered(hash_table.values) == [True,37,"hola",]

def test_should_get_values_of_empty_hash_table():
    assert HashTable(size=100).values == []

def test_should_return_copy_of_values(hash_table):
    assert hash_table.values is not hash_table.values

def test_should_get_keys(hash_table):
    assert hash_table.keys == {98.6,False,"hello",}

def test_should_get_keys_of_empty_hash_table():
    assert HashTable(size=100).keys == set()

def test_should_return_copy_of_keys(hash_table):
    assert hash_table.keys is not hash_table.keys

def test_should_return_pairs(hash_table):
    assert hash_table.pairs == {
         ("hello","hola")
        ,(98.6,37)
        ,(False,True)
    }
def test_should_get_pairs_of_empty_hash_table():
    assert HashTable(size=100).pairs == set()

def test_should_convert_to_dict(hash_table):
    dictionary = dict(hash_table.pairs)
    assert set(dictionary.keys()) == hash_table.keys
    assert set(dictionary.items()) == hash_table.pairs
    assert list(dictionary.values()) == unordered(hash_table.values)

def test_should_not_create_hashtable_with_zero_capacity():
    with pytest.raises(ValueError):
        HashTable(size=0)

def test_should_not_create_hashtable_with_negative_capacity():
    with pytest.raises(ValueError):
        HashTable(size=-100)

def test_should_report_capacity_of_empty_hash_table():
    assert HashTable(size=100).capacity == 100

def test_should_report_capacity(hash_table):
    assert hash_table.capacity == 100



