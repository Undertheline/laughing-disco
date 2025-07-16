import array

tela = []
def draw():
    i = 0
    while i < 25:
        tela.append("O")
        i += 1
        if i == 25:
            lista = tela
            def print_com_limite(texto, limite=5):
                for i in range(0, len(texto), limite):
                    print(texto[i:i+limite])
    print_com_limite(lista, limite=5)
    lista.clear
    tela.clear

draw()
tela.insert(20, "2") 
draw()