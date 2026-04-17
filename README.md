Secure Password Generator (Gerador de Senhas Seguras)
Este é um utilitário de linha de comando escrito em Python que permite gerar senhas fortes e criar hashes criptográficos seguros (SHA-256 com Salt). O projeto foca em segurança utilizando a biblioteca secrets do Python, ideal para fins de criptografia.

✨ Funcionalidades
Geração Customizável: Escolha o comprimento da senha e quais tipos de caracteres incluir (Maiúsculas, Minúsculas, Números e Símbolos).

Segurança Criptográfica: Utiliza o módulo secrets para garantir aleatoriedade adequada para segurança.

Hashing de Senhas: Gera o hash da senha utilizando PBKDF2-HMAC-SHA256 com 100.000 iterações.

Salt Aleatório: Cria um salt único para cada senha, protegendo contra ataques de dicionário e Rainbow Tables.
