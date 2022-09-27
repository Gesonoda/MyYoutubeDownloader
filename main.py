# encoding: utf-8
import pytube
from pathlib import Path
import os
from pytube import YouTube
from pytube.cli import on_progress
import shutil

def baixar_link(link, novo_diretorio):
    """_summary_

    Args:
        link (_type_): _description_
        novo_diretorio (_type_): _description_

    Returns:
        _type_: _description_
    """
    yt = pytube.YouTube(link, on_progress_callback = on_progress)
    titulo = yt.title
    print("Título: ", titulo)
    print("Baixando...")
    ys=yt.streams.get_audio_only()
    downloaded_file = ys.download(novo_diretorio)
    file = converte_em_mp3(downloaded_file)
    return file, str(titulo)

def converte_em_mp3(downloaded_file):
    """_summary_

    Args:
        downloaded_file (_type_): _description_

    Returns:
        _type_: _description_
    """
    base, ext = os.path.splitext(downloaded_file)
    new_file = str(base + '.mp3')
    # colocar um renomear com (2) caso o arquivo ja exista
    os.rename(Path(downloaded_file), Path(new_file))
    return new_file

def cria_pasta(nome_pasta):
    """_summary_

    Args:
        nome_pasta (_type_): _description_

    Raises:
        e: _description_
    """
    import os
    if not os.path.isdir(nome_pasta):
        try:
            os.makedirs(nome_pasta)
        except PermissionError as e:
            raise e
    return


def verificar_se_existe_pasta(novo_diretorio):
    if not os.path.isdir(novo_diretorio):
        try:
            os.makedirs(novo_diretorio)
        except PermissionError as e:
            raise e

def criar_pasta_para_download(nome_arquivo):
    if nome_arquivo.endswith('.txt'):
        name_archive = nome_arquivo[21:-len(".txt")]
    dir = str(Path(r"C:/Users/georg/Music/AudiosSDP/SDP_PlinioCorreiadeOliveira_videos"))
    novo_diretorio = Path(dir + '/' + name_archive)
    verificar_se_existe_pasta(novo_diretorio)
    return novo_diretorio

def ler_arquivo(arquivo):
    with open(arquivo, "r") as archive:
        lista_de_links = list()
        for link in archive:
            lista_de_links.append(link)
        verificar_lista_vazia(lista_de_links)
    return lista_de_links

def verificar_lista_vazia(lista_de_links):
    if lista_de_links:
        print("Arquivo lido com sucesso") 
    else:
        print("Erro - verificar se o arquivo está vazio")
        exit

def baixar_arquivos(novo_diretorio, lista_de_links):
    for link in lista_de_links:
        mp3, nome_mp3 = baixar_link(link, novo_diretorio)

if __name__ == '__main__':
    arquivo = r"C:/Users/georg/Music/Cultura.txt"
    name = arquivo.split("\\")
    for el in name:
        if ".txt" in el:
            nome_arquivo = el
    
    novo_diretorio = criar_pasta_para_download(nome_arquivo)

    lista_de_links = ler_arquivo(arquivo)

    baixar_arquivos(novo_diretorio, lista_de_links)

    print("****************************************")
    print("Seja Feliz! Seus arquivos foram baixados")
    print("****************************************")
