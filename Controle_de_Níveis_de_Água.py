
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# Função responsável por definir a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Exibe o título do sistema
print("=" * 45)
print(" SISTEMA DE CONTROLE DE NÍVEIS DE ÁGUA")
print("=" * 45)

# Exibe todos os níveis com suas respectivas cores
for i, situacao in enumerate(niveis, start=1):
    cor = definir_cor(i)

    print(cor + situacao + Style.RESET_ALL)

# Solicita o nível atual do reservatório
try:
    nivel_atual = int(input("\nInforme o nível atual (1 a 5): "))

    if 1 <= nivel_atual <= 5:
        cor = definir_cor(nivel_atual)
        mensagem = niveis[nivel_atual - 1]

        print("\nSituação atual do reservatório:")
        print(cor + mensagem + Style.RESET_ALL)
    else:
        print(Fore.RED + "Erro: informe um nível entre 1 e 5."
              + Style.RESET_ALL)

except ValueError:
    print(Fore.RED + "Erro: digite um número inteiro válido."
          + Style.RESET_ALL)

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL)
