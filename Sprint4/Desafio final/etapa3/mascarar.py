import hashlib

def gerar_hash_sha1(string):
    sha1 = hashlib.sha1()
    sha1.update(string.encode('utf-8'))
    return sha1.hexdigest()

if __name__ == "__main__":
    while True:
        entrada = input("Digite uma string para gerar o hash SHA-1 (ou 'sair' para terminar): ")
        if entrada.lower() == 'sair':
            break
        hash_resultado = gerar_hash_sha1(entrada)
        print(f"Hash SHA-1: {hash_resultado}")
