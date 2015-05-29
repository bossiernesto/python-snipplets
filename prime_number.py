class PrimeNumberList(object):

    def __init__(self, longitude):
        self.longitude = longitude
        self.array = bytearray(longitude)

    def iterateValues(self):
        for value in range(2, self.longitude):
            i=2
            while i*value <= self.longitude-1:
                self.array[i*value] = 1
                i += 1

    def generateResults(self):
        self.iterateValues()
        return [i for i in range(len(self.array)) if self.array[i] == 0][-1:]

    def getLargestPrime(self):
        ret = 1
        self.iterateValues()
        for i in range(len(self.array)):
            if self.array[i] == 0:
                ret = i
        return ret

a = PrimeNumberList(2**25) #largestPrime 2^25 33.554.393
print(a.generateResults())