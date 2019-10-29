"""
    generate all possible anagrams of a string, ie, permutations of the chars
"""
import pickle
import unicodedata
import re

d = set()


def stripAccents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError:  # unicode is a default on python 3
        pass
    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    return str(text)


def fac(n):
    if n:
        return n * fac(n - 1)
    else:
        return 1


def load_dict(fn):
    try:
        with open(fn, "rt", encoding="utf-8") as f:
            s = f.read()
    except FileNotFoundError:
        print("Cannot open/read file: ", fn)
        sys.exit(1)
    d = {}
    for w in set(s.split("\n")):
        fw = formula(w)
        # fw2 = formula(stripAccents(w))
        # if not re.match('^[a-zA-Z_]+$', w):
        #     w = {w, stripAccents(w)}
        #     d[fw] = d.get(fw, set()) | w
        #     d[fw2] = d.get(fw, set()) | w
        # else:
        #     w = {w}
        #     d[fw] = d.get(fw, set()) | w
        d[fw] = d.get(fw, set()) | {w}

    return d


def write_dict(d):
    with open ("optdict.pkl", "wb") as f:
        pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)
    with open ("optdict.txt", "w") as f:
        for k, v in d.items():
            f.write(str(k) + ' >>> ' + str(v) + '\n\n')


def read_dict():
    with open ("optdict.pkl", "rb") as f:
        return pickle.load(f)


def formula(m):
    d = {c:m.count(c) for c in m}
    return "".join(map(lambda x: x + str(d[x]), sorted(d)))


"""
    On first time convert liste.de.mots.francais.frgut.txt to binary file
"""


d = load_dict("liste.de.mots.francais.frgut.txt")
write_dict(d)

d = read_dict()
print(type(d))
m = "in"  # pour rentrer dans la boucle
while m:
    m = input("Entrez un mot : ")
    print(formula(m))
    print(formula(stripAccents(m)))
    assert formula('rode') == 'd1e1o1r1', "Devrait faire d1e1o1r1"
    if len(m) > 4:
        print("Je recherche parmi ", fac(len(m)), " combinaisons. ")
    if len(m) > 5:
        print("Cela peut prendre un moment...")
    if len(m) > 6:
        print("Pourquoi ne pas aller chercher un café ?")
    if len(m) > 7:
        print("Et à part ça, la famille, ça va ? ")

    print(d.get(formula(m)), d.get(formula(stripAccents(m))))
    # try:
    #     print(d.get(formula(m)).union(d.get(formula(stripAccents(m)))))
    # except AttributeError:
    #     print("NoneType object has no attribute union")
    # except:
    #     print("object is not iterable")
    # print(type(d.get(formula(m))))
    # print(set(filter(lambda x: x in d, permuti(m))))

