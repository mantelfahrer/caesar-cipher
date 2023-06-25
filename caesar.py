# import
import sys


def encode_text(text: str, key: int):
    # check argument type
    if not isinstance(text, str):
        raise TypeError("The first argument must be of type String.")
    if not isinstance(key, int):
        raise TypeError("The second argument must be of type Integer.")

    # ensure the key is between 0 and 25
    key = key % 26

    # initialise empty string
    encodedString: str = ""
    # encode characters in string
    for character in text:
        # check if character is standard alphabetic letter
        if 65 <= ord(character) <= 90 or 97 <= ord(character) <= 122:
            if character.isupper():
                newOrd = ord(character) + key
                # lowest valid unicode for uppercase letter is 65
                if newOrd < 65:
                    newOrd = 90 - (65 - newOrd - 1)
                # highest valid unicode for uppercase letter is 90
                elif newOrd > 90:
                    newOrd = 65 + (newOrd - 90 - 1)
                # add encoded character to encoded text string
                encodedString += chr(newOrd)

            elif character.islower():
                newOrd = ord(character) + key
                # lowest valid unicode for lowercase letter is 97
                if newOrd < 97:
                    newOrd = 122 - (97 - newOrd - 1)
                # highest valid unicode for lowercase letter is 122
                elif newOrd > 122:
                    newOrd = 97 + (newOrd - 122 - 1)
                # add encoded character to encoded text string
                encodedString += chr(newOrd)

        # if character is not standard alphabetic letter add character to encoded text string unchanged
        else:
            encodedString += character

    return encodedString


def string_histogramm(text: str):
    # check argument type
    if not isinstance(text, str):
        raise TypeError("The argument must be of type String.")

    # initialise dictionary
    histogramm = dict()
    # lower case the text
    convertedText = text.lower()
    # populate histogramm for alphabetic characters included in text
    for character in convertedText:
        if character.isalpha():
            if character in histogramm:
                histogramm[character] += 1
            else:
                histogramm.update({character: 1})

    return histogramm


def frequencies(histogramm: dict):
    # check argument type
    if not isinstance(histogramm, dict):
        raise TypeError("The argument must be of type Dictionary.")

    # initialise variables
    frequencies = list()
    charactersTotalAmount = 0

    # add up amount of characters
    for value in histogramm.values():
        charactersTotalAmount += value
    # print("Total amount of characters in text:", charactersTotalAmount)
    # calculate percentage of every alphabetic character
    for i in range(ord('a'), ord('z')+1):
        if chr(i) in histogramm:
            frequencies.append(histogramm[chr(i)] / charactersTotalAmount)
        else:
            frequencies.append(0)

    return frequencies


def crack_caesar(text: str):
    # check argument type
    if not isinstance(text, str):
        raise TypeError("The argument must be of type String.")

    # initialise example text
    exampleText = '''I know that virtue to be in you, Brutus, As well as I do know your outward favour. Well, honour
    is the subject of my story. I cannot tell what you and other men Think of this life; but,
    for my single self, I had as lief not be as live to be In awe of such a thing as I myself. I was
    born free as Caesar; so were you: We both have fed as well, and we can both Endure the
    winter's cold as well as he: For once, upon a raw and gusty day, The troubled Tiber chafing
    with her shores, Caesar said to me 'Darest thou, Cassius, now Leap in with me into this angry
    flood, And swim to yonder point?' Upon the word, Accoutred as I was, I plunged in And
    bade him follow; so indeed he did. The torrent roar'd, and we did buffet it With lusty sinews,
    throwing it aside And stemming it with hearts of controversy; But ere we could arrive the
    point proposed, Caesar cried 'Help me, Cassius, or I sink!' I, as Aeneas, our great ancestor,
    Did from the flames of Troy upon his shoulder The old Anchises bear, so from the waves of
    Tiber Did I the tired Caesar. And this man Is now become a god, and Cassius is A wretched
    creature and must bend his body, If Caesar carelessly but nod on him. He had a fever when
    he was in Spain, And when the fit was on him, I did mark How he did shake: 'tis true, this
    god did shake; His coward lips did from their colour fly, And that same eye whose bend doth
    awe the world Did lose his lustre: I did hear him groan: Ay, and that tongue of his that bade
    the Romans Mark him and write his speeches in their books, Alas, it cried 'Give me some
    drink, Titinius,' As a sick girl. Ye gods, it doth amaze me A man of such a feeble temper
    should So get the start of the majestic world And bear the palm alone.'''

    # calculate probability vectors for each alphabetic character using example text
    probabilityVectorsExampleText = frequencies(string_histogramm(exampleText))

    # initialise key for encoding
    finalKey = 0
    listOfChiSquaredValues = []
    # for each of the 26 alphabetic characters try decoding with that letters number as key
    for i in range(1, 27):
        probabilityVectors = frequencies(string_histogramm(encode_text(text, i)))
        chiSquaredValues = []
        # compare probability vectors for each of the 26 alphabetic characters
        for j in range(0, 26):
            if probabilityVectorsExampleText[j] == 0:
                chiSquaredValues.append(0)
            else:
                chiSquaredValues.append(pow(
                    probabilityVectors[j] - probabilityVectorsExampleText[j], 2) / probabilityVectorsExampleText[j])
        # calculate average chi squared value for all probability vectors and add them to a list
        averageChiSquared = 0
        for k in chiSquaredValues:
            averageChiSquared += k
        averageChiSquared = averageChiSquared / 26
        listOfChiSquaredValues.append(averageChiSquared)
    # get smallest value of all average chi squared values
    finalKey = listOfChiSquaredValues.index(min(listOfChiSquaredValues)) + 1
    # encode text with final key
    crackedText = encode_text(text, finalKey)
    return crackedText


def main():
    try:
        # determine number of arguments passed
        argumentsLength = len(sys.argv)
        if argumentsLength < 3:
            raise RuntimeError("At least two arguments must be passed.")
        if argumentsLength > 3:
            raise RuntimeError("Passed too many arguments. A maximum of two arguments is permitted.")
        if argumentsLength == 3:
            # check if option was used
            if sys.argv[1] == "--crack" or sys.argv[1] == "-c":
                print("cracking encrypted text...")
                # crack caesar
                crackedText = crack_caesar(sys.argv[2])
                print(crackedText)
            elif sys.argv[1] == "--histogramm" or sys.argv[1] == "-h":
                print("creating histogramm for text")
                # create histogramm for text
                histogramm = string_histogramm(sys.argv[2])
                print(histogramm)
            elif sys.argv[1] == "--frequencies" or sys.argv[1] == "-f":
                print("calculating frequencies...")
                # create histogramm for text
                histogramm = string_histogramm(sys.argv[2])
                # determine frequency of characters in text
                histogrammFrequencies = frequencies(histogramm)
                print(histogrammFrequencies)
            else:
                print("encoding/decoding...")
                # convert key to integer
                try:
                    key = int(sys.argv[2])
                except:
                    raise TypeError("The key argument must be a whole number.")
                # encode text
                encodedText = encode_text(sys.argv[1], key)
                # print encoded text
                print(encodedText)

    except RuntimeError as e:
        print("Error:", e)
    except TypeError as e:
        print("TypeError:", e)


# execute main function
if __name__ == '__main__':
    main()
