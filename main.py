import os

from base_conhecimento import BaseConhecimento
from assistente import Assistente


def main():
    # Garante que os caminhos "data/..." funcionem de qualquer pasta.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    base = BaseConhecimento("data/base_conhecimento.json")
    if not base.carregar():
        print("Não foi possível iniciar o assistente sem a base de conhecimento.")
        return

    assistente = Assistente("Citizen Assist AI", base)
    assistente.perguntar()


if __name__ == "__main__":
    main()
