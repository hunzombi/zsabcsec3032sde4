translator = {
    'a' : '0',
    'b' : '1',
    'c' : '00',
    'd' : '10',
    'e' : '01',
    'f' : '11',
    'g' : '000',
    'h' : '100',
    'i' : '110',
    'j' : '010',
    'k' : '001',
    'l' : '011',
    'm' : '101',
    'n' : '111',
    'o' : '0000',
    'p' : '0001',
    'q' : '0010',
    'r' : '0011',
    's' : '0100',
    't' : '0101',
    'u' : '0110',
    'v' : '0111',
    'w' : '1000',
    'x' : '1001',
    'y' : '1010',
    'z' : '1011',
    '0' : '1100',
    '1' : '1101',
    '2' : '1110',
    '3' : '1111',
    '4' : '00000',
    '5' : '00001',
    '6' : '00010',
    '7' : '00011',
    '8' : '00100',
    '9' : '00101',
    ' ' : '2',
    '\n' : '/',
}

reversetrans = {value : key for key, value in translator.items()}

def ecode():
    with open('wordlist.txt', 'r') as f:
        with open('habbrbbbro.txt', 'a') as f2:
            for word in f.read():
                try:
                    letter = translator[word]
                except:
                    continue
                f2.write(letter+' ' if word != ' ' or word != '\n' else letter)
            f2.close()
        f.close()

def dcode():
    with open('habbrbbbro.txt', 'r') as f:
        with open('esults.txt', 'a') as f2:
            combs = {i for i in f.read()}
            for word in combs:
                if word == ' ':
                    continue
                else:
                    f2.write(reversetrans[word])
        f2.close()
    f.close()

dcode()