"""
Q122: Encode and Decode Strings
=================================
Problem: Design an algorithm to encode a list of strings to a single string,
then decode it back to the original list.

Example:
    ["hello","world"] -> encode -> decode -> ["hello","world"]
"""

def encode(strs):
    return ''.join(f"{len(s)}#{s}" for s in strs)

def decode(s):
    result, i = [], 0
    while i < len(s):
        j = s.index('#', i)
        length = int(s[i:j])
        result.append(s[j+1:j+1+length])
        i = j + 1 + length
    return result

if __name__ == "__main__":
    strs = ["hello","world","foo","bar"]
    encoded = encode(strs)
    print("Encoded:", encoded)
    print("Decoded:", decode(encoded))  # ["hello","world","foo","bar"]
    
    edge = ["", "with#hash", "123"]
    print("Edge decoded:", decode(encode(edge)))
