arquivo = open('texto.txt', 'w')

texto = list()

texto.append("Primeira frase adicionada ao arquivo.")
texto.append("Segunda frase adicionada ao arquivo.")
texto.append("Terceira frase adicionada ao arquivo.")

for linha in texto:
    arquivo.write(linha + '\n')

arquivo.close()
