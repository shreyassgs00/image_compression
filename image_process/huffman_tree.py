class Node:
    def __init__(self, hue, freq):
        self.hue = hue # The color value
        self.freq = freq # The frequency of the color
        self.left = None # Left subtree
        self.right = None # Right subtree




class Heap:
    def __init__(self, array):
        self.array = array
        self.create_heap()

    def heapify(self, i):
        least = i
        l = i*2 + 1
        r = i*2 + 2

        if l < len(self.array) and self.array[l].freq < self.array[least].freq:
            least = l

        if r < len(self.array) and self.array[r].freq < self.array[least].freq:
            least = r
        
        if least != i:
            self.array[i], self.array[least] = self.array[least], self.array[i]
            self.heapify(least)


    def create_heap(self):
        x = (len(self.array) - 1) // 2
        for i in range(x, -1, -1):
            self.heapify(i)

    def get_smallest(self):
        return self.array[0]

    def delete_smallest(self):
        self.array[0], self.array[len(self.array) - 1] = self.array[len(self.array) - 1], self.array[0]
        self.array.pop()

        self.heapify(0)

    def insert(self, node):
        self.array.append(node)
        i = len(self.array) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.array[i].freq < self.array[parent].freq:
                self.array[i], self.array[parent] = self.array[parent], self.array[i]
            else:
                break
            i = parent


    def length(self):
        return len(self.array)
    

def create_huffman_tree(freq):    
    freq_array = [Node(hue, freq[hue]) for hue in freq]

    heap = Heap(freq_array)

    while heap.length() > 1:
        a = heap.get_smallest()
        heap.delete_smallest()
        b = heap.get_smallest()
        heap.delete_smallest()        

        result_node = Node(-1, a.freq + b.freq)
        result_node.left = a
        result_node.right = b
        heap.insert(result_node)

    return heap.array[0]