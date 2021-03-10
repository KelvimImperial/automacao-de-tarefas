import os
"""from tkinter import *

class QuantidadeArquivo(object):
    def __init__(self,instancia):
        pass
if __name__=="__main__":
    instanci=Tk()
    instancia.geomefrry"""


listaLivros=list()
listapdf=[]

for (pasta,sub,arquivo) in os.walk("."):
    print()
    print("["+pasta+"]")

    try:
        input("Aperte Enter para ver os conteudos dos diretorios...")
    except:
        break
    for c in arquivo:
        print("-->",os.path.join(pasta,c))

        listaLivros.append(os.path.splitext(c))       
print()
print(f"Neste Diretorio Existe {len(listaLivros)-1} arquivos")

#print(listaLivros)
print()
    
"""for c in listaLivros:
    print(c)
    print()
    
    for x in c: 
            #print(os.path.join(x))
        if x in ".pdf":
            JutandoNomeExtensão=os.path.join(pasta,x)
            
            listapdf.append(os.path.join(x))"""
print()
#print(listaLivros)
print(f"Temos {len(listaLivros)-1} arquivos neste diretorio")
        

