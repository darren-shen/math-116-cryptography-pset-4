import rotor
import reflector
import plugboard
import encoding

def decipher(c, left, middle, right, plug, refl):
    plaintext = ""
    for c in ciphertext:
        right_wheel.rotate()
        plaintext += plug.forward(right.backward(middle.backward(left.backward(refl.forward(left.forward(middle.forward(right.forward(plug.forward(c)))))))))
    return plaintext

# 2a
reflector_wiring = {' ': '-', '-': ' ', 'a': "'", "'": 'a', 'b': '!', '!': 'b', 'c': ',', ',': 'c', 'd': '.', '.': 'd', 'e': 'z', 'z': 'e', 'f': 'y', 'y': 'f', 'g': 'x', 'x': 'g', 'h': 'w', 'w': 'h', 'i': 'v', 'v': 'i', 'j': 'u', 'u': 'j', 'k': 't', 't': 'k', 'l': 's', 's': 'l', 'm': 'r', 'r': 'm', 'n': 'q', 'q': 'n', 'o': 'p', 'p': 'o'}
refl = reflector.Reflector()

left_wiring = {' ': ' ', 'a': 'l', 'b': 'f', 'c': 'i', 'd': 'd', 'e': '.', 'f': 'c', 'g': 'g', 'h': 'm', 'i': '-', 'j': 'e', 'k': ',', 'l': 'a', 'm': 'j', 'n': 'q', 'o': 'p', 'p': "'", 'q': 'h', 'r': 'k', 's': 'w', 't': 'v', 'u': '!', 'v': 'x', 'w': 'b', 'x': 'o', 'y': 'y', 'z': 'u', '.': 's', ',': 'n', '!': 'z', "'": 'r', '-': 't'}
left_wheel = rotor.Rotor(left_wiring, 7, 0, 0)

middle_wiring = {' ': 'u', 'a': 'a', 'b': '-', 'c': 'k', 'd': 'b', 'e': ',', 'f': 'c', 'g': 'x', 'h': 'q', 'i': 'v', 'j': 'n', 'k': 'i', 'l': 'd', 'm': 't', 'n': 'e', 'o': 'r', 'p': 'm', 'q': 'o', 'r': "'", 's': 's', 't': 'h', 'u': ' ', 'v': 'j', 'w': 'p', 'x': '.', 'y': '!', 'z': 'g', '.': 'l', ',': 'y', '!': 'f', "'": 'w', '-': 'z'}
middle_wheel = rotor.Rotor(middle_wiring, 22, 0, 0)

right_wiring = {' ': 'p', 'a': 's', 'b': '-', 'c': 'y', 'd': 'z', 'e': 'x', 'f': 'j', 'g': 'm', 'h': 'u', 'i': ' ', 'j': 'f', 'k': 'a', 'l': 'k', 'm': 'q', 'n': 'w', 'o': 'd', 'p': '.', 'q': ',', 'r': 'o', 's': 'e', 't': '!', 'u': 'c', 'v': 't', 'w': 'v', 'x': 'h', 'y': "'", 'z': 'g', '.': 'l', ',': 'r', '!': 'b', "'": 'n', '-': 'i'}
right_wheel = rotor.Rotor(right_wiring, 15, 0, 0)

plugboard_wiring = {' ': 'r', 'a': 'o', 'b': 'g', 'c': 'c', 'd': 'd', 'e': 'u', 'f': 'f', 'g': 'b', 'h': 'h', 'i': 'i', 'j': ',', 'k': 'z', 'l': 'l', 'm': "'", 'n': 'q', 'o': 'a', 'p': 'p', 'q': 'n', 'r': ' ', 's': '.', 't': 'w', 'u': 'e', 'v': 'v', 'w': 't', 'x': 'x', 'y': 'y', 'z': 'k', '.': 's', ',': 'j', '!': '!', "'": 'm', '-': '-'}
plug = plugboard.Plugboard(plugboard_wiring)

with open("./ciphertext_2a.txt") as f:
    ciphertext = f.read()

print(decipher(ciphertext, left_wheel, middle_wheel, right_wheel, plug, refl))

# 2b
reflector_wiring = {' ': '-', '-': ' ', 'a': "'", "'": 'a', 'b': '!', '!': 'b', 'c': ',', ',': 'c', 'd': '.', '.': 'd', 'e': 'z', 'z': 'e', 'f': 'y', 'y': 'f', 'g': 'x', 'x': 'g', 'h': 'w', 'w': 'h', 'i': 'v', 'v': 'i', 'j': 'u', 'u': 'j', 'k': 't', 't': 'k', 'l': 's', 's': 'l', 'm': 'r', 'r': 'm', 'n': 'q', 'q': 'n', 'o': 'p', 'p': 'o'}
refl = reflector.Reflector()

left_wiring = {' ': ' ', 'a': 'l', 'b': 'f', 'c': 'i', 'd': 'd', 'e': '.', 'f': 'c', 'g': 'g', 'h': 'm', 'i': '-', 'j': 'e', 'k': ',', 'l': 'a', 'm': 'j', 'n': 'q', 'o': 'p', 'p': "'", 'q': 'h', 'r': 'k', 's': 'w', 't': 'v', 'u': '!', 'v': 'x', 'w': 'b', 'x': 'o', 'y': 'y', 'z': 'u', '.': 's', ',': 'n', '!': 'z', "'": 'r', '-': 't'}
left_wheel = rotor.Rotor(left_wiring, 25, 0, 0)

middle_wiring = {' ': 'u', 'a': 'a', 'b': '-', 'c': 'k', 'd': 'b', 'e': ',', 'f': 'c', 'g': 'x', 'h': 'q', 'i': 'v', 'j': 'n', 'k': 'i', 'l': 'd', 'm': 't', 'n': 'e', 'o': 'r', 'p': 'm', 'q': 'o', 'r': "'", 's': 's', 't': 'h', 'u': ' ', 'v': 'j', 'w': 'p', 'x': '.', 'y': '!', 'z': 'g', '.': 'l', ',': 'y', '!': 'f', "'": 'w', '-': 'z'}
middle_wheel = rotor.Rotor(middle_wiring, 12, 0, 0)

right_wiring = {' ': 'p', 'a': 's', 'b': '-', 'c': 'y', 'd': 'z', 'e': 'x', 'f': 'j', 'g': 'm', 'h': 'u', 'i': ' ', 'j': 'f', 'k': 'a', 'l': 'k', 'm': 'q', 'n': 'w', 'o': 'd', 'p': '.', 'q': ',', 'r': 'o', 's': 'e', 't': '!', 'u': 'c', 'v': 't', 'w': 'v', 'x': 'h', 'y': "'", 'z': 'g', '.': 'l', ',': 'r', '!': 'b', "'": 'n', '-': 'i'}
right_wheel = rotor.Rotor(right_wiring, 12, 0, 0)

plugboard_wiring = {' ': ' ', 'a': 'p', 'b': 'b', 'c': 'c', 'd': 'k', 'e': '!', 'f': 'u', 'g': 'y', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'd', 'l': 'l', 'm': "'", 'n': 'n', 'o': 'o', 'p': 'a', 'q': 'x', 'r': 'z', 's': 'v', 't': 'w', 'u': 'f', 'v': 's', 'w': 't', 'x': 'q', 'y': 'g', 'z': 'r', '.': '.', ',': ',', '!': 'e', "'": 'm', '-': '-'}
plug = plugboard.Plugboard(plugboard_wiring)

with open("./ciphertext_2b.txt") as f:
    ciphertext = f.read()

print(decipher(ciphertext, left_wheel, middle_wheel, right_wheel, plug, refl))



