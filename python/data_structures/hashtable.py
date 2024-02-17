from .linked_list import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [LinkedList() for _ in range(self.size)]

    def _hash(self, key):
        """
        Hashes the key to a value within the table's range.
        """
        return sum(ord(char) for char in key) * 599 % self.size

    def set(self, key, value):
        """
        Stores the key/value pair in the hashtable.
        """
        index = self._hash(key)
        node = self._buckets[index].find(lambda item: item[0] == key)
        if node:
            node.value = (key, value)  # Update the value if key exists
        else:
            self._buckets[index].append((key, value))  # Append a new node otherwise

    def get(self, key):
        """
        Retrieves the value associated with the given key.
        """
        index = self._hash(key)
        node = self._buckets[index].find(lambda item: item[0] == key)
        if node:
            return node.value[1]  # Return the value part of the tuple
        return None

    def keys(self):
        """
        Returns a list of all unique keys in the hashtable.
        """
        keys = []
        for bucket in self._buckets:
            keys.extend([node.value[0] for node in bucket])
        return keys

    def display(self):
        """
        Utility method to display all key/value pairs in a bucket.
        This method is specifically created for testing internals and is not part of a typical hashtable interface.
        """
        all_items = []
        for bucket in self._buckets:
            all_items.extend([[node.value[0], node.value[1]] for node in bucket])
        return all_items

# Initialize a new hashtable
# Initialize a new hashtable
hashtable = Hashtable()

# Add some key-value pairs to the hashtable
hashtable.set("name", "John Doe")
hashtable.set("age", "timeless")
hashtable.set("occupation", "Software Engineer")

print("Items added to the hashtable.")
# Retrieve items by their keys
name = hashtable.get("name")
age = hashtable.get("age")

print(f"Name: {name}, Age: {age}")
# Attempt to retrieve a value using a non-existent key
location = hashtable.get("location")  # This key does not exist in the hashtable

if location is None:
    print("The key 'location' does not exist in the hashtable.")

# Add two items that are designed to hash to the same bucket
# Note: This depends on the specific hash function implementation and hashtable size
hashtable.set("key1", "This is the first victim")
hashtable.set("key2", "This is the second suspect")

# Both items should be retrievable despite the collision
item1 = hashtable.get("key1")
item2 = hashtable.get("key2")

print(f"Item 1: {item1}")
print(f"Item 2: {item2}")
