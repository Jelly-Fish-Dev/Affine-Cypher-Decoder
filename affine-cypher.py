import time

test_str = ["NLWC WC M NECN", "YEQ LKCV BDK XCGK EZ BDK UEXLVM QPLQGWSKMB", "NH WRTEQ TFWRX TGY T YEZVXH GJNMGRXX STPGX NH XRGXR TX QWZJDW ZK WRNUZFB P WTY YEJGB ZE RNSQPRY XZNR YJUU ZSPTQR QZ QWR YETPGX ZGR NPGJQR STXQ TGY URQWR VTEYX WTY XJGB"]
test_solution_str = ["this is a test", "my heart aches and a drowsy numbness pains my sense as though of hemlock i had drunk or emptied some dull opiate to the drains one minute past and lethe wards had sunk",]

with open("enable1.txt") as f:
    d = set(map(lambda s: s.strip().lower(), f.readlines()))
    d.update(['a', 'i'])

def Affine (input):
    input_number_arr = []
    for char in input:
        if char != " ":
            input_number_arr.append(ord(char.lower()) - 96)
        else:
            input_number_arr.append(0)
    solution = _Decode(input_number_arr)
    return solution

def _Decode(input):
    str_out = ""
    for a in range(1, 20):
        for b in range(1,20):
            for letter in input:
                if letter != 0:
                    str_out = str_out + chr((((letter * a) + b) % 26) + 96)
                else:
                    str_out = str_out + " "
            if _spellcheck(str_out):
                return str_out
            str_out = ""
        
def _spellcheck(word_str):
    words = word_str.split()
    correct = 0
    for word in words:
        if any(word == a for a in d ):
            correct += 1
            print(word)
        else:
            return
    if correct == len(words):
        return True


print("Input text: {}".format(test_str[2]))
start = time.time()
print(Affine(test_str[2]))
end = time.time()
print("Decoding too {} seconds".format(end-start))
