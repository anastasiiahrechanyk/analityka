from collections import Counter

def firstUniqChar(s: str) -> int:

    freq = Counter(s)

    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1

if __name__ == "__main__":
    s1 = "leopard"
    print("Приклад 1:", firstUniqChar(s1))  

    s2 = "loveleopard"
    print("Приклад 2:", firstUniqChar(s2))  

    s3 = "aabb"
    print("Приклад 3:", firstUniqChar(s3)) 
