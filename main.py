def is_identificator(token):
    characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z", "_"]
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    token = token.strip()
    ok = 0
    if len(token) >= 250:
        ok += 1
    for c in range(0, len(token)):
        if token[c] not in characters and token[c] not in digits:
            ok += 1
        if c == 0 and token[c] in digits:
            ok += 1
        if token[c] in digits and token[-1] in characters:
            ok += 1
        if "_" in token:
            if token[-1] == "_":
                ok += 1
            if token[c] in digits:
                ok += 1
    if ok == 0:
        return True


def is_const_caracter(token):
    characters = {'\'A\'',
                  '\'B\'',
                  '\'C\'',
                  '\'D\'',
                  '\'E\'',
                  '\'F\'',
                  '\'G\'',
                  '\'H\'',
                  '\'I\'',
                  '\'J\'',
                  '\'K\'',
                  '\'L\'',
                  '\'M\'',
                  '\'N\'',
                  '\'O\'',
                  '\'P\'',
                  '\'Q\'',
                  '\'R\'',
                  '\'S\'',
                  '\'T\'',
                  '\'U\'',
                  '\'V\'',
                  '\'W\'',
                  '\'X\'',
                  '\'Y\'',
                  '\'Z\'',
                  '\'_\'',
                  }

    digits = ['\'0\'',
              '\'1\'',
              '\'2\'',
              '\'3\'',
              '\'4\'',
              '\'5\'',
              '\'6\'',
              '\'7\'',
              '\'8\'',
              '\'9\'',
              ]
    token = token.strip()
    ok = 0
    if token not in characters and token not in digits:
        done = False
        for litera in characters:
            if token == litera.lower():
                done = True
        if not done:
            ok += 1
    if ok == 0:
        return True


def is_const_string(token):
    characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z", "_", '"']
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    token = token.strip()
    ok = 0
    for c in range(len(token)):
        if c == 0 and token[c] != '"':
            ok += 1
        if c == len(token) and token[c] != '"':
            ok += 1
        if token[c].upper() not in characters and token[c] not in characters and token[c] not in digits:
            ok += 1
    if token[-1] != '"' or token[0] != '"':
        ok += 1
    if ok == 0:
        return True


def is_const_intreg(token):
    token = token.strip()
    ok = 0
    if token[0] == "0" and len(token) != 1:
        ok += 1
    if token[0] == "-" or token[0] == "+":
        if len(token) == 2 and token[1] == "0":
            ok += 1
        token = token[1:]
    if not token.isdigit():
        ok += 1
    if ok == 0:
        return True


def main():
    codificare = {"identifier": 0,
                  "constant": 1,
                  "char": 2,
                  "list": 3,
                  "of": 4,
                  "varriable": 5,
                  "INTEGER": 6,
                  "CHAR": 7,
                  "BOOLEAN": 8,
                  "REAL": 9,
                  "START": 10,
                  "FINISH": 11,
                  "read": 12,
                  "write": 13,
                  "waitwhile": 14,
                  "solution": 15,
                  "dosomething": 16,
                  "if": 17,
                  "then": 18,
                  "else": 19,
                  "AND": 20,
                  "OR": 21,
                  "NOT": 22,
                  ":": 23,
                  ";": 24,
                  ",": 25,
                  ".": 26,
                  "+": 27,
                  "*": 28,
                  "-": 29,
                  "%": 30,
                  "(": 31,
                  ")": 32,
                  "[": 33,
                  "]": 34,
                  "_": 35,
                  "<": 36,
                  ">": 37,
                  "=": 38,
                  ":=": 39,
                  "<=": 40,
                  ">=": 41,
                  "/": 43,
                  " ": 44,
                  "+=": 45
                  }

    identificators = []
    constants = []
    separators = ["[", "]", ":", ";", " ", "(", ")", "."]
    operators = ["+", "-", "*", "/", ":=", "<", "<=", "=", ">=", ">", "!=", "%", "+="]
    reserved_words = ["list", "char", "dosomething", "else", "if", "int", "of", "solution", "read", "then",
                      "varriable", "waitwhile", "write", "START", "FINISH"]

    erori = []
    ts = []
    fip = []
    fip1 = []
    i = 1
    with open("file.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(" ")
            for token in line:
                token = token.strip()
                if is_identificator(token) and token not in reserved_words:
                    identificators.append(token)
                    exista = 0
                    for el in range(len(ts)):
                        if ts[el][1] == token:
                            exista = ts[el][0]
                    if exista != 0:
                        fip.append((0, exista))
                        fip1.append((token, exista))
                    else:
                        ts.append((i, token))
                        fip.append((0, i))
                        fip1.append((token, i))
                        i += 1
                elif is_const_intreg(token) or is_const_caracter(token) or is_const_string(token):
                    constants.append(token)
                    exista = 0
                    for el in range(len(ts)):
                        if ts[el][1] == token:
                            exista = ts[el][0]
                    if exista != 0:
                        fip.append((1, exista))
                        fip1.append((token, exista))
                    else:
                        ts.append((i, token))
                        fip.append((1, i))
                        fip1.append((token, i))
                        i += 1
                elif token in reserved_words:
                    fip.append((codificare[token], "-1"))
                    fip1.append((token, "-1"))
                elif token in operators:
                    fip.append((codificare[token], "-1"))
                    fip1.append((token, "-1"))
                elif token in separators:
                    fip.append((codificare[token], "-1"))
                    fip1.append((token, "-1"))
                elif "(" in token:
                    if "read" in token:
                        fip.append((codificare["read"], "-1"))
                        fip1.append(("read", "-1"))

                        fip.append((codificare["("], "-1"))
                        fip1.append(("(", "-1"))

                        for el in range(len(ts)):
                            if ts[el][1] == token[5:-1]:
                                fip.append(("0", ts[el][0]))
                                fip1.append((token[5:-1], ts[el][0]))

                        fip.append((codificare[")"], "-1"))
                        fip1.append((")", "-1"))
                    elif "write" in token:
                        fip.append((codificare["write"], "-1"))
                        fip1.append(("write", "-1"))

                        fip.append((codificare["("], "-1"))
                        fip1.append(("(", "-1"))

                        for el in range(len(ts)):
                            if ts[el][1] == token[6:-1] and token[6:-1] in constants:
                                fip.append(("1", ts[el][0]))
                                fip1.append((token[6:-1], ts[el][0]))
                            elif ts[el][1] == token[6:-1] and token[6:-1] in identificators:
                                fip.append(("0", ts[el][0]))
                                fip1.append((token[6:-1], ts[el][0]))

                        fip.append((codificare[")"], "-1"))
                        fip1.append((")", "-1"))
                    elif "write" in token:
                        fip.append((codificare["write"], "-1"))
                        fip1.append(("write", "-1"))

                        fip.append((codificare["("], "-1"))
                        fip1.append(("(", "-1"))

                        for el in range(len(ts)):
                            if ts[el][1] == token[6:-1]:
                                fip.append(("0", ts[el][0]))
                                fip1.append((token[6:-1], ts[el][0]))

                        fip.append((codificare[")"], "-1"))
                        fip1.append((")", "-1"))
                    else:
                        item = token.split("(")

                        if is_identificator(item[0]) and item[0] not in reserved_words:
                            identificators.append(item[0])
                            exista = 0
                            for el in range(len(ts)):
                                if ts[el][1] == item[0]:
                                    exista = ts[el][0]
                            if exista != 0:
                                fip.append((0, exista))
                                fip1.append((item[0], exista))
                            else:
                                ts.append((i, item[0]))
                                fip.append((0, i))
                                fip1.append((item[0], i))
                                i += 1

                        fip.append((codificare["("], "-1"))
                        fip1.append(("(", "-1"))

                        if is_identificator(item[1][:-1]) or is_const_intreg(item[1][:-1]) and item[1][:-1] not in \
                                reserved_words:
                            constants.append(item[1][:-1])
                            exista = 0
                            for el in range(len(ts)):
                                if ts[el][1] == item[1][:-1]:
                                    exista = ts[el][0]
                            if exista != 0:
                                fip.append((1, exista))
                                fip1.append((item[1][:-1], exista))
                            else:
                                ts.append((i, item[1][:-1]))
                                fip.append((1, i))
                                fip1.append((item[1][:-1], i))
                                i += 1

                        if item[1][-1] == ")":
                            fip.append((codificare[")"], "-1"))
                            fip1.append((")", "-1"))

                elif "[" in token:
                    if token[:4] == "list" and token[4] == "[":
                        fip.append((codificare["list"], "-1"))
                        fip1.append(("list", "-1"))
                        fip.append((codificare["["], "-1"))
                        fip1.append(("[", "-1"))
                    if is_const_intreg(token[5:-1]):
                        exista = 0
                        for el in range(len(ts)):
                            if ts[el][1] == token[5:-1]:
                                exista = ts[el][0]
                        if exista != 0:
                            fip.append((1, exista))
                            fip1.append((token[5:-1], exista))
                        else:
                            ts.append((i, token[5:-1]))
                            fip.append((1, i))
                            fip1.append((token[5:-1], i))
                            i += 1
                    if token[-1] == "]":
                        fip.append((codificare["]"], "-1"))
                        fip1.append(("]", "-1"))
                else:
                    erori.append(token)


    print("----------------------FIP--------------------------")
    for el in fip:
        print("{:<30} {:<10}".format(el[0], el[1]))
    print("----------------------TS---------------------------")
    for el in ts:
        print("{:<30} {:<10}".format(el[0], el[1]))
    print("----------------ERORI LEXICALE---------------------")
    for el in erori:
        print(el)


main()
