class CharNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def get_alphabet(text):
    alphabet = {}
    for char in text:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1
    return alphabet
# Si le caractère est déjà présent dans le dictionnaire alphabet, sa valeur est augmentée de 1
# si le caractère n''est pas présent dans le dictionnaire alphabet, une nouvelle entrée est ajoutée avec une valeur =1


def get_sorted_char_nodes(alphabet):
    char_nodes = []
    for char, freq in alphabet.items():
        char_node = CharNode(char, freq)
        char_nodes.append(char_node)
    # "cn " :la fréquence de chaque objet stockée dans l'attribut "freq".
    return sorted(char_nodes, key=lambda cn: (cn.freq, ord(cn.char)))


""


def build_huffman_tree(char_nodes):
    while len(char_nodes) > 1:
        t1 = char_nodes.pop(0)
        t2 = char_nodes.pop(0)
        new_node = CharNode(None, t1.freq + t2.freq)
        new_node.left = t1
        new_node.right = t2
        char_nodes.append(new_node)
        char_nodes = sorted(char_nodes, key=lambda cn: (
            cn.freq, ord(cn.char) if cn.char is not None else float('inf')))
    return char_nodes[0]


""


# La fonction renvoie une table de correspondance entre les caractères et leur code binaire
def build_encoding_table(root):
    encoding_table = {}

    def build_encoding_table_rec(node, code):  # construire la table de correspondance
        if node.char:  # la fonction ajoute une entrée à la table de correspondance encoding_table
            encoding_table[node.char] = code
        else:
            build_encoding_table_rec(node.left, code + '0')
            build_encoding_table_rec(node.right, code + '1')
    build_encoding_table_rec(root, '')
    return encoding_table
# sinon appelle build_encoding_table_rec pour le nœud enfant gauche et ajoute '0' à la fin de la chaîne de caractères

# La fonction encode le texte en utilisant la table de correspondance et renvoie le texte encodé


def encode_text(text, encoding_table):
    encoded_text = ''
    for char in text:
        encoded_text += encoding_table[char]
    return encoded_text


def pack_bits(encoded_text):
    packed_bits = []
    for i in range(0, len(encoded_text), 8):
        # extrait un octet  de la séquence binaire encoded_text en utilisant l'indice i
        byte = encoded_text[i:i + 8]
        # ajoute des zéros à droite de l'octet extrait pour le compléter à une longueur de 8 bits
        byte += '0' * (8 - len(byte))
        packed_bits.append(int(byte, 2))
    return packed_bits  # la liste des octets entiers compressés représentant le texte.
# Si le dernier octet contient moins de 8 bits, des zéros sont ajoutés à droite pour compléter l'octet.

# calcule le taux de compression en pourcentage


def compress(text):
    alphabet = get_alphabet(text)
    char_nodes = get_sorted_char_nodes(alphabet)
    root = build_huffman_tree(char_nodes)
    encoding_table = build_encoding_table(root)
    encoded_text = encode_text(text, encoding_table)
    packed_bits = pack_bits(encoded_text)
    return packed_bits


""

# 0 représente une compression maximale et 1 représente l'absence de compression


def compression_rate(initial_size, compressed_size):
    return 1 - compressed_size / initial_size


texte = "this is an example of a huffman tree"
compressed_text = compress(texte)
print(compressed_text)
for bit in compressed_text:
    print(bin(bit)[2:].zfill(8), end=' ')
alice = open("C:\\Users\\ASUS\\Desktop\\S6\\Projet Algo 2023\\alice.txt", "r")
lines = alice.read().splitlines()
text = ""
for j in range(len(lines)):
    text += lines[j]
ga = get_alphabet(text)
print(ga)
compressed_text = compress(text)
print(compressed_text)
for bit in compressed_text:
    print(bin(bit)[2:].zfill(8), end=' ')
