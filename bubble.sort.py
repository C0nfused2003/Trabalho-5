# Método Bubble Sort
def bubbleSort(array):
    
    for i in range(len(array)):
        
        for j in range(0, len(array) - i - 1):
            
            if array[j] > array[j + 1]:
                
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

numeros = [42, 23, 16, 15, 8, 4, 89, 7, 90, 3, 66, 33, 57, 28, 10]

bubbleSort(numeros)

print("Array ordenado de forma crescente:", numeros)
