#import HtmlTestRunner
#from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from funciones import *
from excel import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from datetime import timedelta
import string

#reporte simple python page3.py
#pytest -v -s --alluredir=C:\SISIA\reportes  C:\SISIA\page3.py

#pytest -v -s --html=report1.html --self-contained-html page3_1.py

#pytest page3_1.py -v --junitxml="page3_1.xml"

#pytest page3.py  page3_2.py  page3_3.py  page3_4.py  page3_5.py  page3_6.py page3_7.py page3_8.py page3_9.py page3_10.py page3_11.py page3_12.py page3_13.py page3_14.py -n 14

#pytest page3.py  page3_2.py  page3_3.py  page3_4.py  page3_5.py -n 5
#pytest page3_6.py page3_7.py page3_8.py page3_9.py page3_10.py -n 5
#pytest page3_11.py page3_12.py page3_13.py page3_14.py page3_15.py -n 5
#pytest page3_16.py page3_17.py page3_18.py page3_19.py page3_20.py -n 5
#pytest page3_21.py page3_22.py page3_23.py page3_24.py page3_25.py -n 5
#pytest page3_26.py page3_27.py page3_28.py page3_29.py page3_30.py -n 5
#pytest page3_31.py page3_32.py page3_33.py page3_34.py page3_35.py -n 5
#pytest page3_36.py  page3_37.py  page3_38.py  page3_39.py  page3_40.py -n 5
#pytest page3_41.py  page3_42.py  page3_43.py  page3_44.py  page3_45.py -n 5
#pytest page3_46.py  page3_47.py  page3_48.py  page3_49.py  page3_50.py -n 5



ren = 4
casos= 4
#ruta="https://prod.senasica.gob.mx/sisia/login"
excel="C://SIPVI//Documentos//Datos.xlsx"
ruta="http://10.16.3.29:8007/login"
t_login=1
tg=.2

#ruta="http://10.16.3.29:8004/login"
#nueva con los id

#Produccion.
#ruta="https://prod.senasica.gob.mx/sisia/login"


class Sisia(unittest.TestCase):


    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        #cls.driver = webdriver.Firefox()
        #cls.driver=webdriver.Ie()
        cls.driver.maximize_window()
        driver = cls.driver
        f = Funciones(driver)
        f.tiempo(2)
        cls.driver.implicitly_wait(15)


    # @unittest.skip("Para pruebas de datos")
    # Primero
    def test01_rastros(self):
        self.driver.implicitly_wait(20)
        driver = self.driver
        f = Funciones(driver)
        fe = Funexcel(driver)
        f.tiempo(.3)
        driver.get(ruta)

        path = excel
        hoja = "Rastros(TIF)"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows):
            user = fe.readData(path, hoja, r, 1)
            passw = fe.readData(path, hoja , r, 2)
            '''
            fecha = fe.readData(path, "Hoja3", r, 12)
            #fecha2 = datetime.now() + timedelta(days=fecha)
            fecha2 = datetime.now()
            fecha2 = fecha2.strftime('%d/%m/%Y')                    
            '''
            # Login
            self.driver.implicitly_wait(5)
            f.tiempo(2)
            f.texto("usuario", user , t_login)
            f.texto("contrasenia", passw , t_login)
            f.Click_xpath("//button[@type='submit']", t_login)

            #Catalogo
            f.Click_xpath("//a[@class='dropdown-toggle'][contains(.,'Catálogos')]", 1)
            f.Click_xpath("//a[@href='/catalogos/cat_rastro']", 1)

            #click Nuevo
            f.tiempo(20)
            f.Click_xpath("//button[contains(.,'Nuevo')]",.5)

            #tipo de Registro TIF
            f.combo_texto_xpath("//select[@formcontrolname='tipoRastro']"," Establecimiento TIF ", .5)
            f.Click_xpath("//button[contains(.,'Siguiente')]", .5)


            #admin de Rastros.
            nom_tif=fe.readData(path, hoja, r, 4)
            num_tif=fe.readData(path, hoja, r, 6)
            rt = random.randint(1, 9)
            correo="demo12"+str(rt)+"@gmail.com"
            telefono="123456789"+ str(rt)
            cp="0799"+str(rt)
            calle=fe.readData(path, hoja, r, 11)
            ne=fe.readData(path, hoja, r, 12)
            ni=fe.readData(path, hoja, r, 12)
            sample_letters = 'ABCDFEGHIJKLOPQRTSRETUIO'
            sample = 'XFTRGERDFRESCDFTYUIOPKASDR'
            rt1 = random.choice(sample_letters)
            rt2 = random.choice(sample)
            curp=str(rt1)+"ASE970124HDFHLR0"+str(rt)
            dias1=random.randint(1, 3)
            dias2=random.randint(4, 7)

            '''
            f.texto_xpath("//input[@placeholder='Nombre del TIF o Rázon sociala']", nom_tif, tg)
            f.texto_xpath("//input[@placeholder='No. TIF']", num_tif, tg)
            f.texto_xpath("//input[@placeholder='Teléfono']", telefono, tg)
            f.texto_xpath("//input[@placeholder='Correo electrónico']",correo, tg)
            f.combo_index_xpath("//select[@formcontrolname='entidad']",rt+1,1)
            f.combo_index_xpath("//select[@formcontrolname='municipio']",rt+2,1)
            f.tiempo(4)
            f.combo_index_xpath("//select[@formcontrolname='localidad']", rt , 1)
            f.texto_xpath("//input[contains(@formcontrolname,'cp')]",cp,tg)
            f.texto_xpath("//input[contains(@formcontrolname,'calle')]",calle,tg)
            f.texto_xpath("//input[contains(@formcontrolname,'exterior')]",ne,tg)
            f.texto_xpath("//input[contains(@formcontrolname,'interior')]",ni,tg)

            #Primer curp
            f.texto_xpath("//input[@formcontrolname='curp']",curp,2)
            f.Click_xpath("(//span[@class='glyphicon glyphicon-search'])[2]",1)
            nomM = fe.readData(path, hoja, r, 38)
            apM = fe.readData(path, hoja, r, 39)
            amM = fe.readData(path, hoja, r, 40)
            val_curp1=f.existe_try_xpath("(//div[contains(.,'×La estructura de la CURP es incorrecta.')])[4]",1)
            #validando error del curp
            while val_curp1 == "Existe":
                rt2= random.randint(3, 7)
                curp = str(rt1) + str(rt2) + "SE970123HDFLLR0" + str(rt2)
                f.texto_xpath("//input[@formcontrolname='curp']", curp, 2)
                f.Click_xpath("(//span[@class='glyphicon glyphicon-search'])[2]", 1)

            #si no esta registrado
            cur1 = f.existe_try_xpath("(//div[contains(.,'×La CURP no se encontró, capture la información de la persona.')])[4]", 1)
            if cur1 == "Existe":
                f.texto_xpath("//input[@formcontrolname='nombre']", nomM, 1)
                f.texto_xpath("//input[@formcontrolname='paterno']", apM, 1)
                f.texto_xpath("//input[@formcontrolname='materno']", amM, 1)
           



            f.combo_index_xpath("/html/body/app-root/div/app-catalogos-principal/app-cat-rastros/div[2]/div/div/div[3]/div[24]/div/select",1,tg)
            f.combo_index_xpath("/html/body/app-root/div/app-catalogos-principal/app-cat-rastros/div[2]/div/div/div[3]/div[24]/div/select",2,tg)
            f.combo_index_xpath("/html/body/app-root/div/app-catalogos-principal/app-cat-rastros/div[2]/div/div/div[3]/div[24]/div/select",3,tg)
            f.Click_xpath("(//button[contains(.,'Agregar')])[1]",1)





            #Horarios
            #f.Click_xpath("(//input[contains(@type,'checkbox')])['str(dias1)']",3)
            #f.Click_xpath("(//input[contains(@type,'checkbox')])['str(dias2)']",3)

            '''


            #Medico
            nomM = fe.readData(path, hoja, r, 38)
            apM = fe.readData(path, hoja, r, 39)
            amM = fe.readData(path, hoja, r, 40)
            curp2 = str(rt1) + "ISE970124HDFLLR0" + str(rt1)
            f.texto_xpath("//input[contains(@formcontrolname,'curpM')]", curp2, tg )
            f.Click_xpath("(//span[contains(@class,'glyphicon glyphicon-search')])[4]",1)
            f.tiempo(1)

            #Fallo el curp
            val_curp2 = f.existe_try_css("alert-danger", 1)


            # validando error del curp
            while val_curp2 == "Existe":
                f.tiempo(20)
                rt2 = random.randint(3, 7)
                curp2 = str(rt1)  + "ISE970124HDFLLR0" + str(rt2)
                f.texto_xpath("//input[contains(@formcontrolname,'curpM')]", curp2, tg)
                f.Click_xpath("(//span[contains(@class,'glyphicon glyphicon-search')])[4]", 1)



            # insertar datos
            Curp_error = f.existe_try_css2("alert-warning", 1)
            if  Curp_error == "Encontrado":
                #f.texto_xpath("//input[contains(@formcontrolname,'curpM')]", curp2, tg)
                f.texto_xpath("//input[@formcontrolname='nombreM']", nomM + rt2, tg)
                f.texto_xpath("//input[@formcontrolname='paternoM']", apM + rt2, tg)
                f.texto_xpath("//input[contains(@formcontrolname,'maternoM')]", amM + rt2, tg)


            if (r == casos):
                break



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Terminan las Pruebas ok")



if  __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Resultados Test"))







