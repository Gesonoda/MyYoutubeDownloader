# encoding: utf-8
import pytube
from pathlib import Path
import os
from pytube import YouTube
from pytube.cli import on_progress
import shutil

def baixar_link(link):
    yt = pytube.YouTube(link, on_progress_callback = on_progress)
    titulo = yt.title
    print("Título: ", titulo)
    print("Baixando...")
    ys=yt.streams.get_audio_only()
    downloaded_file = ys.download()
    converte_em_mp3(downloaded_file)
    return downloaded_file, str(titulo)

def converte_em_mp3(downloaded_file):
    base, ext = os.path.splitext(downloaded_file)
    new_file = str(base + '.mp3')
    os.rename(downloaded_file, new_file)

def cria_pasta(nome_pasta):
    """
    Cria pasta para armazenar arquivos de output caso não exista
    :param nome_pasta: Caminho desejado
    :return: Criação da posta
    """
    import os
    if not os.path.isdir(nome_pasta):
        try:
            os.makedirs(nome_pasta)
        except PermissionError as e:
            raise e
    return


if __name__ == '__main__':    
    arquivo = r"C:/Users/georg/Music/Tradição.txt"
    name = arquivo.split("\\")
    for el in name:
        if ".txt" in el:
            nome_arquivo = el
    
    if nome_arquivo.endswith('.txt'):
        name_archive = nome_arquivo[21:-len(".txt")]
    dir = str(Path(r"C:/Users/georg/Music/AudiosSDP/SDP_PlinioCorreiadeOliveira_videos"))
    novo_diretorio = Path(dir + '/' + name_archive)
    if not os.path.isdir(novo_diretorio):
        try:
            os.makedirs(novo_diretorio)
        except PermissionError as e:
            raise e

    with open(arquivo, "r") as archive:
        lista_de_links = list()
        for link in archive:
            lista_de_links.append(link)

        if lista_de_links:
            print("Arquivo lido com sucesso") 
        else:
            print("Erro - verificar se o arquivo está vazio")
            exit

    for link in lista_de_links:
        mp3, nome_mp3 = baixar_link(link)
        source = Path(str(os.getcwd()) + '/' + nome_mp3 + '.mp3')
        destino = Path(str(novo_diretorio) + '/' + nome_mp3 + '.mp3')
        # shutil.copy2(source, destino)
        # if os.path.exists(source):
        #     os.remove(source)
        root_src_dir = os.path.join('/',source)
        root_target_dir = os.path.join('/',destino)
        operation= 'move' # 'copy' or 'move'
        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_target_dir)
            if not os.path.exists(dst_dir):
                os.mkdir(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    os.remove(dst_file)
                if operation is 'copy':
                    shutil.copy(src_file, dst_dir)
                elif operation is 'move':
                    shutil.move(src_file, dst_dir)