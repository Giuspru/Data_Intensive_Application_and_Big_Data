#Co-Occurrence Matrix with MapReduce:

class PairsMapper:

    def map(self, text):
        
        word_count = []
        words = text.split()
        for w1 in words:
            for w2 in words:
                if w1 != w2:
                    word_count.append(((w1, w2), 1))

        return word_count
    
# file = open("text.txt", "r")
# text = file.read()  
# pair = PairsMapper()
# mapped = pair.map(text) 
# # print(mapped)


def shuffle_and_sort(mapped_data):
    shuffled_data = {}

    for key, value in mapped_data:
        if key in shuffled_data:
            shuffled_data[key].append(value)
        else:
            shuffled_data[key] = [value]

    return shuffled_data

# shuffle_data = shuffle_and_sort(mapped)
# # print(shuffle_data)


class pairsReducer:

    def reduce(self, shuffled_data):
        reduce_data = {}
        for key, value in shuffled_data.items():
            reduce_data[key] = sum(value)
            sorted_items = sorted(reduce_data.items(), key=lambda x: x[1], reverse=True)
            reduced_data = dict(sorted_items)
        return reduced_data
    



if __name__ == "__main__":

    file = open("text.txt", "r")
    text = file.read()
    mapper = PairsMapper()
    mapped_data = mapper.map(text)
    shuffle_data = shuffle_and_sort(mapped_data)
    reducer = pairsReducer()
    reduced_data = reducer.reduce(shuffle_data)
    print(reduced_data)







