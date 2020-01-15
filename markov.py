"""Generate Markov text from text files."""

#
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    opened_file = open(file_path)
    opened_file = opened_file.read()
    # print(opened_file)

    # your code goes here

    return opened_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")


    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]

    """
    words = text_string.split()

    chains = {}
   

    for i in range(len(words)-2):
        key = (words[i], words[i+1])
        value_item = words[i+2]
        # print(key)
        # print(value_item)

        # check for existence of key in idct
        # if key does not exist, set the value of the key in the dict as an empty list
        # if key exist, append the value item of the key to the list
        
        chains[key] = chains.get(key, []) + [value_item]
        

    # your code goes here
    # print(chains)
    return chains

def find_random_current_key(chains):

    # for i in range(len())

    current_key = choice(list(chains.keys()))

    print(current_key)

    return current_key


def make_text(chains):
    """Return text from chains."""

    words = []

    # current_key = choice(open_and_read_file(input_path))
    find_the_key = find_random_current_key(chains)
    # print(current_key)

    new_key_list = []

    # value_for_random_choice = chains[("Would", "you")]

    # random_v = choice(value_for_random_choice)

    # new_key = ((current_key)[1], random_v)

    # new_key = (current_key)[1], choice(chains[("Would", "you")])

    new_key = (find_the_key)[1], choice(chains[find_the_key])

    new_key_list.append(new_key)

    # print(words)

    while new_key in chains:

        new_key = (new_key)[1], choice(chains[new_key])
        
        new_key_list.append(new_key)

    # print(new_key_list)

    for word in new_key_list:
        
        words.append(word[0])

        # print("inner loop", words)

    words.append(word[1])

    # print("outer loop", words)

    # print(words)


    return " ".join(words)


input_path = "gettysburg.txt"


#Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# print(input_text)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
