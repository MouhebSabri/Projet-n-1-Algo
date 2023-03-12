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


def get_sorted_char_nodes(alphabet):
    char_nodes = []
    for char, freq in alphabet.items():
        char_node = CharNode(char, freq)
        char_nodes.append(char_node)
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


def build_encoding_table(root):
    encoding_table = {}

    def build_encoding_table_rec(node, code):
        if node.char:
            encoding_table[node.char] = code
        else:
            build_encoding_table_rec(node.left, code + '0')
            build_encoding_table_rec(node.right, code + '1')
    build_encoding_table_rec(root, '')
    return encoding_table


def encode_text(text, encoding_table):
    encoded_text = ''
    for char in text:
        encoded_text += encoding_table[char]
    return encoded_text


def pack_bits(encoded_text):
    packed_bits = []
    for i in range(0, len(encoded_text), 8):
        byte = encoded_text[i:i + 8]
        byte += '0' * (8 - len(byte))
        packed_bits.append(int(byte, 2))
    return packed_bits


def compress(text):
    alphabet = get_alphabet(text)
    char_nodes = get_sorted_char_nodes(alphabet)
    root = build_huffman_tree(char_nodes)
    encoding_table = build_encoding_table(root)
    encoded_text = encode_text(text, encoding_table)
    packed_bits = pack_bits(encoded_text)
    return packed_bits


""


def compression_rate(initial_size, compressed_size):
    return 1 - compressed_size / initial_size


def get_compression_rate(initial_size, compressed_size): return 1 - compressed_size / initial_size


texte = "aujourd'hui on a une seance de projet algorithmique ouaiiis"
compressed_text = compress(texte)
print(compressed_text)
for bit in compressed_text:
    print(bin(bit)[2:].zfill(8), end=' ')
