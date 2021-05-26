from data_processing.create_table import create_pettyTable
from scraping.scrapy_data_full import get_data_repository_full


class CompileRepo:
    def __init__(self, repo):
        self.url_git = 'https://github.com'
        # Realiza a procura de todos os arquivos retornando em um dicionario
        data = get_data_repository_full(repo, self)
        # convoca a função que cria a tabela e exibe a mesma
        create_pettyTable(repo, data, self)

        print('\n' * 2)


if __name__ == '__main__':
    CompileRepo('Erickson-lopes-dev/Compile-Repo')
