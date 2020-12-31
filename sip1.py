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
        self.driver.implicitly_wait(15)
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
          
            mision = fe.readData(path, "Hoja3", r, 10)
            vision = fe.readData(path, "Hoja3", r, 11)
            fecha = fe.readData(path, "Hoja3", r, 12)
            #fecha2 = datetime.now() + timedelta(days=fecha)
            fecha2 = datetime.now()
            fecha2 = fecha2.strftime('%d/%m/%Y')
            fecha3 = datetime.now()
            fecha4 = fecha3.strftime('%d/%m/%Y')
            registro = str(fe.readData(path, "Hoja3", r, 13))
            telefono = str(fe.readData(path, "Hoja3", r, 14))
            sample_letters = 'ABCDFEGHIJKLOPQRTSRETUIO'
            sample = 'XFTRGERDFRESCDFTYUIOPKASDR'
            rt = random.choice(sample_letters)
            rt2 = random.choice(sample)
            raa = random.randint(1, 9)
            ra1 = random.randint(1, 9)
            rfc = str(fe.readData(path, "Hoja3", r, 15))
            rfcc = rfc + str(ra1)+ rt + str(raa)
            curpp = str("SENASICA/01-31/2019")
            # curpp = curp + rt + str(r)
            presidente = str(fe.readData(path, "Hoja3", r, 17))
            secretario = str(fe.readData(path, "Hoja3", r, 18))
            tesorero = str(fe.readData(path, "Hoja3", r, 19))
            pdf1 = str(fe.readData(path, "Hoja3", r, 20))
            pdf2 = str(fe.readData(path, "Hoja3", r, 21))
            pdf3 = str(fe.readData(path, "Hoja3", r, 22))
            '''
            # Login
            self.driver.implicitly_wait(5)
            f.tiempo(2)
            f.texto_xpath("//input[contains(@id,'usuario')]", user , t_login)
            f.texto_xpath("//input[contains(@id,'contrasenia')]", passw , t_login)
            f.Click_xpath("//button[@type='submit']", t_login)

            #Catalogo
            f.Click_xpath("//a[@class='dropdown-toggle'][contains(.,'Catálogos')]", 1)
            f.Click_xpath("//a[@href='/catalogos/cat_rastro']",1)

            #click Nuevo
            f.tiempo(6)
            f.Click_xpath("//button[contains(.,'Nuevo')]",2)

            #tipo de Registro TIF
            f.combo_texto_xpath("//select[@formcontrolname='tipoRastro']"," Establecimiento TIF ", 2)
            f.Click_xpath("//button[contains(.,'Siguiente')]", 1)
            f.tiempo(4)


            '''
            f.Click("sisiaMenu_menu_621")
            f.Click("sisiaMenu_subMenu_622")


            # DATOS IE
            self.driver.implicitly_wait(10)
            f.tiempo(5)
            f.Click_oculto("tab_recursosHumanosMateriales")
            self.driver.implicitly_wait(10)
            f.tiempo(5)
            f.texto("datosIE_mision", mision)
            f.texto("datosIE_vision", vision)
            f.texto("datosIE_fechaA", fecha2)
            f.combo_texto("datosIE_anio",registro)
            f.texto("datosIE_tel", telefono)
            #cambios
            f.texto("datosIE_rfc",rfcc)
            f.texto("datosIE_clave", curpp)
            f.texto("datosIE_presidente", presidente)
            f.texto("datosIE_secretario", secretario)
            f.texto("datosIE_tesorero", tesorero)
            f.scrolling(150)
            driver.implicitly_wait(2)
            pdf = f.existe_try("datosIE_docActaConst")
            print(pdf)
            if (pdf == "Existe"):
                f.upload("datosIE_docActaConst", pdf1)
                f.upload("datosIE_docActaMesa", pdf2)
                f.upload("datosIE_docOficio", pdf3)
                f.tiempo(2)
                f.Click("datosIE_buttonSave")
                f.tiempo(28)
                f.Click("datosIE_modalOk")
                self.driver.implicitly_wait(5)
                f.tiempo(5)
                f.Click("infUsuari_logout")
                f.tiempo(1)
            print("Valor de R: " + str(r))
            if(r == casos):
                break

            elif (pdf == "Falso"):
                f.tiempo(1)
                f.Click("datosIE_buttonSave")
                f.tiempo(4)
                f.Click("datosIE_modalOk")
                self.driver.implicitly_wait(5)
                f.tiempo(5)
                f.Click("infUsuari_logout")
                f.tiempo(1)
            print("Valor de R: " + str(r))
            if (r == casos):
                break




    #ok listo
    #@unittest.skip("Para pruebas de personas")
    def test02_persona(self):
        self.driver.implicitly_wait(30)
        driver = self.driver
        driver.get(ruta)
        f = Funciones(driver)
        fe = Funexcel(driver)
        f.tiempo(2)
        path = excel
        hoja = "Hoja3"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, "Hoja3", r, 1)
            passw = fe.readData(path, "Hoja3", r, 9)
            # Seccion Personal
            nom = str(fe.readData(path, "Hoja3", r, 23))
            ap = str(fe.readData(path, "Hoja3", r, 24))
            am = str(fe.readData(path, "Hoja3", r, 25))
            email = str(fe.readData(path, "Hoja3", r, 26))
            puesto = str(fe.readData(path, "Hoja3", r, 27))
            costo = str(fe.readData(path, "Hoja3", r, 28))
            laboral = str(fe.readData(path, "Hoja3", r, 29))
            telefono = str(fe.readData(path, "Hoja3", r, 14))
            sample_letters = 'ABCDFEGHIJKLOPQRTSRETUIO'
            sample = 'XFTRGERDFRESCDFTYUIOPKASDR'
            rt = random.choice(sample_letters)
            rt2 = random.choice(sample)
            ra = random.randint(1, 9)
            ra1 = random.randint(1, 9)
            rfc = str(fe.readData(path, "Hoja3", r, 15))
            rfcc = rfc + str(ra1) + rt + str(ra)
            curp = str(fe.readData(path, "Hoja3", r, 16))
            curpp = curp + rt + str(ra)

            # Login
            self.driver.implicitly_wait(10)
            f.tiempo(5)
            f.texto("username", user)
            f.texto("password", passw)
            f.Click("login_iniciarBtn")
            f.Click("sisiaMenu_menu_621")
            f.Click("sisiaMenu_subMenu_622")

            # Sección personal
            self.driver.implicitly_wait(10)
            f.tiempo(5)
            f.Click_oculto("tab_personal")
            self.driver.implicitly_wait(10)
            f.tiempo(5)
            f.texto("personal_nombre", nom)
            f.texto("personal_apellidoPat", ap)
            f.texto("personal_apellidoMat", am)
            f.texto("personal_rfc", rfcc)
            f.texto("personal_curp", curpp)
            f.texto("personal_correo", email)
            f.texto("personal_tel", telefono)
            #f.scrolling(550)
            #f.tiempo(1)
            f.combo_index("personal_puesto", puesto)
            f.combo_index("personal_ubicLab", laboral)
            f.texto("personal_costMes", costo)
            f.Click("personal_agregarBtn")
            driver.implicitly_wait(8)
            f.tiempo(8)
            v = f.existe_try("personal_modalOK")
            if (v == "Existe"):
                f.Click("personal_modalOK")
                f.tiempo(1)
                f.Click("personal_saveBtn")
                self.driver.implicitly_wait(5)
                f.tiempo(5)
                f.Click("infUsuari_logout")
                f.tiempo(1)

            print("Valor de R: " + str(r))
            if (r == casos):
                break

   
            '''





    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Terminan las Pruebas ok")



if  __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Resultados Test"))







