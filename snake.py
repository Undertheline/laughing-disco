import array

tela = []
def draw():
    i = 0
    while i < 64:
        tela.append("O")
        i += 1
        if i == 64:
            lista = tela
            def print_com_limite(texto, limite=8):
                for i in range(0, len(texto), limite):
                    print(texto[i:i+limite])
                    lista.clear
                    tela.clear
    print_com_limite(lista, limite=8)
    

tela.insert(20, "9") 
tela.insert(20, "9") 
draw()