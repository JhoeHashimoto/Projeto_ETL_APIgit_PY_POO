import requests
import base64


##CODIGO COM A CLASSE IMPLEMENTADA
class ManipulaRepositorios:

    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.headers = {'Authorization': 'Bearer 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',
                        'X-GitHub-Api-Version': '2022-11-28'
}
        
    def cria_repo(self, nome_repo):
        data = {
            "name": nome_repo,
            "description": "Dados dos repositórios de algumas empresas",
            "private": False
        }
        response = requests.post(f"{self.api_base_url}/user/repos", 
                                 json=data, headers=self.headers)

        print(f'status_code criação do repositório: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):

        # Codificando o arquivo
        with open(caminho_arquivo, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)

        # Realizando o upload
        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
        data = {
            "message": "Adicionando um novo arquivo",
            "content": encoded_content.decode("utf-8")
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code upload do arquivo: {response.status_code}')


    # def add_PROJETO(self, nome_repo, nome_arquivo, caminho_arquivo):

    #     # Realizando o upload
    #     url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
    #     data = {
    #         "message": "Adicionando um novo arquivo",
    #         "content": nome_arquivo
    #     }

    #     response = requests.put(url, json=data, headers=self.headers)
    #     print(f'status_code upload do arquivo: {response.status_code}')
        


# instanciando um objeto
x = input('Digite o login do usuário git:')
novo_repo = ManipulaRepositorios(x)

# Criando o repositório
nome_repo = input('Digite o nome do repositório a ser criado: ')
novo_repo.cria_repo(nome_repo)

# Adicionando arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')

#Upando o projeto

# novo_repo.add_PROJETO(nome_repo, 'dados_repos.py', 'Projeto_Request/dados_repos.py')
# novo_repo.add_PROJETO(nome_repo, 'linguagens_repos_aula1.ipynb', 'Projeto_Request/linguagens_repos_aula1.ipynb')
# novo_repo.add_PROJETO(nome_repo, 'manipula_dados.py', 'Projeto_Request/manipula_dados.py')

