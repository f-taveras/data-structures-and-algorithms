import pytest
from data_structures.hashtable import Hashtable

def test_exists():
    """
    Test to ensure the Hashtable class exists.
    """
    assert Hashtable

def test_get_apple():
    """
    Test setting a key/value and retrieving the value by key.
    """
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

def test_null_for_nonexistent_key():
    """
    Test retrieving a value with a key that does not exist returns None.
    """
    hashtable = Hashtable()
    result = hashtable.get("nonexistent")
    assert result is None

def test_unique_keys_list():
    """
    Test successfully returning a list of all unique keys in the hashtable.
    """
    hashtable = Hashtable()
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")
    keys = hashtable.keys()
    assert "key1" in keys and "key2" in keys and len(keys) == 2

def test_handle_collision():
    """
    Test handling a collision in the hashtable.
    """
    hashtable = Hashtable(10) # Use a smaller size for easier collision
    # These keys should result in a collision based on the hash function
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")
    assert hashtable.get("key1") == "value1"
    assert hashtable.get("key2") == "value2"

def test_retrieve_from_collision():
    """
    Test retrieving a value from a bucket within the hashtable that has a collision.
    """
    hashtable = Hashtable(10) # Ensuring collision
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")
    actual = hashtable.get("key2")
    expected = "value2"
    assert actual == expected

def test_hash_in_range():
    """
    Test hashing a key to an in-range value.
    """
    hashtable = Hashtable(1024)
    key = "somekey"
    index = hashtable._hash(key)
    assert 0 <= index < 1024

@pytest.mark.skip("Testing internals")
def test_internals():
    """
    Test to verify the internal structure and collision handling.
    """
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # Note: This uses a method not typically part of the hashtable's public interface
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]
    assert actual == expected

# Run the tests
if __name__ == "__main__":
    pytest.main()
