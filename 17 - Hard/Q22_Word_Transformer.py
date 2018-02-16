from collections import deque

ALPHABET = [str.encode(ch) for ch in 'abcdefghijklmnopqrstuvwxyz']

def find_word_transformation_bread_first(word1, word2, dictionary):
    def word_distance(x, y):
        dist = 0
        for char1, char2 in zip(x,y):
            if char1 != char2:
                dist += 1
        return dist

    queue = deque()
    # An entry is the current word and the past modifications
    entry = (word1, (),)
    queue.append(entry)
    visited = set()
    visited.add(word1)

    while len(queue) > 0:
        curr_word, past = queue.popleft()
        print((curr_word, past))
        if curr_word == word2:
            return list(past) + [curr_word]
        
        for i in range(len(curr_word)):
            for char in ALPHABET:
                modified = curr_word[:i] + char + curr_word[i+1:]
                # If one character has been modified in this position, then they all have
                if modified in visited:
                    continue
                if modified in dictionary:
                    new_entry = (modified[:], tuple(list(past) + [curr_word]))
                    # print(new_entry)
                    queue.append(new_entry)
                    visited.add(modified)

    return -1

def create_dictionary_from_file(path, word_length = None):
    dictionary_set = set()
    with open(path, 'rb') as raw_words:
        for word in raw_words:
            # Checks that if we have a word length set, we add only proper length words
            if not word_length or len(word) - 2 == word_length:
                word = word.rstrip(b'\r\n')
                dictionary_set.add(word)
    return dictionary_set





    
######################################################################
from heapq import heappop, heappush

def find_word_transformation_with_heap(word1, word2, dictionary):
    def word_distance(x, y):
        dist = 0
        for char1, char2 in zip(x,y):
            if char1 != char2:
                dist += 1
        return dist

    heap = []
    # An entry is the current word and the past modifications
    entry = (word1, (),)
    heappush(heap, (word_distance(word1, word2), entry))
    visited = set()
    visited.add(word1)

    while len(heap) > 0:
        priority, entry = heappop(heap)
        print(entry)
        curr_word, past = entry
        if curr_word == word2:
            return list(past) + [curr_word]
        
        for i in range(len(curr_word)):
            for char in ALPHABET:
                modified = curr_word[:i] + char + curr_word[i+1:]
                # If one character has been modified in this position, then they all have
                if modified in visited:
                    continue
                if modified in dictionary:
                    new_past = tuple(list(past) + [curr_word])
                    new_entry = (modified, new_past)
                    # print(new_entry)
                    new_priority = word_distance(modified, word2) + len(new_past)
                    heappush(heap, (new_priority, new_entry))
                    visited.add(modified)

    return -1

######################################################################
FORWARD = True
BACKWARD = False

def find_word_transformation_bidirectional_bread_first(word1, word2, dictionary):
    def word_distance(x, y):
        dist = 0
        for char1, char2 in zip(x, y):
            if char1 != char2:
                dist += 1
        return dist

    # Init both queues
    queue = deque()

    # An entry is the current word and the past modifications
    entry1 = (word1, (), FORWARD)
    queue.append(entry1)
    entry2 = (word2, (), BACKWARD)
    queue.append((entry2))

    # Need to save the past paths of visited
    # TODO: Paths should be hashed and stored in a separate table so that the same paths aren't stored multiple times
    visited1 = {}
    visited1[word1] = ()
    visited2 = {}
    visited2[word2] = ()

    def try_next_word(queue, visited_self, visited_other, other_word):
        curr_word, past, direction = queue.popleft()
        print((curr_word, past))

        if curr_word == other_word:
            return list(past) + [curr_word]
        elif curr_word in visited_other:
            correct_path = list(past) + [curr_word] + list(reversed(visited_other[curr_word]))
            # Reverse the path if we start from word2
            if not is_forward(direction):
                correct_path.reverse()
            return correct_path
        for i in range(len(curr_word)):
            for char in ALPHABET:
                modified = curr_word[:i] + char + curr_word[i + 1:]
                # If one character has been modified in this position, then they all have
                if modified in visited_self:
                    continue
                if modified in dictionary:
                    new_past = tuple(list(past) + [curr_word])
                    new_entry = (modified[:], new_past, direction)
                    # print(new_entry)
                    queue.append(new_entry)
                    visited_self[modified] = new_past

    def is_forward(direction):
        # The last entry of the tuple determines whether it is forwards or backwards
        return direction


    while len(queue) > 0:
        if is_forward(queue[0][-1]):
            path = try_next_word(queue, visited_self=visited1, visited_other=visited2, other_word=word2)
            if path:
                return path
        else:
            path = try_next_word(queue, visited_self=visited2, visited_other=visited1, other_word=word1)
            if path:
                path.reverse()
                return path



    return -1


######################################################################


def find_word_transformation_starter(word1, word2):
    assert(len(word1) == len(word2))

    word_dictionary = create_dictionary_from_file('words_alpha.txt', word_length = len(word1))

    return find_word_transformation_bidirectional_bread_first(word1, word2, word_dictionary)

print(find_word_transformation_starter(b'hello', b'apple'))
