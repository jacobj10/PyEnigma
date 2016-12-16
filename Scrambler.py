class Scrambler():
    def __init__(self, initNum):
        self.scramblers = []
        self._dict = {}
        self._rev_dict = {}
        for i in range(0, 26):
            self.scramblers.append(i)
        self._setup(initNum)

    def _setup(self, initNum):
        self.scramblers = self.scramblers[initNum:len(self.scramblers)] + self.scramblers[0:initNum]
        for i in range(0, 26):
            self._dict[chr(i+65)]=chr(self.scramblers[i]+64)
            self._rev_dict[chr(self.scramblers[i]+64)]=chr(i+65)

    def increment(self):
        self.scramblers = self.scramblers[1:len(self.scramblers)] + [self.scramblers[0],]

    def letters(self):
        return [chr(letter + 65) for letter in self.scramblers]

    def __getitem__(self, n):
        return self.letters()[n]
