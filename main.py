password-generator/  
├── main.py          # Código principal  
├── README.md        # Documentação bonita  
└── requirements.txt # Dependências (se precisar)  
import random
import string

def generate_password(length=12):
    """Gera uma senha aleatória com letras, números e símbolos."""
    characters = string.ascii_letters + string.digits + "!@#$%&*"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔒 GERADOR DE SENHAS SEGURAS 🔒")
    length = int(input("Quantos caracteres? (Recomendado: 12): "))
    password = generate_password(length)
    print(f"Sua senha: \033[1;32m{password}\033[0m")  # Cor verde no terminal
