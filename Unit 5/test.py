import sys


class DFA:
    def __init__(self, filepath=None, states=None, final=None, language=None):
        if states is None and final is None and language is None:
            self.states = {}
            self.final = []
            self._language = []
            with open(filepath) as f:
                lines = f.read()
            lines = lines.split("\n\n")
            nested = []
            for line in lines:
                nested.append(line.split("\n"))
            _language, _numnodes, _final = nested.pop(0)
            for line in nested:
                self.states[line[0]] = [
                    line[1:][x].split(" ") for x in range(len(line[1:]))
                ]
            # print("States: ", self.states)
            self.final = _final.split(" ")
            # print("Final States: ", self.final)
            self._language = list(_language)
        else:
            self.states = states
            self.final = final
            self._language = language

    def __str__(self):
        row0 = f"*\t" + "\t".join(self._language)
        for state in self.states:
            row = f"{state}\t"
            for char in self._language:
                # handle if there is no transition
                try:
                    row += f"{self.states[state][self._language.index(char)][0]}\t"
                except:
                    row += f"_\t"
            row0 += f"\n{row}"

        return row0

    def todict(self, entry):
        dict = {}
        for option in entry:
            dict[option[0]] = option[1]
        return dict

    def eval(self, string):
        current = "0"  # always a number
        for idx, char in enumerate(string):
            # look up char in dicitonary to see where to move next
            _state = self.states[current]
            curr_dict = self.todict(_state)
            if char in curr_dict.keys():
                current = curr_dict[char]
            else:
                return False
        return current in self.final


# dfa 1
states1 = {
    "0": [["a", "1"], ["b", "4"]],
    "1": [["a", "2"], ["b", "4"]],
    "2": [["a", "4"], ["b", "3"]],
    "3": [["a", "4"], ["b", "4"]],
    "4": [["a", "4"], ["b", "4"]],
}
final = ["3"]
language = ["a", "b"]
DFA1 = DFA(states=states1, final=final, language=language)

# dfa 2
states2 = {
    "0": [["0", "0"], ["1", "1"], ["2", "0"]],
    "1": [["0", "0"], ["1", "1"], ["2", "0"]],
}
final2 = ["1"]
language2 = ["0", "1", "2"]
DFA2 = DFA(states=states2, final=final2, language=language2)

# dfa 3
states3 = {
    "0": [["a", "0"], ["b", "1"], ["c", "0"]],
    "1": [["a", "1"], ["b", "1"], ["c", "1"]],
}
final3 = ["1"]
language3 = ["a", "b", "c"]
DFA3 = DFA(states=states3, final=final3, language=language3)

# dfa 4
states4 = {"0": [["0", "1"], ["1", "0"]], "1": [["0", "0"], ["1", "1"]]}
final4 = ["0"]
language4 = ["0", "1"]
DFA4 = DFA(states=states4, final=final4, language=language4)

# dfa 5
states5 = {
    "0": [["0", "1"], ["1", "2"]],
    "1": [["0", "0"], ["1", "3"]],
    "2": [["0", "3"], ["1", "0"]],
    "3": [["0", "2"], ["1", "1"]],
}
final5 = ["0", "3"]
language5 = ["0", "1"]
DFA5 = DFA(states=states5, final=final5, language=language5)

# dfa 6
states6 = {
    "0": [["a", "1"], ["b", "0"], ["c", "0"]],
    "1": [["a", "1"], ["b", "2"], ["c", "0"]],
    "2": [["a", "1"], ["b", "0"], ["c", "3"]],
    "3": [["a", "3"], ["b", "3"], ["c", "3"]],
}
final6 = ["0", "1", "2"]
language6 = ["a", "b", "c"]
DFA6 = DFA(states=states6, final=final6, language=language6)

# dfa 7
states7 = {
    "0": [["0", "1"], ["1", "0"]],
    "1": [["0", "2"], ["1", "1"]],
    "2": [["0", "2"], ["1", "3"]],
    "3": [["0", "2"], ["1", "4"]],
    "4": [["0", "4"], ["1", "4"]],
}
final7 = ["4"]
language7 = ["0", "1"]
DFA7 = DFA(states=states7, final=final7, language=language7)

DFAS = [DFA1, DFA2, DFA3, DFA4, DFA5, DFA6, DFA7]


if __name__ == "__main__":
    args = sys.argv[1:]
    try:
        num = int(args[0])
        mode = "TEST_DFA"
    except:
        mode = "EVAL_DFA"

    if mode == "EVAL_DFA":
        dfa = DFA(args[0])
        print(dfa)

        with open(args[1]) as f:
            lines = f.read()

        lines = lines.split("\n")
        for line in lines:
            print(dfa.eval(line), line)

    elif mode == "TEST_DFA":
        print(DFAS[num - 1])
        with open(args[1]) as f:
            lines = f.read()
        lines = lines.split("\n")
        for line in lines:
            print(DFAS[num - 1].eval(line), line)