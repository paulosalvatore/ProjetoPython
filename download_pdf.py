from urllib.request import urlretrieve

def download_file(download_url):
    urlretrieve(download_url, 'arquivo_salvar.pdf')

download_file("http://www3.camaraserra.es.gov.br/Arquivo/Documents/IND/IND10732018/38656-15561916052018.pdf")
