# Aluno: Mauro Wildemberg Pires Junior
#2022101186

def contacandidato(quantcandidados,candidatos=[0],i=1):
    if quantcandidados >= 2 and quantcandidados <=100:
        if i<=quantcandidados:
            y= input()
            return contacandidato(quantcandidados,candidatos+[y],i+1)
        
        else:
            return candidatos
    else:
        print("Insira um valor válido")
        main()

def confere(quantvotos,quantcandidados,votos,i=1):
    if quantvotos>=i:
        voto = int(input())
        if voto == 0:
            votos[0] = votos[0] + 1
            return confere(quantvotos,quantcandidados,votos,i+1)
        elif voto > 0 and voto <= quantcandidados:
            votos[voto] = votos[voto] + 1
            return confere(quantvotos,quantcandidados,votos,i+1)
        else:
            votos[quantcandidados+1] = votos[quantcandidados+1] + 1
            return confere(quantvotos,quantcandidados,votos,i+1)
    else:
        return votos
def exibevencedor(candidatos,quantcandidados,votos,i=1):
    if i < len(candidatos):
        print(f"{candidatos[i]}: {votos[i]}")
        return exibevencedor(candidatos,quantcandidados,votos,i+1)
    print(f"Brancos: {votos[0]}")
    print(f"Nulos: {votos[quantcandidados+1]}")

def ganha(z,votos,b = 1, i = 1):
    candidatos = len(votos)-1
    if i < candidatos:
        if votos[i] > votos[b]:
            b = i
        return ganha(z,votos,b ,i+1)
    else:
        print(f"Vencedor(a): {z[b]}")

def main():
    quantcandidados = int(input())
    z = contacandidato(quantcandidados)
    votos = [0] *(quantcandidados+2)
    quantvotos = int(input())
    s = confere(quantvotos,quantcandidados,votos)
    exibevencedor(z,quantcandidados,s)
    ganha(z,s)

main()