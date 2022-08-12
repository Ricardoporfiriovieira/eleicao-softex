from enum import Enum

class Candidatos(Enum):
    candidato_1 = 889
    candidato_2 = 847
    candidato_3 = 515
    voto_branco = 0

candidatos = [0,0,0,0]

loop = bool(1)

while(loop):
    try:
        print(" 889 - candidato_1 \n 847 - candidato_2 \n 515 - candidato_3 \n 0 - voto_branco ")
        voto = int(input("Digite o numero do candidato desejado: "))
        if(Candidatos.candidato_1.value == voto):
            candidatos[0] += 1
        elif(Candidatos.candidato_2.value == voto):
            candidatos[1] += 1
        elif(Candidatos.candidato_3.value == voto):
            candidatos[2] += 1
        else:
            candidatos[3] += 1

        loop = bool(0) if input("Deseja continuar? [S/N]").upper() == 'N' else bool(1)
        
        if(candidatos[0] > candidatos[1]):
            maior = 1
        elif(candidatos[1] > candidatos[2]):
             maior = 2
        else:
            maior = 3
        
    except:
        print("\n Erro tente novamente! \n")

print(f"Vencedor: Candidato {maior}\ncandidato 1 Votos: {candidatos[0]}\ncandidato 2 Votos: {candidatos[1]}\ncandidato 3 Votos: {candidatos[2]}\nVotos Nulos:{candidatos[3]}")



