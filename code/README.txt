README - Indice Invertido com Web Scraping

Este projeto contem um script Python chamado IVWebScrapping.py. O programa roda no terminal, acessa URLs informadas pelo usuario, extrai o texto das paginas e monta um indice invertido para consulta de palavras.


1. Requisitos

Para executar o projeto, e necessario ter:

- Python 3 instalado
- Acesso ao terminal
- Conexao com a internet para acessar as URLs


2. Verificar se o Python esta instalado

Abra o terminal na pasta do projeto e execute:

python --version

Se o Python estiver instalado, sera exibida a versao, por exemplo:

Python 3.12.0

Caso o comando nao funcione, tente:

py --version


3. Instalar as dependencias

O script utiliza as bibliotecas requests e BeautifulSoup. Para instalar, execute no terminal COMO ADMINISTRADOR:

pip install requests beautifulsoup4

Caso o comando pip nao funcione, tente:

python -m pip install requests beautifulsoup4

Ou, no Windows:

py -m pip install requests beautifulsoup4


4. Executar o programa

Depois de instalar as dependencias, execute o script com:

python IVWebScrapping.py

Se estiver no Windows e o comando acima nao funcionar, tente:

py IVWebScrapping.py


5. Como usar o programa

Ao executar o script, sera exibido um menu com as opcoes:

1. Adicionar URL
2. Consultar
3. Sair


6. Adicionar uma URL

Escolha a opcao 1 e informe uma URL de site.

Exemplo:

https://www.python.org

O programa acessara o site, extraira o texto da pagina e adicionara as palavras encontradas ao indice invertido.


7. Consultar palavras

Escolha a opcao 2 e informe uma ou mais palavras separadas por virgula.

Exemplo:

python, download, documentation

O programa mostrara em quais URLs indexadas cada palavra foi encontrada.


8. Voltar ao menu

Apos cada operacao, o programa pede para pressionar Enter para voltar ao menu. Antes de exibir o menu novamente, o terminal sera limpo.


9. Encerrar o programa

Para finalizar, escolha a opcao 3 no menu.


10. Observacoes

O indice invertido e armazenado apenas em memoria. Isso significa que, ao fechar o programa, as URLs e palavras indexadas serao perdidas.

Alguns sites podem bloquear requisicoes automaticas ou demorar para responder. Nesses casos, o programa exibira uma mensagem de erro.
