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
casos= 5
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
    def test01_Grupo_mercancia(self):
        self.driver.implicitly_wait(20)
        driver = self.driver
        f = Funciones(driver)
        fe = Funexcel(driver)
        f.tiempo(.3)
        driver.get(ruta)

        path = excel
        hoja = "Sitio_inspeccion"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows):
            user = fe.readData(path, hoja, r, 1)
            passw = fe.readData(path, hoja , r, 2)
            gm = fe.readData(path, hoja, r, 3)
            cm = fe.readData(path, hoja, r, 4)

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
            f.Click("id_menu_catalogos", 1)
            f.Click("id_menu_cat_sitios_inspeccion", 1)

            #click Nuevo
            f.tiempo(4)
            f.Click("SitiosInspeccion__btn-nuevo",.5)

            #Administración de Inspección
            ra1 = random.randint(1, 12)
            ra2 = random.randint(1, 9)
            ra3 = random.randint(6, 8)
            ca = fe.readData(path, hoja, r, 3)
            nom = fe.readData(path, hoja, r, 4)
            tip = fe.readData(path, hoja, r, 5)
            Dom = fe.readData(path, hoja, r, 6)
            nk = fe.readData(path, hoja, r, 7)
            Ejex = fe.readData(path, hoja, r, 18)
            Ejex=str(Ejex)
            Ejey = fe.readData(path, hoja, r, 19)
            Ejey=str(Ejey)




            #Fase 1
            f.texto("claveAutorizacionForm", ca, .5)
            f.texto("Nombre",nom, .3)
            f.combo_index("tipoSitioInspeccionForm", tip, 2)
            f.texto("domicilioCarretera",Dom, .3)
            f.texto("numeroKm", nk, .2)
            f.combo_index("estado", ra1, 1)
            f.combo_index("municipio", ra2, 1)
            f.texto("coordenadas__ejeX", Ejex, .5)
            f.texto("coordenadas__ejeY", Ejey, .5)

            #Fase 2
            Ofa = fe.readData(path, hoja, r, 20)
            Ofc = fe.readData(path, hoja, r, 22)

            fecha1 = datetime.now()
            fecha1 = fecha1.strftime('%d/%m/%Y')
            fecha2 = datetime.now() + timedelta(days=10)
            fecha2 = fecha2.strftime('%d/%m/%Y')
            f.texto("oficioAutorizacion",Ofa, .5)
            f.texto("fechaAutorizacion", fecha1, .6)
            f.texto("oficioCancelacion", Ofc, .5)
            f.texto("fechaCancelacion", fecha2, 3)

            #Materia.
            ra1 = random.randint(1, 3)
            ra2 = random.randint(4, 6)
            ra3 = random.randint(6, 8)
            f.combo_index("materia", ra1, .1)
            f.combo_index("materia", ra2, .1)
            f.combo_index("materia", ra3, .1)
            f.Click("materias_btn-agregar",.5)

            #Servicios
            f.combo_index("servicio", ra1, .1)
            f.combo_index("servicio", ra2, .1)
            f.combo_index("servicio", ra3, .1)
            f.Click("servicio__btn-agregar", .5)

            #Observaciones
            Obs = fe.readData(path, hoja, r, 26)
            f.texto("observaciones", Obs, .2)

            f.tiempo(3)

            f.Click("id_salir_sipvi", .1)


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







