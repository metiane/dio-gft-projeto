def classificar_heroi(xp):
    if xp < 1000:
        return "Ferro"
    elif 1001 <= xp <= 2000:
        return "Bronze"
    elif 2001 <= xp <= 5000:
        return "Prata"
    elif 5001 <= xp <= 7000:
        return "Ouro"
    elif 7001 <= xp <= 8000:
        return "Platina"
    elif 8001 <= xp <= 9000:
        return "Ascendente"
    elif 9001 <= xp <= 10000:
        return "Imortal"
    else:
        return "Radiante"

herodex = []
# Leitura dos dados
nome = input("Digite o nome do herói: (0 para parar) ")

# Enquanto o nome for diferente de 0
while nome != "0":
    xp = int(input("Digite o XP do herói: "))
    herodex.append({"nome": nome, "xp": xp})  # Adiciona o herói ao dicionário
    nome = input("Digite o nome do próximo herói: (0 para parar) ")   
# Classificação dos heróis
for heroi in herodex:
    print(f"Nome: {heroi['nome']}, Classificação: {classificar_heroi(heroi['xp'])}")





