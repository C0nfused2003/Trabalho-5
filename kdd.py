import time

class Glossario:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.palavras = list()


    def ler_arquivo(self):
        with open(self.caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:

                self.palavras.extend(linha.split())


    def bubble_sort(self):
        lista = self.palavras.copy()
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    def selection_sort(self):
        lista = self.palavras.copy()
        n = len(lista)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if lista[min_idx] > lista[j]:
                    min_idx = j
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
        return lista


    def python_sort(self):
        return sorted(self.palavras)


    def medir_tempo(self, func):
        inicio = time.time()
        resultado = func()
        fim = time.time()
        return resultado, fim - inicio


def main():

    glossario = Glossario('loremipsum.txt')
    

    glossario.ler_arquivo()


    resultado_bubble, tempo_bubble = glossario.medir_tempo(glossario.bubble_sort)
    print(f"Bubble Sort - Tempo: {tempo_bubble:.5f} segundos")
    

    resultado_selection, tempo_selection = glossario.medir_tempo(glossario.selection_sort)
    print(f"Selection Sort - Tempo: {tempo_selection:.5f} segundos")
    

    resultado_sort, tempo_sort = glossario.medir_tempo(glossario.python_sort)
    print(f"Python Sort - Tempo: {tempo_sort:.5f} segundos")
    

    print("\nResultados:")
    print("Bubble Sort:", resultado_bubble)
    print("Selection Sort:", resultado_selection)
    print("Python Sort:", resultado_sort)

    # Escolhe o algoritmo mais rápido e escreve no arquivo "palavras_ordenadas.txt"
    melhor_resultado = resultado_sort
    with open('palavras_ordenadas.txt', 'w') as arquivo:
        for palavra in melhor_resultado:
            arquivo.write(palavra + '\n')

if __name__ == "__main__":
    main()
