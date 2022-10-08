import argparse
import hashlib


parser = argparse.ArgumentParser(description="calculate volume")
parser.add_argument("target", type=str, metavar='', help="The hash you want to crack")
parser.add_argument("-w", "--wordlist", type=str, metavar='', required=True, help="path of the wordlist you want to use")
parser.add_argument("-v", "--verbose", action="store_true", help="print out more output")
args = parser.parse_args()


def hash(string):
    hash = hashlib.sha256(bytes(string, "UTF-8")).hexdigest()
    return hash

wordlist = args.wordlist
target = args.target
target = target.lower()
verbose = args.verbose
cracked = False

def search():
    global cracked
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
        for word in file.readlines():
            word = word[:-1]
            ha = hash(word)
            if ha == target:
                cracked = True
            
            if not cracked and verbose:
                print(f"Trying {word}\t{ha} is not a match")

            if cracked:
                print(f"\n Match Found: {word}")
                return
        file.close()
    
    if not cracked:
        print("\nNo matches found")


search()
