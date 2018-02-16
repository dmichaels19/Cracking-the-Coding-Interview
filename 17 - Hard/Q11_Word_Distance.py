def find_word_distance(file_path, word1, word2):
    word1 = str.encode(word1)
    word2 = str.encode(word2)
    word1_min_index = -float('inf')
    word2_min_index = float('inf')
    word1_most_recent_index = None
    word2_most_recent_index = None
    min_distance = float('inf')
    curr_index = -1 # at first loop, curr_index will start at 0

    with open(file_path, 'rb') as large_file:
        # Will only read one line at a time. Buffering, etc works as expected.
        for line in large_file:
            for curr_word in line.split(b' '):
                curr_word = curr_word.rstrip(b'\n,.:')
                curr_word = curr_word.lower()
                curr_index += 1
                if word1 == curr_word:
                    word1_most_recent_index = curr_index
                elif word2 == curr_word:
                    word2_most_recent_index = curr_index
                else:
                    continue
                
                # If we haven't seen word1 or word2 yet, continue
                if not (word1_most_recent_index and word2_most_recent_index):
                    continue
                
                if abs(word1_most_recent_index - word2_most_recent_index) < min_distance:
                    word1_min_index = word1_most_recent_index
                    word2_min_index = word2_most_recent_index
                    min_distance = abs(word1_most_recent_index - word2_most_recent_index)
        return min_distance if min_distance != float('inf') else -1

print(find_word_distance('text.txt', 'the', 'array'))
