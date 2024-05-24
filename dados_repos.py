import requests
import pandas as pd
from math import ceil

class DadosRepositorios:     #         INSTANCIANDO A CLASSE


    def __init__(self, owner):      #   OBJETO CONSTRUTOR COM OS ATRIBUTOS
        self.onwer = owner           #owner é o nome de login
        self.api_base_url = 'https://api.github.com'
        self.headers = {
                        'Authorization': 'Bearer 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',
                        'X-GitHub-Api-Version': '2022-11-28'
}
        
    def lista_repositorios(self):
        repos_list = []

        #calculando a quantidade de paginas
        response = requests.get(f'https://api.github.com/users/{self.onwer}')
        num_pages = ceil(response.json()['public_repos']/30)   #bib math arredonda pra cima divide a quantidade de de repos por 30

        for page_num in range(1, num_pages):

            try:
                url = f'{self.api_base_url}/users/{self.onwer}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        
        return repos_list
    

    def nomes_repos (sel, repos_list):
        repo_names= []
        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])

                except:
                    pass

        return repo_names

    def nomes_linguagens(self, repos_list):    #Paginação
        repo_languages = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo['language'])
                except:
                    pass

        return repo_languages
    
    def cria_df_linguagens(self):  #criando o dataframe

        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens

        return dados
    


amazon_rep = DadosRepositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()
#print(ling_mais_usadas_amzn)

netflix_rep = DadosRepositorios('netflix')
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()
#print(ling_mais_usadas_netflix)

spotify_rep = DadosRepositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()
#print(ling_mais_usadas_spotify)



#Salvando os dados

ling_mais_usadas_amzn.to_csv('dados/linguagens_amzn.csv')
ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv')
ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv')