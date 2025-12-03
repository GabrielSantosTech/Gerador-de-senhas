import secrets
import string
import hashlib
import getpass
from typing import List, Optional

def gerar_senha_forte(comprimento: int = 12, usar_maiusculas: bool = True, 
                     usar_minusculas: bool = True, usar_numeros: bool = True, 
                     usar_simbolos: bool = True) -> str:
    """
    Gera uma senha forte e aleatória com base nas preferências do usuário.
    
    Args:
        comprimento: Comprimento da senha desejado
        usar_maiusculas: Incluir letras maiúsculas
        usar_minusculas: Incluir letras minúsculas
        usar_numeros: Incluir números
        usar_simbolos: Incluir símbolos especiais
        
    Returns:
        str: Senha gerada
    """
    caracteres = []
    
    if usar_maiusculas:
        caracteres.extend(string.ascii_uppercase)
    if usar_minusculas:
        caracteres.extend(string.ascii_lowercase)
    if usar_numeros:
        caracteres.extend(string.digits)
    if usar_simbolos:
        caracteres.extend('!@#$%^&*()_+-=[]{}|;:,.<>?')
    
    if not caracteres:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado")
    
    # Garante que a senha tenha pelo menos um caractere de cada tipo selecionado
    senha = []
    if usar_maiusculas:
        senha.append(secrets.choice(string.ascii_uppercase))
    if usar_minusculas:
        senha.append(secrets.choice(string.ascii_lowercase))
    if usar_numeros:
        senha.append(secrets.choice(string.digits))
    if usar_simbolos:
        senha.append(secrets.choice('!@#$%^&*()_+-=[]{}|;:,.<>?'))
    
    # Preenche o resto da senha com caracteres aleatórios
    while len(senha) < comprimento:
        senha.append(secrets.choice(caracteres))
    
    # Embaralha a senha para melhor aleatoriedade
    secrets.SystemRandom().shuffle(senha)
    
    return ''.join(senha)

def gerar_hash_senha(senha: str, salt: Optional[bytes] = None) -> tuple:
    """
    Gera um hash seguro da senha usando SHA-256 com salt.
    
    Args:
        senha: Senha em texto puro
        salt: Salt opcional. Se não fornecido, um novo será gerado.
        
    Returns:
        tuple: (hash_gerado, salt_usado)
    """
    if salt is None:
        salt = secrets.token_bytes(16)
    
    # Combina a senha com o salt e gera o hash
    hash_obj = hashlib.pbkdf2_hmac(
        'sha256',
        senha.encode('utf-8'),
        salt,
        100000  # Número de iterações
    )
    
    return hash_obj.hex(), salt.hex()

def menu_principal():
    """Exibe o menu principal e processa as escolhas do usuário."""
    print("\n=== Gerador de Senhas Seguras ===")
    print("1. Gerar nova senha")
    print("2. Sair")
    
    while True:
        escolha = input("\nEscolha uma opção: ").strip()
        if escolha in ['1', '2']:
            return escolha
        print("Opção inválida. Tente novamente.")

def obter_preferencias():
    """Obtém as preferências do usuário para geração de senha."""
    print("\n=== Preferências da Senha ===")
    
    while True:
        try:
            comprimento = int(input("Digite o comprimento da senha (mínimo 8): "))
            if comprimento < 8:
                print("O comprimento mínimo é 8.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido.")
    
    print("\nSelecione os tipos de caracteres a serem incluídos:")
    usar_maiusculas = input("Incluir letras maiúsculas? (S/n): ").strip().lower() != 'n'
    usar_minusculas = input("Incluir letras minúsculas? (S/n): ").strip().lower() != 'n'
    usar_numeros = input("Incluir números? (S/n): ").strip().lower() != 'n'
    usar_simbolos = input("Incluir símbolos especiais? (S/n): ").strip().lower() != 'n'
    
    # Garante que pelo menos um tipo de caractere foi selecionado
    if not any([usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos]):
        print("Pelo menos um tipo de caractere deve ser selecionado. Usando todos os tipos.")
        usar_maiusculas = usar_minusculas = usar_numeros = usar_simbolos = True
    
    return {
        'comprimento': comprimento,
        'usar_maiusculas': usar_maiusculas,
        'usar_minusculas': usar_minusculas,
        'usar_numeros': usar_numeros,
        'usar_simbolos': usar_simbolos
    }

def main():
    """Função principal do programa."""
    print("Bem-vindo ao Gerador de Senhas Seguras!")
    
    while True:
        escolha = menu_principal()
        
        if escolha == '2':
            print("\nObrigado por usar o Gerador de Senhas Seguras!")
            break
            
        # Obter preferências do usuário
        try:
            prefs = obter_preferencias()
            
            # Gerar senha
            senha = gerar_senha_forte(
                comprimento=prefs['comprimento'],
                usar_maiusculas=prefs['usar_maiusculas'],
                usar_minusculas=prefs['usar_minusculas'],
                usar_numeros=prefs['usar_numeros'],
                usar_simbolos=prefs['usar_simbolos']
            )
            
            # Gerar hash da senha
            hash_senha, salt = gerar_hash_senha(senha)
            
            # Exibir resultados
            print("\n=== Senha Gerada com Sucesso! ===")
            print(f"Senha: {senha}")
            print(f"Hash (SHA-256 com salt): {hash_senha}")
            print(f"Salt usado: {salt}")
            print("\nImportante: Anote sua senha em um local seguro!")
            
            input("\nPressione Enter para continuar...")
            
        except Exception as e:
            print(f"\nOcorreu um erro: {e}")
            print("Por favor, tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()