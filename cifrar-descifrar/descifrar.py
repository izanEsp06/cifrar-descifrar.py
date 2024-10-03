import string

# Función para descifrar César
def caesar_decipher(ciphertext, shift):
    return caesar_cipher(ciphertext, -shift)

# Función para descifrar Vigenère
def vigenere_decipher(ciphertext, key):
    result = []
    alphabet = string.ascii_uppercase
    key_length = len(key)
    for i, char in enumerate(ciphertext.upper()):
        if char in alphabet:
            shifted_index = (alphabet.index(char) - key[i % key_length]) % 26
            result.append(alphabet[shifted_index])
        else:
            result.append(char)
    return ''.join(result)

# Función para descifrar por Transposición
def transposition_decipher(ciphertext, key):
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols + (1 if len(ciphertext) % num_cols != 0 else 0)
    matrix = [[''] * num_cols for _ in range(num_rows)]
    
    sorted_key = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    idx = 0
    for col, _ in sorted_key:
        for row in range(num_rows):
            if idx < len(ciphertext):
                matrix[row][col] = ciphertext[idx]
                idx += 1
    
    result = []
    for row in matrix:
        result.extend(row)
    
    return ''.join(result).rstrip('X')

# Función para cifrado César reutilizada
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

# Textos a descifrar
ciphertext_cesar = "TAK BAD XM FMDPQ"
ciphertext_vigenere = "MWMOSX I ESRMT"
ciphertext_transposition = "NAUNBEUTRASENUTARXEXXX"

# Claves
caesar_key = 12 # Se trata de un algoritmo de sustitución alfabética que consiste en desplazar
# los símbolos del alfabeto k posiciones a la derecha. Por ejemplo, si k = 3: cambia A por D, B por E, etc. 
# Es cíclico, de modo que cambia X por A, Y por B y Z por C. 

vigenere_key = [4, 5, 8, 2] # Ampliación del algoritmo César. La clave no está formada por un único
# desplazamiento, sino por d desplazamientos {k0, k1, k2, k3, . . . , kd−1}. Para cifrar un
# texto se agrupa el mensaje inicial en bloques de d símbolos. Si un símbolo aparece en
# la posición j (de cualquier bloque), se le aplica el desplazamiento kj.

transposition_key = [3, 0, 4, 2, 1]
# Este cifrado consiste en cambiar la posición de los caracteres en el
# texto de entrada. Se define un tamaño de bloque y se cogen los caracteres de entrada
# en bloques de ese tamaño. Para cifrar un bloque se aplica una permutación concreta,
# que es la clave secreta. En caso de que el último bloque no se llene, se usa “relleno”.

# Aplicando los descifrados
decipher_cesar_result = caesar_decipher(ciphertext_cesar.replace(' ', ''), caesar_key)
decipher_vigenere_result = vigenere_decipher(ciphertext_vigenere.replace(' ', ''), vigenere_key)
decipher_transposition_result = transposition_decipher(ciphertext_transposition.replace(' ', ''), transposition_key)

# Mostrando los resultados
print("Descifrado César (k=12):", decipher_cesar_result)
print("Descifrado Vigenère (clave {4, 5, 8, 2}):", decipher_vigenere_result)
print("Descifrado Transposición (clave [3, 0, 4, 2, 1]):", decipher_transposition_result)