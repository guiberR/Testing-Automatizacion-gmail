
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# Segun un articulo de internet se modificaron funciones a partir de la v4 
# Razon por la cual es necesario importa las siguientes librerias
# Mas Informacion: https://itsmycode.com/executable-path-has-been-deprecated/
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))

#Inicia la pagina
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fadssettings.google.com%2Fauthenticated%3Fhl%3Des&hl=es&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')


#Rellena los datos de persona
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'input#firstName')))\
    .send_keys('Carlos')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'input#lastName')))\
    .send_keys('jimenez')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'input#username')))\
    .send_keys('rimer.Alvarez2022')
#Rellena los datos de contraseña
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.NAME,
                                    'Passwd')))\
    .send_keys('mzas20147') 
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.NAME,
                                    'ConfirmPasswd')))\
    .send_keys('mzas20147') 

#Hace click en el boton Siguiente
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.NAME,
                                        
                                    '#VfPpkd-RLmnJb')))\
    .click() 
          
  

print ("Done") 
input('Press anything to quit') 
driver.quit() 
print("Finished") 
