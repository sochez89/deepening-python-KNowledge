# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "goat") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    sort_str1 = sorted(word)
    sort_str2 = sorted(anagram)
    if sort_str1 == sort_str2:
        return True
    else:
        return False
    #print out to check whether hello and goat are anagram. if they are are not, it will output False, otherwise it will ouput True
print(find_anagram("hello", "goat"))
    #print out to check whether elbow and below are anagram, if they are, it will output True, otherwise it will ouput False.
print(find_anagram("elbow", "below"))

