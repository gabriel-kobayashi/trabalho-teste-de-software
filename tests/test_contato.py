from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CAMINHO = "file:///C:/trabalho-teste-de-software/app/index.html"


def test_contato_sucesso():

    driver = webdriver.Chrome()

    driver.get(CAMINHO)

    driver.find_element(
        By.ID,
        "nome"
    ).send_keys("Gabriel")

    driver.find_element(
        By.ID,
        "emailContato"
    ).send_keys("gabriel@email.com")

    driver.find_element(
        By.ID,
        "mensagem"
    ).send_keys("Olá")

    botoes = driver.find_elements(
        By.TAG_NAME,
        "button"
    )

    botoes[1].click()

    time.sleep(1)

    resultado = driver.find_element(
        By.ID,
        "resultadoContato"
    ).text

    assert resultado == "Mensagem enviada"

    driver.quit()


def test_contato_vazio():

    driver = webdriver.Chrome()

    driver.get(CAMINHO)

    botoes = driver.find_elements(
        By.TAG_NAME,
        "button"
    )

    botoes[1].click()

    time.sleep(1)

    resultado = driver.find_element(
        By.ID,
        "resultadoContato"
    ).text

    assert resultado == "Preencha todos os campos"

    driver.quit()