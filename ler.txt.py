arquivo = open('loremipsum.txt', 'r')


conteudo_completo = arquivo.read()


print("Conteúdo completo do arquivo:")
print(conteudo_completo)


arquivo.close()

arquivo = open('loremipsum.txt', 'r')


primeira_linha = arquivo.readline()

# Imprimir a primeira linha
print("\nPrimeira linha do arquivo:")
print(primeira_linha)


arquivo.close()


arquivo = open('loremipsum.txt', 'r')


tres_primeiros_caracteres = arquivo.read(3)


print("\nPrimeiros 3 caracteres do arquivo:")
print(tres_primeiros_caracteres)


arquivo.close()

with open('loremipsum.txt', 'r') as arquivo:
    
    conteudo_completo_with = arquivo.read()


print("\nConteúdo do arquivo utilizando 'with':")
print(conteudo_completo_with)
