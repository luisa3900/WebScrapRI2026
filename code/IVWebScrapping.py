import os
import re
from collections import defaultdict
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


indice_invertido = defaultdict(set)
urls_indexadas = set()


def normalizar_url(url):
    url = url.strip()

    if not url:
        return ""

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url


def url_valida(url):
    partes = urlparse(url)
    return partes.scheme in ("http", "https") and bool(partes.netloc)


def buscar_texto_site(url):
    resposta = requests.get(
        url,
        timeout=10,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0 Safari/537.36"
            )
        },
    )
    resposta.raise_for_status()

    soup = BeautifulSoup(resposta.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    return soup.get_text(separator=" ")


def extrair_palavras(texto):
    return re.findall(r"\w+", texto.lower(), flags=re.UNICODE)


def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def aguardar_voltar_menu():
    input("\nPressione Enter para voltar ao menu...")
    limpar_terminal()


def adicionar_url():
    url = normalizar_url(input("Informe a URL: "))

    if not url_valida(url):
        print("URL invalida.")
        return

    if url in urls_indexadas:
        print("Esta URL ja foi adicionada ao indice.")
        return

    try:
        texto = buscar_texto_site(url)
    except requests.RequestException as erro:
        print(f"Erro ao acessar a URL: {erro}")
        return

    palavras = extrair_palavras(texto)

    if not palavras:
        print("Nenhuma palavra foi encontrada nessa pagina.")
        return

    for palavra in palavras:
        indice_invertido[palavra].add(url)

    urls_indexadas.add(url)
    print(f"URL adicionada com sucesso. {len(set(palavras))} palavras unicas indexadas.")


def consultar():
    texto = input("Informe uma ou mais palavras separadas por virgula: ")
    palavras = [palavra.strip().lower() for palavra in texto.split(",") if palavra.strip()]

    if not palavras:
        print("Digite ao menos uma palavra valida.")
        return

    for palavra in palavras:
        urls = sorted(indice_invertido.get(palavra, set()))

        if not urls:
            print(f"\nA palavra '{palavra}' nao foi encontrada nas URLs indexadas.")
            continue

        print(f"\nA palavra '{palavra}' esta presente em:")
        for url in urls:
            print(f"- {url}")


def exibir_menu():
    print("\n=== Indice Invertido Web ===")
    print("1. Adicionar URL")
    print("2. Consultar")
    print("3. Sair")


def main():
    limpar_terminal()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            adicionar_url()
            aguardar_voltar_menu()
        elif opcao == "2":
            consultar()
            aguardar_voltar_menu()
        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opcao invalida. Tente novamente.")
            aguardar_voltar_menu()


if __name__ == "__main__":
    main()
