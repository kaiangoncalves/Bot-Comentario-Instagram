from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import usuario
import random

login = usuario.login_usuario
navegador = webdriver.Chrome()
wait = WebDriverWait(navegador, 10, 1)

def executar_login():
    navegador.get("https://www.instagram.com")
    time.sleep(3)
    campo_usuario = navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    campo_usuario.click()
    time.sleep(1)
    campo_usuario.send_keys(login['usuario'])
    time.sleep(1)
    campo_senha = navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    campo_senha.click()
    time.sleep(1)
    campo_senha.send_keys(login['senha'])
    time.sleep(3)
    campo_senha.send_keys(Keys.ENTER)
    time.sleep(10)

def inserir_comentario(repeticoes):  #pausa
    for x in range(repeticoes):
        navegador.get('INSIRA AQUI O LINK DO SORTEIO')
        time.sleep(4)
        campo_comentario = wait.until( 
            expected_conditions.element_to_be_clickable(
                (By.XPATH,'//div[@class="RxpZH"]')
            )
        )
        campo_comentario.click()
        campo_comentario = wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, '//textarea[@placeholder="Add a comment…"]')
            )
        )
        for letra in x:
            campo_comentario.send_keys(letra)
            time.sleep(60 / random.randint(160,300))
        botao_publicar = wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, '//button[@type="submit"]')
            )
        )
        botao_publicar.click()
        #campo_comentario.send_keys(comentario)  
        #campo_comentario.send_keys(Keys.ENTER)
        #time.sleep(10)

def inserir_comentario_lista(lista_contatos,pausa_padrao,numero_comentarios,pausa_entre_comentarios):
    comentarios_postados=0
    for contato in lista_contatos:
        navegador.get('LINK DO SORTEIO NOVAMENTE')
        time.sleep(4)
        campo_comentario = wait.until( 
            expected_conditions.element_to_be_clickable(
                (By.XPATH,'//div[@class="RxpZH"]')
            )
        )
        campo_comentario.click()
        campo_comentario = wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, '//textarea[@placeholder="Add a comment…"]')
            )
        )
        for letra in contato:
            campo_comentario.send_keys(letra)
            time.sleep(60 / random.randint(160,300))
        botao_publicar = wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, '//button[@type="submit"]')
            )
        )
        botao_publicar.click()
        comentarios_postados+=1
        if comentarios_postados==numero_comentarios:
            print(numero_comentarios, 'postados. Vamos aguardar',pausa_entre_comentarios,'segundos')
            time.sleep(pausa_entre_comentarios)
            comentarios_postados=0
        else:    
            time.sleep(pausa_padrao)
        



def carregar_contatos(arquivo,n_marcacoes):
    contatos = open(arquivo,'r',encoding='UTF-8')
    lista_contatos = contatos.read()
    lista_contatos = lista_contatos.split('\n')
    contatos_formatados=[]
    linha_atual=1
    proxima_linha=-1
    contador=0
    contato_formatado=''
    for contato in lista_contatos:
        if contato[0:4] == 'Foto':
            proxima_linha=linha_atual+1
        elif proxima_linha == linha_atual:
            contador+=1
            if len(contato_formatado)>0:
                contato_formatado+='@'+contato+' '
            else:
                contato_formatado='@'+contato+' '  
        if contador == n_marcacoes:      
            contatos_formatados.append(contato_formatado)
            contador=0
            contato_formatado=''

        linha_atual+=1

    return contatos_formatados  
n_marcacoes=1
pausa_padrao=35
numero_comentarios=45
pausa_entre_comentarios=600

contatos=carregar_contatos('contatos.txt', n_marcacoes)
print(contatos)         


login = usuario.login_usuario
navegador = webdriver.Chrome()
wait = WebDriverWait(navegador, 10, 1)
executar_login()
#inserir_comentario('quero ganhar',5)


inserir_comentario_lista(contatos,pausa_padrao,numero_comentarios,pausa_entre_comentarios)