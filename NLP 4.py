class FiniteStateMachine:
    def __init__(self):
        self.rules = [
            ("s", "ses"),   # Words ending in 's' -> 'ses'
            ("x", "xes"),   # Words ending in 'x' -> 'xes'
            ("z", "zes"),   # Words ending in 'z' -> 'zes'
            ("sh", "shes"), # Words ending in 'sh' -> 'shes'
            ("ch", "ches"), # Words ending in 'ch' -> 'ches'
            ("y", "ies"),   # Words ending in 'y' -> 'ies'
        ]
    
    def pluralize(self, noun):
        for suffix, plural_suffix in self.rules:
            if noun.endswith(suffix):
                return noun[:-len(suffix)] + plural_suffix
        if noun.endswith("f"):
            return noun[:-1] + "ves"
        if noun.endswith("fe"):
            return noun[:-2] + "ves"
        return noun + "s"  # Default rule: add 's'

# Test cases
fsm = FiniteStateMachine()
test_nouns = ["cat", "dog", "bus", "box", "church", "baby", "leaf", "knife"]

for noun in test_nouns:
    print(f"Singular: {noun} -> Plural: {fsm.pluralize(noun)}")
