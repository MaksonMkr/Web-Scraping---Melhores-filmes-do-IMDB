from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

# Configuração do WebDriver para Chrome
driver = webdriver.Chrome()

# Acessando a página
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
driver.get(url)

# Lista para armazenar os filmes e suas respectivas notas
nomes_filmes = []
notas_filmes = []

# Esperar o carregamento do conteúdo da página
time.sleep(5)

# Pegar o elemento principal da lista de filmes
filmes = driver.find_elements(By.CSS_SELECTOR, "div.ipc-metadata-list-summary-item__c")

# Rolar a página até o final para carregar todo o conteúdo
action = ActionChains(driver)
scroll_pause_time = 2

while True:
    for filme in filmes:
        nome = filme.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text
        nota = filme.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--rating").text

        nomes_filmes.append(nome)
        notas_filmes.append(nota)
    
    # Verificar se chegou ao fim da página
    try:
        driver.find_element(By.CSS_SELECTOR, "footer")
        break
    except:
        action.send_keys(Keys.END).perform()
        time.sleep(scroll_pause_time)

# Criar DataFrame
df = pd.DataFrame({
    'Nome': nomes_filmes,
    'Nota': notas_filmes
})

print(df)

# Fechar o WebDriver
driver.quit()
