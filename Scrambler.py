class Scrambler():
    def __init__(self, initNum):
        self.scramblers = []
        for i in range(0, 26):
            self.scramblers.append(i)
        self._setup(initNum)

    def _setup(self, initNum):
        self.scramblers = self.scramblers[initNum:len(self.scramblers)] + self.scramblers[0:initNum]

    def increment(self):
        self.scramblers = self.scramblers[1:len(self.scramblers)] + [self.scramblers[0],]

    def letters(self):
        return [chr(letter + 65) for letter in self.scramblers]

