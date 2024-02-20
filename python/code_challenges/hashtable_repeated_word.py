import re
from collections import defaultdict

def first_repeated_word(s):
    # Remove punctuation and make lowercase
    cleaned = re.sub(r'[^\w\s]', ' ', s.lower())
    words = cleaned.split()
    
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
        if word_counts[word] > 1:
            return word
    return None
