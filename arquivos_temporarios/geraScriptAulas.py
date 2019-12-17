origem = open('playlist.csv', 'r')
destino = open('scriptGerado.txt', 'w')

texto = origem.readlines()

textoDestino = []

for linha in texto:
    id, titulo, link = linha.split(';')
    string = f"Aulas.objects.create(\n\tid={id},\n\ttitulo='{titulo}',\n\tlink='{link[:-1]}')\n"
    textoDestino.append(string)

destino.writelines(textoDestino)

destino.close()
origem.close()
