from string import ascii_lowercase, ascii_uppercase


low = list(ascii_lowercase)
hig = list(ascii_uppercase)
baj = low[-13:]

def encrypt(s):
    res = ""
    for i in s:
        try:
            if i.islower():
                if low.index(i) < len(low)-13:
                    res = res + low[low.index(i)+13]
                else:
                    res = res + low[baj.index(i)]
            else:
                if hig.index(i) < len(hig)-13:
                    res = res + hig[hig.index(i)+13]
                else:
                    res = res + hig[hig[-13:].index(i)]

        except ValueError:
            res = res + i
    return res


def decrypt(s):
    res = ""
    for i in s:
        try:
            if i.islower():
                res = res + low[low.index(i)-13]
            else:
                res = res + hig[hig.index(i)-13]

        except ValueError:
            res = res + i
    return res
print(decrypt(encrypt("hello")))
