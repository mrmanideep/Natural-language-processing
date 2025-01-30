class FiniteStateAutomaton:
    def __init__(self):
        self.state = 0

    def transition(self, char):
        if self.state == 0:
            if char == 'a':
                self.state = 1
            else:
                self.state = 0
        elif self.state == 1:
            if char == 'b':
                self.state = 2
            else:
                self.state = 0
        elif self.state == 2:
            self.state = 2

    def accepts(self, string):
        for char in string:
            self.transition(char)
        return self.state == 2

fsa = FiniteStateAutomaton()
test_strings = ["hello", "testab", "abab", "xyzab", "abc"]

for s in test_strings:
    if fsa.accepts(s):
        print(f"'{s}' ends with 'ab'")
    else:
        print(f"'{s}' does not end with 'ab'")
