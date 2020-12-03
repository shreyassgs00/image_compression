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
