import os
import threading
import time

global files, number_files, excluding, excluded, stop

files = []
number_files = 0
excluding = 0
excluded = 0
stop = False
    
def print_run():
    while stop == False:
        print(f'Escaneando.', end='\r')
        time.sleep(1)
        print(f'             ', end='\r')
        print(f'Escaneando..', end='\r')        
        time.sleep(1)
        print(f'             ', end='\r')
        print(f'Escaneando...', end='\r')
        time.sleep(1)
        print(f'             ', end='\r')

def search_for_files(path, searched_file):
    
    global files, number_files, excluding, stop

    for (dirpath, dirnames, filenames) in os.walk(path):        
        for file in filenames:
            if file == searched_file:
                files.append({"path": dirpath,
                              "file": file})
                excluding = excluding + 1
        number_files = number_files + len(filenames)

    stop = True

def confirm_exluding():

    global files, excluded

    print(f'>Serão excluidos {excluding} arquivos.')
    print(f'>Digite "Yes" para confirmar exclusão...')

    answer = input()

    if answer != 'Yes':
        print(f'>Cancelado!')

    else:
        for file in files:
            full_file = file["path"] + '/' + file["file"]
            os.remove(full_file)
            print(f'>>>Total de arquivos excluído: { full_file }')
            excluded = excluded + 1

    print(f'>>>Arquivos excluídos: { excluded }')    

print('>>>Esse programa procura arquivos para deletar de acordo com o nome')        
print('>Qual directório deseja escanear?')

directory = input()

print('>Qual o nome do arquivo?')

filename = input()

threading.Thread(target=print_run).start()

search_for_files(directory, filename)

print(f'>Total de arquivos escaneados: { number_files }')

if len(files) > 0:
    confirm_exluding()
else:
    print(f'>>>Nenhum arquivo encontrado!')
