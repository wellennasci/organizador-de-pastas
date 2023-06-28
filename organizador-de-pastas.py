

import os

try:
    pasta_downloads = os.path.join("c:\\Users", os.getlogin(), "Downloads" )
except:
    print(f'Não foi possível alternar para a pasta {pasta_downloads}')

os.chdir(pasta_downloads)
lista_arquivos = [arquivo.lower() for arquivo in os.listdir() if os.path. isfile(arquivo)]
lista_extensoes = {tipo.split('.')[-1] for tipo in lista_arquivos}

for tipo in lista_extensoes:
    if os.path.exists(tipo): 
        pass
    else:
         os.mkdir(tipo)


for arquivo in lista_arquivos:
    pasta_destino = arquivo.split('.')[-1] 
    de = os.path.join(os.getcwd(), arquivo)
    para = os.path.join(os.getcwd(), pasta_destino, arquivo)
    if os.path. exists(de): 
        os.replace(de, para) 
        


