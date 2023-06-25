# Caesar cipher

## Description

This is a small project that was created in the course of my studies at the university. It implements the caesar cipher in Python.

## How it works
The caesar cipher is a simple and very insecure method of encrypting a text. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter in a specified number of places down the alphabet. The number of places is determined by the key.

For example, the key is `3` and the text is 

`This is a secret message`

Then the text would be encrypted to 

`Wklv lv d vhfuhw phvvdjh`

The caesar cipher only works for ASCII characters, not for special characters, which will be taken over unchanged. Encryption of text is case sensitive.

## How to use
`python caesar.py [-c string/text | -f string/text | -h string/text] string/text key`

If used without options, a string/text and a key of type integer musst be passed as arguments. If options are used, no key is passed as argument.


### Options
The options are as follows:

Option | Description
--- | ----
--crack or -c *string/text* | Cracks the encrypted string/text and prints result
--frequence or -f *string/text* | Calculates and prints the frequencies of all letters of the alphabet for given string/text
--histogramm or -h *string/text* | Creates and prints histogramm for letters contained in given string/text

### Examples
The following example shows the output of caesar.py with the option ```-c``` cracking the encrypted text:
```
$ python caesar.py -c "Wklv lv d vhfuhw phvvdjh"
cracking encrypted text...
This is a secret message
```
The following example shows the output of caesar.py with the option ```-f``` calculating frequencies of letters:
```
$ python caesar.py -f "Wklv lv d vhfuhw phvvdjh"
calculating frequencies...
[0, 0, 0, 0.1, 0, 0.05, 0, 0.2, 0, 0.05, 0.05, 0.1, 0, 0, 0, 0.05, 0, 0, 0, 0, 0.05, 0.25, 0.1, 0, 0, 0]
```
The following example shows the output of caesar.py with the option ```-h``` creating a histogramm:
```
$ python caesar.py -h "Wklv lv d vhfuhw phvvdjh"
creating histogramm for text...
{'w': 2, 'k': 1, 'l': 2, 'v': 5, 'd': 2, 'h': 4, 'f': 1, 'u': 1, 'p': 1, 'j': 1}
```