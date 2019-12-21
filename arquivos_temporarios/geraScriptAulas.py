origem = open('playlist.csv', 'r')
destino = open('scriptGerado.txt', 'w')

texto = origem.readlines()

textoDestino = []

for linha in texto:
    id, titulo, link = linha.split(';')

    posicao = link.find('=') + 1
    a = link[posicao:]
    posicao = a.find('&')
    link = a[:posicao]

    print(link)

    string = f"Aulas.objects.create(\n\tid={id},\n\ttitulo='{titulo}',\n\tlink='{link}')\n"
    textoDestino.append(string)

destino.writelines(textoDestino)

destino.close()
origem.close()