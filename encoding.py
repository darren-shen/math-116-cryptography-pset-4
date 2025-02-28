from collections import Counter


punctuation_to_num = {'.': 27, ',': 28, '!': 29, "'": 30, "-": 31}
num_to_puncutation = {27: '.', 28: ',', 29: '!', 30:"'", 31: "-"}

def char_to_num(ch):
    # Check for space first.
    if ch == ' ':
        return 0
    
    # Convert character to lowercase for uniform processing.
    ch = ch.lower()
    
    # If it's a letter, map it from a=1, b=2, ..., z=26.
    if 'a' <= ch <= 'z':
        num = ord(ch) - ord('a') + 1  # a -> 1, b -> 2, ..., z -> 26
        return num
    
    # map punctuation to 5-bits as in punctuation_to_num
    elif ch in punctuation_to_num:
        return punctuation_to_num[ch]
    
    return ''

def num_to_char(num):
    if num == 0: #0 = space
        return ' '
    elif 1 <= num <= 26: #letters indexed by position in alphabet
        return chr(num + ord('a') + -1)
    elif num in num_to_puncutation: #map numbers to punctuation as in num_to_punctuation
        return num_to_puncutation[num]
    
#processes the string so that it only involves the allowed characters
def process(s):
    processed = ""
    s = s.lower() #convert to lowercase
    allowed_chars = {" "}
    allowed_chars.update(punctuation_to_num)  # Add all keys from punctuation_to_num.
    for ch in s:
        if 'a' <= ch <= 'z' or ch in allowed_chars:
            processed += ch
    return processed
    
def add_chars(c1:str, c2:str):
    assert len(c1) ==1
    assert len(c2) == 1
    s1 = char_to_num(c1)
    s2 = char_to_num(c2)
    return num_to_char((s1+s2)%32)

def shift_char_by_delta(delta: int, ch: str) -> str:
    num = char_to_num(ch)
    new_num = (num + delta) % 32
    return num_to_char(new_num)

def unshift_char_by_delta(delta: int, ch: str) -> str:
    num = char_to_num(ch)
    new_num = (num - delta) % 32
    return num_to_char(new_num)


def IC(s):
    assert s == process(s)
    char_counts = Counter(s)
    n = len(s)
    if n <= 1:
        print("string too short")
        return -1

    total_coincidences = 0
    for c in char_counts:
        total_coincidences += char_counts[c] * (char_counts[c]-1)
    return total_coincidences / (n*(n-1))


# 1a: encrypting vigenere ciphers
def vigenere_encrypt(plaintext, key):
    result = ""
    plaintext, key = process(plaintext), process(key)
    key_length = len(key)
    for i, ch in enumerate(plaintext):
        result += add_chars(ch, key[i % key_length])
    return result

with open("./1a.txt") as f:
    message = f.read()

# print(vigenere_encrypt(message, "marauders map"))

# 1b: decrypting vigenere ciphers
def sub_chars(c1:str, c2:str):
    assert len(c1) ==1
    assert len(c2) == 1
    s1 = char_to_num(c1)
    s2 = char_to_num(c2)
    return num_to_char((s1-s2)%32)

def vigenere_decrypt(plaintext, key):
    result = ""
    plaintext, key = process(plaintext), process(key)
    key_length = len(key)
    for i, ch in enumerate(plaintext):
        result += sub_chars(ch, key[i % key_length])
    return result

def shift(plaintext, k):
    return vigenere_encrypt(plaintext, num_to_char(k))

def letter_distribution(plaintext):
    result = [0] * 32
    for char in plaintext:
        result[char_to_num(char)] += 1
    
    for i in range(32):
        result[i] /= len(plaintext)
    return result

def isolate_nmod(plaintext, k):
    result = [""] * k
    for i in range(len(plaintext)):
        result[i % k] += plaintext[i]
    return result

def MIC(s, t):
    count_s = Counter(s)
    count_t = Counter(t)
    n1, n2 = len(s), len(t)

    total_coincidences = 0
    for c in set(s + t):
        total_coincidences += count_s[c] * count_t[c]
    return total_coincidences / (n1 * n2)

def make_words(differences):
    result = []
    for i in range(32):
        j = i
        word = num_to_char(j)
        for difference in differences:
            j = (j + difference) % 32
            word += num_to_char(j)
        result.append(word)
    return result

# steps for 1b
"""
with open("./1b.txt") as f:
    message = f.read()

for i in range(2, 20):
    results = [IC(m) for m in isolate_nmod(message, i)]
    print("key length", str(i) + ":", [IC(m) for m in isolate_nmod(message, i)])
"""

"""
key length 2: [0.04331779331779332, 0.04698118782625825]
key length 3: [0.05394736842105263, 0.05592105263157895, 0.04479283314669653]
key length 4: [0.03912363067292645, 0.04655712050078247, 0.04616588419405321, 0.04627766599597585]
key length 5: [0.038112522686025406, 0.030852994555353903, 0.03884711779448621, 0.045112781954887216, 0.02568922305764411]
key length 6: [0.0851063829787234, 0.09131205673758866, 0.06382978723404255, 0.09131205673758866, 0.05851063829787234, 0.061979648473635525]
key length 7: [0.025609756097560974, 0.03414634146341464, 0.04878048780487805, 0.054878048780487805, 0.03780487804878049, 0.02804878048780488, 0.032926829268292684]
key length 8: [0.0380952380952381, 0.047619047619047616, 0.046031746031746035, 0.05238095238095238, 0.03333333333333333, 0.03492063492063492, 0.047619047619047616, 0.03529411764705882]
key length 9: [0.04233870967741935, 0.06653225806451613, 0.028225806451612902, 0.04032258064516129, 0.06048387096774194, 0.056451612903225805, 0.06048387096774194, 0.04435483870967742, 0.03870967741935484]

therefore, key is most likely length 6
"""

"""
result = isolate_nmod(message, 6)
for i in range(len(result) - 1):
    best, m = 0, 0
    for j in range(32):
        test_str = shift(result[i], j)
        curr_MIC = MIC(test_str, result[i + 1])
        if curr_MIC > best:
            best = curr_MIC
            m = j
    print("most optimal difference between", i, "and", str(i + 1) + ":", m, best)
"""

"""
most optimal difference between 0 and 1: 1 0.07421875
most optimal difference between 1 and 2: 29 0.0720486111111111
most optimal difference between 2 and 3: 23 0.0724826388888889
most optimal difference between 3 and 4: 5 0.07899305555555555
most optimal difference between 4 and 5: 25 0.06560283687943262
"""

"""
test = make_words([1, 29, 23, 5, 25])
for t in test:
    print(t)
    print(vigenere_decrypt(message, t))
"""
# key="turing", the imitation game may perhaps be criticised on the ground that the odds are weighted too heavily against the machine. if the man were to try and pretend to be the machine he would clearly make a very poor showing. he would be given away at once by slowness and inaccuracy in arithmetic.


# steps for 1c
"""
with open("./1c.txt") as f:
    message = f.read()

for i in range(2, 20):
    results = [IC(m) for m in isolate_nmod(message, i)]
    print("key length", str(i) + ":", [IC(m) for m in isolate_nmod(message, i)])
"""

"""
key length 2: [0.03332099222510181, 0.02815829528158295]
key length 3: [0.027210884353741496, 0.031462585034013606, 0.031462585034013606]
key length 4: [0.02702702702702703, 0.03153153153153153, 0.03903903903903904, 0.023809523809523808]
key length 5: [0.03218390804597701, 0.03218390804597701, 0.03201970443349754, 0.027093596059113302, 0.029556650246305417]
key length 6: [0.02, 0.016666666666666666, 0.03, 0.03260869565217391, 0.050724637681159424, 0.028985507246376812]
key length 7: [0.07142857142857142, 0.06190476190476191, 0.08571428571428572, 0.05714285714285714, 0.047619047619047616, 0.0761904761904762, 0.09047619047619047]
key length 8: [0.017543859649122806, 0.023391812865497075, 0.04093567251461988, 0.0196078431372549, 0.032679738562091505, 0.0392156862745098, 0.0457516339869281, 0.0196078431372549]
key length 9: [0.014705882352941176, 0.022058823529411766, 0.014705882352941176, 0.025, 0.041666666666666664, 0.041666666666666664, 0.016666666666666666, 0.016666666666666666, 0.041666666666666664]
key length 10: [0.0380952380952381, 0.0380952380952381, 0.0380952380952381, 0.009523809523809525, 0.0380952380952381, 0.0380952380952381, 0.01904761904761905, 0.03296703296703297, 0.04395604395604396, 0.03296703296703297]

therefore, key is most likely length 7
"""

"""
result = isolate_nmod(message, 7)
for i in range(len(result) - 1):
    best, m = 0, 0
    for j in range(32):
        test_str = shift(result[i], j)
        curr_MIC = MIC(test_str, result[i + 1])
        if curr_MIC > best:
            best = curr_MIC
            m = j
    print("most optimal difference between", i, "and", str(i + 1) + ":", m, best)
"""

"""
most optimal difference between 0 and 1: 27 0.08163265306122448
most optimal difference between 1 and 2: 29 0.09977324263038549
most optimal difference between 2 and 3: 31 0.09070294784580499
most optimal difference between 3 and 4: 30 0.08616780045351474
most optimal difference between 4 and 5: 28 0.07256235827664399
most optimal difference between 5 and 6: 9 0.07709750566893424
"""

"""
test = make_words([27, 29, 31, 30, 28, 9])
for t in test:
    print(t)
    print(vigenere_decrypt(message, t))
"""

# key="tolkien", all that is gold does not glitter,not all those who wander are lost.the old that is strong does not wither,deep roots are not reached by the frost.
