from data_processing.create_table import create_pettyTable
from scraping.scrapy_data_full import get_data_repository_full


class CompileRepo:
    def __init__(self, repo):
        # Realiza a procura de todos os arquivos retornando em um dicionario
        data = get_data_repository_full(repo)
        print(data)
        # convoca a função que cria a tabela e exibe a mesma
        create_pettyTable(repo, data)

        print('\n' * 2)


if __name__ == '__main__':
    CompileRepo('Erickson-lopes-dev/Compile-Repo')
