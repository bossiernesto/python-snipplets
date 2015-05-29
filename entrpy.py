import math

def getFrequencyString(string):
    wordList=list(string)
    frequency = dict()
    for word in set(wordList):
        cnt = len([letter for letter in wordList if letter == word])
        frequency[word] = float(cnt) / len(wordList)
    return frequency

_entr = lambda val: val * math.log(val,2)
_entropy = lambda values: -sum(map(_entr, values))
_minBitEncoding = lambda entropy: int(math.ceil(entropy))
_entropyEfficiency= lambda values: -sum(map(lambda val: _entr(val)/math.log(len(values), 2), values))

st='abcddeefghijklmnopqrstuvwxyz1234567'
f=getFrequencyString(st)
print(getFrequencyString(st))
#{'1': 0.008849557522123894, '3': 0.008849557522123894, '2': 0.008849557522123894, '5': 0.008849557522123894, '4': 0.008849557522123894, '7': 0.6991150442477876, '6': 0.008849557522123894, 'a': 0.008849557522123894, 'c': 0.008849557522123894, 'b': 0.008849557522123894, 'e': 0.017699115044247787, 'd': 0.017699115044247787, 'g': 0.008849557522123894, 'f': 0.008849557522123894, 'i': 0.008849557522123894, 'h': 0.008849557522123894, 'k': 0.008849557522123894, 'j': 0.008849557522123894, 'm': 0.008849557522123894, 'l': 0.008849557522123894, 'o': 0.008849557522123894, 'n': 0.008849557522123894, 'q': 0.008849557522123894, 'p': 0.008849557522123894, 's': 0.008849557522123894, 'r': 0.008849557522123894, 'u': 0.008849557522123894, 't': 0.008849557522123894, 'w': 0.008849557522123894, 'v': 0.008849557522123894, 'y': 0.008849557522123894, 'x': 0.008849557522123894, 'z': 0.008849557522123894}
print(len(getFrequencyString(st)))
#33
print(_entropy(f.values()))
#2.37771277564
print(_entropyEfficiency(f.values()))
#0.471357455301
print(_minBitEncoding(_entropy(f.values())))
#3