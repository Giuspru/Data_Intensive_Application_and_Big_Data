'''As first thing we impolement a map function that:
1) Takes a text file and generate a list of key-value pairs, divided by lines
2) For each line it generates another list of key-value pairs divided by space'''

class WordCounterMapper:

    def map(self, text):
        lines = text.split("\n")
        word_counts = []

        for line in lines:
            words = line.split()
            for word in words:
                word_counts.append((word, 1))

        return word_counts #obtained a list [(word1, 1), (word2, 1), (word3, 1), ...]
    
# file = open("text.txt", "r")
# text = file.read()

# mapper = WordCounterMapper()
# mapped_data = mapper.map(text)

# print(mapped_data)


def shuffle_and_sort(mapped_data): # i want to obtain {word : [1, 1, 1, 1, 1]} for example
    shuffled_data = {}

    for key, value in mapped_data:
        if key in shuffled_data:
            shuffled_data[key].append(value)
        else:
            shuffled_data[key] = [value] #It has to be an array, because it has to be modified with an append

    return shuffled_data
    

# shuffle_data = shuffle_and_sort(mapped_data)
# print(shuffle_data)


class WordCounterRedecer:

    def reduce(self, shufflled_data):
        reduce_data = {}

        for key, values in shufflled_data.items():
            reduce_data[key] = sum(values)
            sorted_items = sorted(reduce_data.items(), key=lambda x: x[1], reverse=True)
            reduce_data = dict(sorted_items)
            

        return reduce_data
        

# reducer = WordCounterRedecer()
# reduce_data = reducer.reduce(shuffle_data)
# print(reduce_data)


if __name__ == "__main__":
    file = open("text.txt", "r")
    text = file.read()

    mapper = WordCounterMapper()
    mapped_data = mapper.map(text)
    shuffle_data = shuffle_and_sort(mapped_data)
    reducer = WordCounterRedecer()
    reduce_data = reducer.reduce(shuffle_data)

    print(reduce_data)
