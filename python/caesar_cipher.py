from collections import deque # this function allows you to rotate a list

def caesar_cipher(sentence, shift_amount):
    copy = sentence.upper()
    indexes = []
    shifter = []
    shift_amount_counter = 0
    uppercase = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  
    # tries to find the index of each letter in sentence and convert it to the same index of uppercase
    # if it's not a letter it just passes the value instead
    for i in range(len(copy)):
        same = copy[i]
        try:
            if uppercase.index(same) == -1:
                indexes.append(copy[i])
            else:
                indexes.append(uppercase.index(same))
        except ValueError:
            indexes.append(copy[i])

    if shift_amount > 0:
        while shift_amount_counter != shift_amount:
            uppercase = deque(uppercase)
            uppercase.rotate(-1)
            uppercase = list(uppercase)
            shift_amount_counter += 1
    else:
        while shift_amount_counter != shift_amount:
            uppercase = deque(uppercase)
            uppercase.rotate(1)
            uppercase = list(uppercase)
            shift_amount_counter -= 1

    # this matches the index of letters in sentence to the new indexes of upper and returns that letter
    for i in range(len(indexes)):
        try:
            if sentence[i] == sentence[i].lower():
                shifter.append(str(uppercase[indexes[i]].lower()))
            else:
                shifter.append(uppercase[indexes[i]])
        except TypeError:
                shifter.append([indexes[i]])
    result = ''.join(''.join(l) for l in shifter) # necessary to join a non-string valued list
    return result
