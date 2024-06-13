from collections import Counter

def magic(string):
    freq = Counter(string)
    max_freq = max(freq.values())
    min = len(string) - max_freq
    return min

string="aabbccdddd"
print(magic(string))




