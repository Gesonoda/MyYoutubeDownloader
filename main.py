# encoding: utf-8
import pytube
from pathlib import Path
import os
from pytube import YouTube
from pytube.cli import on_progress

def verificar_arquivo_existente(link, local_para_download):
    """_summary_

    Args:
        link (_type_): _description_
        novo_diretorio (_type_): _description_

    Returns:
        _type_: _description_
    """
    yt = pytube.YouTube(link, on_progress_callback = on_progress)
    titulo = yt.title
    pathlist = Path(local_para_download).glob('*.mp3')
    for path in pathlist:
        var = False
        path_basename = os.path.basename(path)
        path_basename = path_basename[:-4]
        if titulo.__eq__(path_basename):
            var = True
            break
    return var

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
    dir = str(Path(r"C:/Users/georg/Music/AudiosSDP/SDP_PlinioCorreiadeOliveira_videos"))
    novo_diretorio = Path(dir + '/' + nome_arquivo)
    verificar_se_existe_pasta(novo_diretorio)
    return novo_diretorio

def ler_arquivo_txt(arquivo):
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

def verificar_arquivos(novo_diretorio, lista_de_links):
    for link in lista_de_links:
        arquivo_ja_baixado = verificar_arquivo_existente(link, novo_diretorio)
        if arquivo_ja_baixado == False:
            baixar_arquivo(link, novo_diretorio)

def baixar_arquivo(link, novo_diretorio):
    yt = pytube.YouTube(link, on_progress_callback = on_progress)
    titulo = yt.title
    print("Título: ", titulo)
    print("Baixando...")
    arquivo=yt.streams.get_audio_only()
    downloaded_file = arquivo.download(novo_diretorio)
    converte_em_mp3(downloaded_file)

if __name__ == '__main__':
    directory = 'C:/Users/georg/Music'
    lista_de_txt = Path(directory).glob('*.txt')
    for txt in lista_de_txt:
        arquivo_txt = os.path.basename(txt)
        nome_arquivo_txt = arquivo_txt[:-4]
        nova_pasta_txt = criar_pasta_para_download(nome_arquivo_txt)
        lista_de_links = ler_arquivo_txt(txt)
        arquivo_txt = verificar_arquivos(nova_pasta_txt, lista_de_links)

    print("****************************************")
    print("Seja Feliz! Seus arquivos foram baixados")
    print("****************************************")
