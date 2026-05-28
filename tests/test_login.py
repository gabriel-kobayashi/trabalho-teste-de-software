from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CAMINHO = "file:///C:/trabalho-teste-de-software/app/index.html"


def test_login_sucesso():

    driver = webdriver.Chrome()

    driver.get(CAMINHO)

    driver.find_element(
        By.ID,
        "email"
    ).send_keys("admin@email.com")

    driver.find_element(
        By.ID,
        "senha"
    ).send_keys("123456")

    driver.find_element(
        By.TAG_NAME,
        "button"
    ).click()

    time.sleep(1)

    resultado = driver.find_element(
        By.ID,
        "resultadoLogin"
    ).text

    assert resultado == "Login realizado"

    driver.quit()


def test_login_invalido():

    driver = webdriver.Chrome()

    driver.get(CAMINHO)

    driver.find_element(
        By.ID,
        "email"
    ).send_keys("teste@email.com")

    driver.find_element(
        By.ID,
        "senha"
    ).send_keys("111")

    driver.find_element(
        By.TAG_NAME,
        "button"
    ).click()

    time.sleep(1)

    resultado = driver.find_element(
        By.ID,
        "resultadoLogin"
    ).text

    assert resultado == "Login inválido"

    driver.quit()


def test_login_campos_vazios():

    driver = webdriver.Chrome()

    driver.get(CAMINHO)

    driver.find_element(
        By.TAG_NAME,
        "button"
    ).click()

    time.sleep(1)

    resultado = driver.find_element(
        By.ID,
        "resultadoLogin"
    ).text

    assert resultado == "Campos obrigatórios"

    driver.quit()