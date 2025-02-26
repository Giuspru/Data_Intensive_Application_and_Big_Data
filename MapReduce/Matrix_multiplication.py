'''we want to implement the c = axb matrix multiplication
where a is a m x n matrix and b is a n x p matrix, hence 
c will be a n x p matrix. Everythings using the method MapReduce'''



'''we assuming our inputs is a set of key values pairs:
([i,j] , [a_ij,0]) for matrix a 
([j,k] , [b_jk,1]) for matrix b
'''

'''Implementing a script that takes a numpy matrix and provides
an input desired like output, is another problem'''

'''
matrix = [ ([0,0], [1,0]),
           ([0,1], [2,0]),
           ([1,0], [3,0]),
           ([1,1], [4,0])
        ]
Position on the left and values on the right. 
The second value of the second array identify the matrix
0 for matrix a and 1 for matrix b
'''


# matrix = [ ([0,0], [1,0]),
#            ([0,1], [2,0]),
#            ([1,0], [3,0]),
#            ([1,1], [4,0])
#         ]
# print(matrix[0][1][1])

class step1map:

    def mapper(self, matrix):
        mapped_values = []

        for index , value in matrix:
            if value[1] == 0:
                j = index[1]
                mapped_values.append((j, [0,index[0], value[0]]))
            else:
                j = index[0]
                mapped_values.append((j, [1, index[1], value[0]]))
        return mapped_values
    

matrix1 = [ ([0,0], [1,0]),
           ([0,1], [2,0]),
           ([1,0], [3,0]),
           ([1,1], [4,0])
        ]

matrix2 = [ ([0,0], [5,0]),
           ([0,1], [6,0]),
           ([1,0], [7,0]),
           ([1,1], [8,0])
        ]        

mapper = step1map()
mapped = mapper.mapper(matrix1)
#print(mapped)


class step1reduce:
    def reducer(self, mapped):
        a = []
        b = []
        h = 0
        z = 0
        
        for _, array in mapped:
            if array[0] == 0:
                a.append((array[1], array[2]))
                h += 1
            else:
                b.append((array[1], array[2]))
                z += 1
        ris = []
        for pa in a:
            i = pa[0]
            aij = pa[1]
            for pb in b:
                k = pb[0]
                bjk = pb[1]
            
                ris.append(([i,k], [aij*bjk]))
        return ris



reducer = step1reduce() 
reduced = reducer.reducer(mapped)
print(reduced)






    

#class step1reduce:


#class ste2map:


#class step2reduce:

