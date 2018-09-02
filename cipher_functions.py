# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:


def clean_message(message):
    ''' (str) -> str
    Returns a copy of the message that includes only its alphabetical
    characters, where each of those characters has been converted
    to uppercase.
    >>> clean_message ("h3_*(&ajjh")
    "hajjh"
    >>> clean_message ("kjkjll")
    "kjkjll
    '''
    # instantiate new string
    output_str = ""
    # traverse message
    for i in range(0, len(message)):
        # check if the character is in the alphabet
        if (message[i].isalpha()):
            # add it to the output string
            output_str += message[i].upper()
    # return the variable
    return output_str


def encrypt_letter(char, keystream):
    ''' (str,int) -> str
    Applies the keystream value to the character to
    encrypt the character, and return the result
    REQ: char in alphabet
    >>> encrypt_letter ('L',12)
    'X'
    '''
    # instatiate counter variable
    counter = 0
    # make list of the alphabet
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    # finde the index of the letter
    alpha_num = alphabet.index(char)
    # apply the encryption
    alpha_num += keystream
    alpha_num = alpha_num % 26
    # make the char the new encrypted letter
    char = alphabet[alpha_num]
    # return the encrypted letter
    return char


def decrypt_letter(char, keystream):
    ''' (str,int) -> str
    Applies the keystream value to the character to decrypt
    the character, and return the result
    REQ: char in alphabet
    >>>decrypt_letter('X',12)
    'L'
    '''
    # make list of alphabet
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    # instatiate number and counter variables
    counter = 0
    # find letter corresponding to keystrea
    alpha_num = alphabet.index(char)
    # subtract the keystream to get real letter
    alpha_num -= keystream
    # convert it back to a letter
    char = alphabet[alpha_num]
    # return the decrypted letter
    return char


def swap_cards(cards, index):
    ''' (list of int, int) -> NoneType
    Swaps the card at the index with the card that follows it.
    Deck is treated as circular: if the card at the index is on
    the bottom of the deck, swap that card with the top card
    REQ: index is in cards
    >>> cards = [1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,
    21,24,27,2,5,8,11,14,17,20,23,26]
    >>> swap_cards(cards,5)
    >>> print(cards)
    [1, 4, 7, 10, 16, 13, 19, 22, 25, 28, 3, 6, 9,
    12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> swap_cards(cards,0)
    >>> print(cards)
    [26, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9,
    12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 1]
    '''
    # check if they chose the top card
    if (index == 0):
        # make sure it switches with the bottom card
        cards[0], cards[len(cards) - 1] = cards[len(cards) - 1], cards[0]
    else:
        # just switch it with the previous card
        cards[index], cards[index - 1] = cards[index - 1], cards[index]


def move_joker_1(cards):
    ''' (list of int) -> NoneType
    Finds JOKER1 and swaps it with the card that follows it. Deck
    is still treated as circular
    REQ: deck contains JOKER1
    >>>cards =[26, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6,
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 1]
    >>>move_joker_1(cards)
    >>>print(cards)
    [26, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 2, 27, 5, 8, 11, 14, 17, 20, 23, 1]
    >>>cards = [26, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3,
    6, 9, 12, 15, 18, 21, 24, 2, 1, 5, 8, 11, 14, 17, 20, 23, 27]
    >>>move_joker_1(cards)
    >>>print(cards)
    [27, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 2, 1, 5, 8, 11, 14, 17, 20, 23, 26]
    '''
    # instatiate counter, moved boolean
    counter = 0
    moved = False
    # look through the list for joker 1
    while (not(moved)):
        # check if its the joker and first letter
        if (cards[counter] == JOKER1 and counter == len(cards) - 1):
            cards[0], cards[len(cards) - 1]\
                = cards[len(cards) - 1], cards[0]
            moved = True
        # check if its the joker
        elif (cards[counter] == JOKER1):
            # just switchem regularly
            cards[counter], cards[counter + 1]\
                = cards[counter + 1], cards[counter]
            moved = True
        counter += 1


def move_joker_2(cards):
    ''' (list) -> NoneType
    Finds JOKER2 and moves it two cards down. Deck
    is still treated as circular
    REQ: deck contains JOKER2
    >>>cards = [27, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3,
    6, 9, 12, 15, 18, 21, 24, 2, 1, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>move_joker_2(cards)
    >>>print (cards)
    [27, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 28, 9, 12, 15,
    18, 21, 24, 2, 1, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>cards = [27, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6,
    9, 12, 15, 18, 21, 24, 2, 1, 5, 8, 11, 14, 17, 20, 28, 26]
    >>>move_joker_2(cards)
    >>>print(cards)
    [28, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12,
    15, 18, 21, 24, 2, 1, 5, 8, 11, 14, 17, 20, 26, 27]
    '''
    # instatiate  counter, moved boolean
    counter = 0
    moved = False
    # look through the list for joker 1
    while (not(moved)):
        # check if its the joker and last letter
        if (cards[counter] == JOKER2 and counter == len(cards) - 1):
            # switch for circularity
            cards[counter], cards[0], cards[1]\
                = cards[0], cards[1], cards[counter]
            moved = True
        # check if its the joker and the second last letter
        elif (cards[counter] == JOKER2 and counter == len(cards) - 2):
            # switch for circularity
            cards[counter], cards[counter + 1], cards[0]\
                = cards[counter + 1], cards[0], cards[counter]
            moved = True
        # check if its the regular case
        elif (cards[counter] == JOKER2):
            # regular switch for every other case
            cards[counter], cards[counter + 1], cards[counter + 2]\
                = cards[counter + 1], cards[counter + 2], cards[counter]
            moved = True
        counter += 1


def triple_cut(cards):
    ''' (list) -> NoneType
    Cut the deck three times based on the locations of the Jokers
    REQ: deck contains JOKER1 and JOKER2
    >>>cards = [22, 4, 7, 10, 13, 16, 19, 28, 25, 23, 3,
    6, 9, 12, 15, 18, 21, 24, 2, 1, 5, 27, 11, 14, 17, 20, 26, 8]
    >>>triple_cut(cards)
    >>>print(cards)
    [11, 14, 17, 20, 26, 8, 28, 25, 23, 3, 6, 9, 12, 15,
    18, 21, 24, 2, 1, 5, 27, 22, 4, 7, 10, 13, 16, 19]
    '''
    # instantiate joker indexes
    i_joker1 = -1
    i_joker2 = -1
    # get indexes of 27 and 28
    for i in range(0, len(cards)):
        # check if its the first joker
        if ((cards[i] == JOKER1 or cards[i] == JOKER2) and i_joker1 < 0):
            # make the jokers index that index
            i_joker1 = i
        # check if its the second joker
        elif ((cards[i] == JOKER1 or cards[i] == JOKER2) and i_joker2 < 0):
            # make the jokers index that index
            i_joker2 = i
    # instantiate our holder list
    cut_cards = []
    # use some basic slicing, to make the list we want
    cut_cards = cards[i_joker2 + 1:len(cards)] + \
        cards[i_joker1:i_joker2 + 1]\
        + cards[0:i_joker1]
    # apply the new list one by one to mutate old list
    for i in range(0, len(cut_cards)):
        # make the elements at each index the same
        cards[i] = cut_cards[i]


def insert_top_to_bottom(cards):
    ''' (list) -> NoneType
    Look at the bottom card of the deck; move that many cards
    from the top of the deck to the bottom, inserting them
    just above the bottom card. Special case: if the bottom card
    is JOKER2, use JOKER1 as the number of cards.
    REQ: deck contains JOKER1 and JOKER2
    >>>cards = [11, 14, 17, 20, 26, 8, 28, 25, 23, 3, 6, 9, 12,
    15, 18, 21, 24, 2, 1, 5, 27, 22, 4, 7, 10, 13, 16, 19]
    >>>insert_top_to_bottom(cards)
    >>>print(cards)
    [5, 27, 22, 4, 7, 10, 13, 16, 11, 14, 17, 20, 26, 8, 28, 25,
    23, 3, 6, 9, 12, 15, 18, 21, 24, 2, 1, 19]
    >>>cards = [11, 14, 17, 20, 26, 8, 19, 25, 23, 3, 6, 9, 12,
    15, 18, 21, 24, 2, 1, 5, 27, 22, 4, 7, 10, 13, 16, 28]
    >>>insert_top_to_bottom(cards)
    >>>print(cards)
    [11, 14, 17, 20, 26, 8, 19, 25, 23, 3, 6, 9, 12, 15, 18,
    21, 24, 2, 1, 5, 27, 22, 4, 7, 10, 13, 16, 28]
    '''
    # get last element value
    last_element = cards[len(cards) - 1]
    # set our cutting variable
    cut_cards = []
    # check if we have 28 as last element
    if (not(last_element == JOKER2)):
        # just use slicing
        cut_cards = cards[last_element:len(cards) - 1]\
            + cards[0:last_element]\
            + [last_element]
        # different slicing sequence
    # apply the new list to the old one
    for i in range(0, len(cut_cards)):
        # make the elements the same in the old list
        cards[i] = cut_cards[i]


def get_card_at_top_index(cards):
    ''' (list) -> int
    Look at the top card. Using that value as an index, return the card
    in that deck and that index. Special case: if the top card is
    JOKER2, use JOKER1 as the index
    REQ: deck contains JOKER1 and JOKER2
    >>>get_card_at_top_index([1,2,3,4,5])
    2
    >>>get_card_at_top_index([28,45,4,5,6,7,7,7,7,7,7,7,7
    ,2,3,4,5,6,7,8,6,4,3,2,3,4,5,6,7,8,9,0])
    0
    '''
    # check if the top card is joker2
    if (cards[0] == JOKER2):
        index = cards[JOKER1]
    else:
        index = cards[cards[0]]
    return index


def get_next_value(cards):
    ''' (list) -> int
    Does all five steps of the algorithm. Returns the next
    potential keystream value
    REQ: deck contains JOKER1 and JOKER2
    >>>get_next_value([11, 14, 17, 20, 26, 8, 19, 25, 23, 3,
    6, 9, 12, 15, 18, 21, 24, 2, 1, 5, 27, 22, 4, 7, 10, 13, 16, 28])
    12
    '''
    # step 1 of the algorithm
    move_joker_1(cards)
    # step 2 of the algorithm
    move_joker_2(cards)
    # step 3 of the algorithm
    triple_cut(cards)
    # step 4 of the algorithm
    insert_top_to_bottom(cards)
    # step 5 of the alogrithm, apply keystream value
    keystream = get_card_at_top_index(cards)
    return keystream


def get_next_keystream_value(cards):
    ''' (list) -> int
    Repeats all five steps of the algorithm until a valid
    keystream value is produced
    REQ: deck contains JOKER1 and JOKER2
    >>>get_next_keystream_value([11, 14, 17, 20, 26, 8, 19, 25, 23, 3, 6,
    9, 12, 15, 18, 21, 24, 2, 1, 5, 27, 22, 4, 7, 10, 13, 16, 28])
    12
    '''
    # instantiate keystream variable
    keystream = 0
    # keep getting new values until its in between 1-26
    while not(keystream >= 1 and keystream <= 26):
        # assign a new keystream value using steps 1-5
        keystream = get_next_value(cards)
    # return the keystream value we found
    return keystream


def process_message(cards, message, action):
    ''' (list,str,str) -> str
    Return the encrypted or decrypted message. Note that the
    message might contain non-letters.
    REQ: action in {'e','d'}
    REQ: deck contains JOKER1 and JOKER2
    >>>cards = [11, 14, 17, 20, 26, 8, 19, 25, 23, 3, 6, 9, 12,
    15, 18, 21, 24, 2, 1, 5, 27, 22, 4, 7, 10, 13, 16, 28]
    >>>process_message(cards,"Hello","e")
    'TEQPL'
    >>>process_message(cards,"TTEED",'d')
    'HNDPF'
    '''
    message = clean_message(message)
    # instantiate blank word variable
    word = ""
    # check if we want to ecrypt
    if (action == 'e'):
        # encrypt the message letter by letter
        for i in message:
            # apply letters to variable
            word += encrypt_letter(i, get_next_keystream_value(cards))
    # check if we want to decrypt
    elif (action == 'd'):
        # decrypt message letter by letter
        for i in message:
            # apply letters to variable
            word += decrypt_letter(i, get_next_keystream_value(cards))
    # return the encrypted or decrypted word
    return word


def process_messages(cards, messages, action):
    ''' (list,list,str) -> list
    Return the list of encrypted or decrypted list of messages
    REQ: action in {'e','d'}
    REQ: deck contains JOKER1 and JOKER2
    >>>cards = [11, 14, 17, 20, 26, 8, 19, 25, 23, 3, 6, 9, 12,
    15, 18, 21, 24, 2, 1, 5, 27, 22, 4, 7, 10, 13, 16, 28]
    >>>messages = ["hello","john","man"]
    >>>process_messages(cards,messages,'e')
    ['TEQPL', 'MVUP', 'WMT']
    >>>process_messages(cards,messages,'d')
    ['GPNHL', 'ZDCJ', 'VFY']
    '''
    # make a new list to return
    return_list = []
    # use the process message function we already made
    for i in range(0, len(messages)):
        # call the function we made
        return_list.append(process_message(cards, messages[i], action))
    return return_list


def read_messages(file):
    ''' (file) -> list
    Read and return the contents of the file as a list of messages. Strip
    the newline form each line.
    '''
    # make a list of messages
    messages = file.readlines()
    # go through each element
    for i in messages:
        # get rid of the \n
        i = i.strip("\n")
    # close the file
    file.close()
    # return the new stripped list
    return messages


def read_deck(file):
    ''' (file) -> list
    Read and return the contents of the file. Returns
    all integers from the deck file
    '''
    # get the numbers in a string from the file
    nums = file.read()
    # make a list of the numbers
    num_list = nums.split()
    # convert all the numbers to ints
    for i in range(0, len(num_list)):
        # cast the value
        num_list[i] = int(num_list[i])
    # close the file
    file.close()
    # return the list
    return num_list
