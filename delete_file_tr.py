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
        print(f'Taranıyor.', end='\r')
        time.sleep(1)
        print(f'             ', end='\r')
        print(f'Taranıyor..', end='\r')        
        time.sleep(1)
        print(f'             ', end='\r')
        print(f'Taranıyor...', end='\r')
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

def confirm_excluding():

    global files, excluded

    print(f'> {excluding} dosyalar silinecek.')
    print(f'> Silmeyi onaylamak için "Yes" yazın...')

    answer = input()

    if answer.lower() != 'yes':
        print(f'> İptal edildi !')

    else:
        for file in files:
            full_file = os.path.join(file["path"], file["file"])
            os.remove(full_file)
            print(f'>>> Toplam silinen dosyalar:  {full_file}')
            excluded = excluded + 1

    print(f'>>> Silinen dosyalar:  {excluded}')    

print('>>> Bu program belirtilen kriterlere göre silinecek dosyaları arar.')        
print('> Hangi dizini taramak istersiniz?')

directory = input()

print('> Dosyanın adı nedir?')

filename = input()

threading.Thread(target=print_run).start()

search_for_files(directory, filename)

print(f'> Toplam tarama yapılan dosyalar: {number_files}')

if len(files) > 0:
    confirm_excluding()
else:
    print(f'>>> Hiç dosya bulunamadı!')
