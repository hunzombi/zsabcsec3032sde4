from datetime import datetime
start_time = datetime.now()
import hashlib
import sys


if len(sys.argv) != 3:
    raise Exception("Invalid Syntax\nSyntax: python hashcracker <hash> <wordlist>")

crack = sys.argv[1]
file_path = sys.argv[2]

def enc(word):
    s = ''.join(str(l) for l in word)
    hash = hashlib.md5(s.encode('utf-8'))
    res = hash.hexdigest()
    return res

found = False

with open(file_path, 'r') as f:
    for w in f.readlines():
        try:
            w = w.rstrip("\n")
            if found:
                break
            elif enc(w) == crack:
                found = True
                print(f"The hash is: {w}")
        except:
            continue
    if not found:
        print("No hash was found!")
    f.close()

end_time = datetime.now()

print(end_time-start_time)