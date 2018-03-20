def is_perm(str1, str2):
    if len(str1) != len(str2):
        return False
    
#    str1.sort()
#    str2.sort()

    return sorted(str1) == sorted(str2)

def is_perm2(str1, str2):
    if len(str1) != len(str2):
        return False

    frequency_table = {}

    # Create frequency table from first string
    for char in str1:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1
    print(frequency_table)
        
    # Subtract counts of character of second string
    for char in str2:
        if not char in frequency_table:
            return False
        else:
            frequency_table[char] -= 1
    
    # If not all the counts in the frequency table are zero, return False
    for char, count in frequency_table.items():
        if count != 0:
            return False
    else:
        return True

print(is_perm2("ball", "llab"))
