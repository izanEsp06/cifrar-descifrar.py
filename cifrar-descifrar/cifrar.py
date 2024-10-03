import string

# Función para el cifrado César
def caesar_cipher(text, shift):
    result = []
    alphabet = string.ascii_uppercase
    for char in text.upper():
        if char in alphabet:
            shifted_index = (alphabet.index(char) + shift) % 26
            result.append(alphabet[shifted_index])
        else:
            result.append(char)
    return ''.join(result)

# Función para el cifrado Vigenère
def vigenere_cipher(text, key):
    result = []
    alphabet = string.ascii_uppercase
    key_length = len(key)
    for i, char in enumerate(text.upper()):
        if char in alphabet:
            shifted_index = (alphabet.index(char) + key[i % key_length]) % 26
            result.append(alphabet[shifted_index])
        else:
            result.append(char)
    return ''.join(result)

# Función para el cifrado por Transposición
def transposition_cipher(text, key):
    text = text.replace(' ', '').upper()
    num_cols = len(key)
    num_rows = len(text) // num_cols + (1 if len(text) % num_cols != 0 else 0)
    matrix = [['X'] * num_cols for _ in range(num_rows)]
    
    idx = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if idx < len(text):
                matrix[r][c] = text[idx]
                idx += 1
    
    sorted_key = sorted(list(enumerate(key)), key=lambda x: x[1])
    result = []
    for col, _ in sorted_key:
        for row in matrix:
            result.append(row[col])
    
    return ''.join(result)

# Texto a cifrar
text = "AYER FUIMOS AL PARQUE"

# Claves
caesar_key = 10 # Se trata de un algoritmo de sustitución alfabética que consiste en desplazar
# los símbolos del alfabeto k posiciones a la derecha. Por ejemplo, si k = 3: cambia A por D, B por E, etc. 
# Es cíclico, de modo que cambia X por A, Y por B y Z por C. 

vigenere_key = [3, 5, 2, 8] # Ampliación del algoritmo César. La clave no está formada por un único
# desplazamiento, sino por d desplazamientos {k0, k1, k2, k3, . . . , kd−1}. Para cifrar un
# texto se agrupa el mensaje inicial en bloques de d símbolos. Si un símbolo aparece en
# la posición j (de cualquier bloque), se le aplica el desplazamiento kj.

transposition_key = [4, 2, 0, 5, 1, 3]

# : Este cifrado consiste en cambiar la posición de los caracteres en el
# texto de entrada. Se define un tamaño de bloque y se cogen los caracteres de entrada
# en bloques de ese tamaño. Para cifrar un bloque se aplica una permutación concreta,
# que es la clave secreta. En caso de que el último bloque no se llene, se usa “relleno”.

# Aplicando los cifrados
caesar_result = caesar_cipher(text, caesar_key)
vigenere_result = vigenere_cipher(text, vigenere_key)
transposition_result = transposition_cipher(text, transposition_key)

# Mostrando los resultados
print("Cifrado César:", caesar_result)
print("Cifrado Vigenère (clave {3, 5, 2, 8}):", vigenere_result)
print("Cifrado Transposición (clave [4, 2, 0, 5, 1, 3]):", transposition_result)
