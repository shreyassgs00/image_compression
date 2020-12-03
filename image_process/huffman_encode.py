def dfs(node, huffman_code, huffman_dict):
    if node != None:
        if node.hue != -1:
            huffman_dict[node.hue] = huffman_code
        dfs(node.left, huffman_code + '0', huffman_dict)
        dfs(node.right, huffman_code + '1', huffman_dict)    

def huffman_encode(huffman_tree):
    huffman_dict = {}
    dfs(huffman_tree, "", huffman_dict)
    return huffman_dict

def find_length_of_encoded_bits(huffman_codes, frequencies):
    length_of_encoded_bits = 0
    intensity_value_length = {}
    multiplied_dict = {}
    for i in huffman_codes:
        length = len(huffman_codes[i])
        intensity_value_length[i] = length
    for j in intensity_value_length:
        frequency = frequencies[j]
        multiplied_dict[j] = intensity_value_length[j]*frequency
    for k in multiplied_dict:
        length_of_encoded_bits = length_of_encoded_bits + multiplied_dict[k]
    return length_of_encoded_bits

def find_compression_ratio(actual_length, encoded_length):
    compression_ratio = encoded_length*100/actual_length
    return compression_ratio