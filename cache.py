import random, traceback
try:
    mp=[]
    for i in range(128):
        x=random.randint(0,2047)
        x=bin(x)
        x=x[2:]
        while len(x)!=11:
            x='0'+x
        mp.append(x)
    mc=[['',0,'    ',0],['',0,'    ',0],['',0,'    ',0],['',0,'    ',0],['',0,'    ',0],['',0,'    ',0],['',0,'    ',0],['',0,'    ',0]]

    def LerEndereco(mp,cache,miss,hit):
        endereco=str(input()[:7])
        rotulo=endereco[:4]
        conj=endereco[4]
        aux=0
        if conj=='0':
            for i in range(4):
                if endereco==mc[i][0]:
                    aux=1
                    hit+=1
                    if mc[i][3]!=15:
                        mc[i][3]+=1
                    break
            if aux==0:
                miss+=1
                aux2=0
                for i in range(4):
                    if mc[i][1]==0:
                        mc[i][0]=endereco
                        mc[i][1]=1
                        mc[i][2]=rotulo
                        mc[i][3]=0
                        aux2=1
                        break
                if aux2==0:
                    aux3=16
                    for i in range(4,8):
                        if mc[i][3]<aux3:
                            aux3=mc[i][3]
                    for i in range(4,8):
                        if mc[i][3]==aux3:
                            mc[i][0]=endereco
                            mc[i][1]=1
                            mc[i][2]=rotulo
                            mc[i][3]=0
                            break
        else:
            for i in range(4,8):
                if endereco==mc[i][0]:
                    aux=1
                    hit+=1
                    break
            if aux==0:
                miss+=1
                aux2=0
                for i in range(4,8):
                    if mc[i][1]==0:
                        mc[i][0]=endereco
                        mc[i][1]=1
                        mc[i][2]=rotulo
                        mc[i][3]=0
                        aux2=1
                        break
                if aux2==0:
                    aux3=16
                    for i in range(4,8):
                        if mc[i][3]<aux3:
                            aux3=mc[i][3]
                    for i in range(4,8):
                        if mc[i][3]==aux3:
                            mc[i][0]=endereco
                            mc[i][1]=1
                            mc[i][2]=rotulo
                            mc[i][3]=0
                            break
        print("bloco da memória :",int(endereco,2)//4)
        print("conjunto :",conj)
        return cache,hit,miss

    def EscreverMem(principal,cache,miss,hit):

        return principal,cache,miss,hit

    def Estatistica(mp,mc,hitl,missl,hite,misse):
        print("quantidade de acessos realizados :",leitura+escrita)
        print("quantidade de leituras realizadas :",leitura)
        print("quantidade de escritas realizadas :",escrita)
        if hitl!=0 or missl!=0:
            print("quantidade de acertos na leitura :",hitl,"percent :",hitl*100/(hitl+missl))
            print("quantidade de erros na leitura :",missl,"percent :",missl*100/(hitl+missl))
        if hite!=0 or misse!=0:
            print("quantidade de acertos na escrita :",hite,"percent :",hite*100/(hite+misse))
            print("quantidade de erros na escrita :",misse,"percent :",misse*100/(hite+misse))
        print("Prime Enter para voltar para interface principal",end='')
        input()

    hitl=0
    missl=0

    hite=0
    misse=0

    leitura=0
    escrita=0
    while True:
        print("\n\n---Memória Principal---")
        print("  Bloco  |endereço|   valor   |endereço|   valor   |endereço|   valor   |endereço|   valor   ")
        for i in range(0,128,4):
            print("Bloco {:2} : {:07b}:{}  {:07b}:{}  {:07b}:{}  {:07b}:{}".format(i//4,i,mp[i],i+1,mp[i+1],i+2,mp[i+2],i+3,mp[i+3]))
        print("\n\n---Memória Cache---")
        print("   Linha   |val|    valor    | rotl | subs |")
        for i in range(8):
            print("Linha {0:03b} :| {2} | {1:11} | {3} | {4:04b} |".format(i,mc[i][0],mc[i][1],mc[i][2],mc[i][3]))
        print("""Escolha uma opção:
    0 - Sair
    1 - Ler um endereço da memória
    2 - Escrever na memória
    3 - Apresentar as estatísticas""")
        op=int(input())
        if op==0:
            break
        elif op==1:
            leitura+=1
            mc,hitl,missl=LerEndereco(mp,mc,missl,hitl)
        elif op==2:
            escrita+=1
            mp,mc,misse,hite=EscreverMem(mp,mc,misse,hite)
        elif op==3:
            Estatistica(mp,mc,hitl,missl,hite,misse)
except Exception:
    traceback.print_exc()












input()
