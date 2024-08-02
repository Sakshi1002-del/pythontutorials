import numpy as np
'''
CURVE_CENTER = 80
grades = np.array([72,35,64,88,51,90,74,12])
average = grades.mean();
print(average)
change = CURVE_CENTER -average
print(change)
def curves(grades):
    average = grades.mean();
    change = CURVE_CENTER -average
    new_grades = grades + change
    return np.clip(new_grades,grades,100)

print(curves(grades))
'''
'''
temperatures = np.array([29.3,42.2,18.8,16.1,38.0,12.5,12.6,49.5,38.6,
                         31.3,9.2,22.2]).reshape(2,2,3)
print(temperatures.shape)
print(temperatures)

print("*" *60)
print(np.swapaxes(temperatures,1,2))
'''
'''
batting_averages = np.array([
    [50,30,70,40],
    [20,60,90,70],
    [100,90,70,80],
    [40,20,30,50]
    ])
print ("size of an array: ", batting_averages.shape)

print ("Maximum Average: ", batting_averages.max())

print ("Maximum Average: ", batting_averages.max(axis=0))

print ("Maximum Average Row: ", batting_averages.max(axis=1))

'''
'''
numbers = np.linspace(5,50,24,dtype=int).reshape(4,6) #allows you to creat evenly spaced arrays with a specific number of element
print(numbers)
'''

'''
nums = np.arange(32).reshape(4,1,8)
print (nums)
nums_1 = np.arange(48).reshape(1,6,8)
print (nums_1)
print ("*" *60)
print(nums + nums_1)
'''
'''
arr1 = np.arange(10,100,5,dtype=int).reshape(3,6)
print (arr1)
print ("*" *40)

arr2 = np.arange(10,100,5,dtype=int).reshape(3,6)
print (arr2)

sum_of_2_arrays = arr1+arr2
print ( sum_of_2_arrays)

prod_of_2_arrays = arr1*arr2
print ( prod_of_2_arrays)
'''
'''
square = np.array([
    [16,3,2,13],
    [5,10,11,8],
    [9,6,7,12],
    [4,15,14,1]
    ])
'''
'''
for i in range(4):
    print(square[:,i].sum()==34)
    print(square[i,:].sum()==34)
'''

'''
square = np.array([
    [16,3,2,13],
   [5,10,11,8],
    [9,6,7,12],
    [4,15,14,1]
    ])
    '''

'''
print(square[:2,:2])
print(square[:2,2:])
'''
'''
numbers = np.linspace(5,50,24,dtype="int").reshape(4,-1)
print(numbers)

print ("*" *60)
'''
'''
mask = numbers%5==0
print(mask)

print ("all the values divisible by 5 ", numbers[mask])
print ("all the values divisible by 8 ", numbers[numbers%8==0])

print(numbers.T)
print("Horizontal Sorting", np.sort(numbers,axis=0))
print("Vertical Sorting", np.sort(numbers,axis=1))
'''
'''
a = np.array([[4,8],[6,1]])
b = np.array([[3,5],[7,2]])

print(np.concatenate((b,a))) #merging two array
print(np.concatenate((b,a),axis=None))
print(np.hstack((a,b)))
print(np.hstack((a,b)))

stock_prices = np.random.random((30,10))
print("stock_prices")
print(stock_prices)
'''

'''
import numpy as np
array = np.arange(30).reshape(6,5)
print (array)
print()

print(np.argmax(array))
print(np.argmax(array, axis=1)) # argmax: used to return the indices of the max elements
                               # elements of the given array along with the specified axis
print(np.argmax(array, axis=0))
'''

'''
array = np.array([
    [3,7,1],
    [10,5,4],
    [8,9,4]
    ])
print (array)
print(np.sort(array, axis =None))
print(np.sort(array, axis =1))
print(np.sort(array, axis =0))
'''

'''
list = [
    np.array([3,2,8,9]),
    np.array([6,7,52,29,28]),
    np.array([23,12,68])
    ]

result = []

for i in range(len(list)):
    result.append(np.mean(list[i])) # a built-in function used to add an item to the end of a list
     
print (result)
 '''

'''
array = np.array([
    [3,4,5],
    [6,7,8],
    [9,10,11]
    ])

newRow = np.array([1,2,3])
newArray = np.vstack((array, newRow)) # stack array vertically (row-wise)to make a single array
print (newArray)

'''

'''
array = np.array([5,6,7,8,9,10,11])
reversedarray = np.flipud(array)
print (reversedarray)
'''

'''
matrix1 =[
    [5,6,7],
    [4,3,2],
    [7,8,9]
    ]
matrix2 =[
    [7,9,8],
    [6,5,4],
    [3,2,4]
    ]
result = np.dot(matrix1,matrix2) #multiply two matrics in single line using numpy
print(result)
'''

'''
n=8

matrix = np.zeros((n,n), dtype=int)
# fill 1 with alternate rows and column
matrix[::2, 1::2] = 2
matrix[1::2, ::2] = 2

#print the checkboard pattern
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()
'''





      
                                                
