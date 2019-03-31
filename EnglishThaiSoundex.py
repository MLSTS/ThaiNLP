#define group
t1 = "กขคฆ"
t2 = "ง"
t3 = "จฉฌชซศษสฎดฏตฐฑฒถทธ"
t4 = "ญย"
t5 = "ณนรลฬ"
t6 = "บปผพภฝฟ"
t7 = "ม"
t8 = "ว"
t0 = "ฅฃฮอฦฤห"
tspecial = "ๅุูึๆไำะัํี๊ฯโ็้เา.ฺิ์ืใ?"

e1 = "BbFfPpVv"
e2 = "CcGgJjKkQqSsXxZz"
e3 = "DdTt"
e4 = "Ll"
e5 = "MmNn"
e6 = "Rr"
e0 = "AaEeIiOoUuHhWwYy"
especial = "?"

#define Thai word
Thai = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t0 + tspecial
English = e1 + e2 + e3 + e4 + e5 + e6 + e0 + especial

def Soundex(word):
    print("--------------------")
    print("Original spilt word: ", word)
    #define variable
    i = 0
    char = ''
    Soundex = []
    ThaiCharinEnglishWord = ""
    EnglishCharinThaiWord = ""
    if word[0] in Thai:
        Soundex.append(word[0]) #Append First Character
        for char in word[1:]:
            if char in t1:
                Soundex.append(1)
            elif char in t2:
                Soundex.append(2)
            elif char in t3:
                Soundex.append(3)
            elif char in t4:
                Soundex.append(4)
            elif char in t5:
                Soundex.append(5)
            elif char in t6:
                Soundex.append(6)
            elif char in t7:
                Soundex.append(7)
            elif char in t8:
                Soundex.append(8)
            elif char in t0:
                Soundex.append(0)
            elif char in tspecial:
                Soundex.append(0)
            else:
                if char in English:
                    print("English character detected: ", char)
                    print("Attempt to soundex and seperate English character.")
                    EnglishCharinThaiWord += char
                else:
                    print("Unknown character: ", char)
                    print("Program terminated.")
                    return -1
        print("English Character: ", EnglishCharinThaiWord)
        print("Non-normalize soundex: ", Soundex)

        while i < len(Soundex):
            try:
                if Soundex[i] == Soundex[i+1]:
                    Soundex.pop(i+1)
                    i -= 1
                if Soundex[i] == 0:
                    Soundex.pop(i)
                    i -= 1
                i += 1
            except IndexError:
                break

        if(len(Soundex) > 4):
            Soundex = Soundex[0:4]
    
        while len(Soundex) < 4:
            Soundex.append(0)

        return Soundex
    
    elif word[0] in English:
        Soundex.append(word[0]) #Append First Character
        for char in word[1:]:
            if char in e1:
                Soundex.append(1)
            elif char in e2:
                Soundex.append(2)
            elif char in e3:
                Soundex.append(3)
            elif char in e4:
                Soundex.append(4)
            elif char in e5:
                Soundex.append(5)
            elif char in e6:
                Soundex.append(6)
            elif char in e0:
                Soundex.append(0)
            elif char in especial:
                Soundex.append(0)
            else:
                if char in Thai:
                    print("Thai character detected: ", char)
                    print("Attempt to soundex and seperate Thai character.")
                    ThaiCharinEnglishWord += char
                else:
                    print("Unknown character: ", char)
                    print("Program terminated.")
                    return -1
        print("Thai Character: ", ThaiCharinEnglishWord)
        print("Non-normalize soundex: ", Soundex)

        while i < len(Soundex):
            try:
                if Soundex[i] == Soundex[i+1]:
                    Soundex.pop(i+1)
                    i -= 1
                if Soundex[i] == 0:
                    Soundex.pop(i)
                    i -= 1
                i += 1
            except IndexError:
                break

        if(len(Soundex) > 4):
            Soundex = Soundex[0:4]
    
        while len(Soundex) < 4:
            Soundex.append(0)

        return Soundex

    else:
        print("Unknown character: ", word[0])
        print("Program terminated.")
        return -1

if __name__ == '__main__':
    word = input("Enter word: ")
    word = word.split()
    print("Original word: ", word)
    for char in word:
        print("Soundex: ", Soundex(char))