import subprocess
import re
import sys


def remover_credenciais_github():
    """
    Remove todas as credenciais relacionadas ao GitHub no Gerenciador de
    Credenciais do Windows usando o comando cmdkey.
    """
    try:
        print(
            """Buscando credenciais do GitHub no Gerenciador de
            Credenciais do Windows..."""
        )

        processo = subprocess.run(
            ["cmdkey.exe", "/list"],
            capture_output=True,
            text=True,
            check=True,
            encoding="utf-8",
        )

        saida = processo.stdout

        padrao = re.compile(r"Target: (git:https://github.com/|github.com)")

        linhas = saida.splitlines()
        credenciais_encontradas = []

        for linha in linhas:
            if match := padrao.search(linha):
                target = match[0].replace("Target: ", "").strip()
                credenciais_encontradas.append(target)

        if not credenciais_encontradas:
            print("Nenhuma credencial do GitHub encontrada para remover.")
            return

        print("\nAs seguintes credenciais do GitHub foram encontradas:")
        for target in credenciais_encontradas:
            print(f"- {target}")

        confirmacao = input(
            "\nTem certeza de que deseja remover estas credenciais? (s/n): "
        ).lower()
        if confirmacao != "s":
            print("Operação cancelada.")
            return

        print("\nRemovendo credenciais...")

        for target in credenciais_encontradas:
            try:
                subprocess.run(
                    ["cmdkey.exe", "/delete", target],
                    check=True,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                )
                print(f"Credencial '{target}' removida com sucesso.")
            except subprocess.CalledProcessError as e:
                print(
                    f"Não foi possível remover '{target}': {e.stderr.strip()}",
                    file=sys.stderr,
                )

        print(
            "\nProcesso concluído. As credenciais do GitHub foram removidas.")

    except subprocess.CalledProcessError as e:
        print(
            f"Erro ao executar o comando do sistema: {e.stderr.strip()}",
            file=sys.stderr,
        )
        print("Verifique se o 'cmdkey.exe' está acessível no seu sistema.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}", file=sys.stderr)


if __name__ == "__main__":
    remover_credenciais_github()
