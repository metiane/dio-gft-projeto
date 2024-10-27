# Função que recebe como parâmetro a quantidade 
# de vitorias e derrotas de um jogador,
# depois disso retorna o resultado para uma variável, 
# o saldo de Rankeadas deve ser feito através do calculo 
# (vitorias - derrotas)

def saldo(vitorias, derrotas):    
    saldo = vitorias - derrotas
    return saldo

def rankeada(saldo):
# Função que recebe como parâmetro a quantidade
if saldo <10:
    rank = "ferro"
elif  11<= saldo <= 20:
    rank = "bronze"
elif  21<= saldo <= 50:
    rank = "prata"
elif 51<= saldo <= 80:
    rank = "ouro"
elif 81<= saldo <= 90:
    rank = "diamante"
elif 91 <= saldo <= 100:
    rank = "lendario"
elif saldo >= 101:
    rank = "imortal"
return rank
## Saída

#Exibe uma mensagem:
print(f"O Herói tem de saldo de **{saldo}** e está no nível de **{rank}**")