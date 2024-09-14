# Array de 15 números inteiros 
numeros = [42, 23, 16, 15, 8, 4, 89, 7, 90, 3, 66, 33, 57, 28, 10]

# Método Selection Sort
def selectionSort(array):
   
    for i in range(len(array)):
        
        min_index = i
        
        
        for j in range(i + 1, len(array)):
            
            if array[min_index] > array[j]:
                min_index = j
        
       
        array[i], array[min_index] = array[min_index], array[i]


selectionSort(numeros)

print("Array ordenado de forma crescente:", numeros)
