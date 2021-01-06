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
            f.Click("id_menu_catalogos", 1)
            f.Click("id_menu_cat_rastros", 1)

            #click Nuevo
            f.tiempo(15)
            f.Click("id_btn_nuevo",.5)

            #tipo de Registro TIF
            f.combo_texto("id_tipo_rastro", "Establecimiento TIF",.5)
            f.Click("id_btn_siguiente", .5)


            #admin de Rastros.
            nom_tif=fe.readData(path, hoja, r, 4)
            num_tif=fe.readData(path, hoja, r, 6)
            rt = random.randint(1, 9)
            correo="demo12"+str(rt)+"@gmail.com"
            telefono="123456789"+ str(rt)
            cp="0799"+str(rt)
            calle=fe.readData(path, hoja, r, 11)
            ne=fe.readData(path, hoja, r, 12)
            ni=fe.readData(path, hoja, r, 13)
            sample_letters = 'ABCDFEGHIJKLOPQRTSRETUIO'
            sample = 'XFTRGERDFRESCDFTYUIOPKASDR'
            rt1 = random.choice(sample_letters)
            rt2 = random.choice(sample)
            curp=str(rt1)+"ASE970124HDFHLR0"+str(rt)
            dias1=random.randint(1, 3)
            dias2=random.randint(4, 7)

            #Representante Legal
            f.texto("id_razon_social_tif", nom_tif, tg)
            f.texto("id_ntif",num_tif, tg)
            f.texto("id_telefono", telefono, tg)
            f.texto("id_correo_electronico",correo, tg)
            f.combo_index("id_entidad",rt+1,1)
            f.combo_index("id_municipio",rt+2,1)
            f.tiempo(4)
            f.combo_index("id_localidad", rt , 1)
            f.texto("id_cp",cp,tg)
            f.texto("id_calle",calle,tg)
            f.texto("id_numero_exterior",ne,tg)
            f.texto("id_numero_interior",ni,tg)



            #Primer curp
            f.texto("id_curp",curp,2)
            f.Click("id_btn_curp",1)
            nomM = fe.readData(path, hoja, r, 38)
            apM = fe.readData(path, hoja, r, 39)
            amM = fe.readData(path, hoja, r, 40)
            val_curp1=f.existe_try_id("id_alert_danger",1)
            #validando error del curp
            while val_curp1 == "Existe":
                rt2= random.randint(3, 7)
                curp = str(rt1) + str(rt2) + "SE970123HDFLLR0" + str(rt2)
                f.texto("id_curp", curp, 2)
                f.Click("id_btn_curp", 1)

            #si no esta registrado
            cur1 = f.existe_try_id("id_alert_warning", 1)
            if cur1 == "Existe":
                f.texto("id_nombre", nomM, 1)
                f.texto("id_paterno", apM, 1)
                f.texto("id_materno", amM, 1)


            #Combox, Especies
            f.combo_index_id("id_especies_disponibles",1,tg)
            f.combo_index_id("id_especies_disponibles",2,tg)
            f.combo_index_id("id_especies_disponibles",3,tg)
            f.Click("id_btn_agregar_e",1)


            #Horarios
            f.Click("id_check_horario_Lunes",1)
            f.Click_xpath("(//input[@placeholder='HH:MM'])[1]",1)
            f.Click_xpath("//*[@id='cdk-overlay-0']/nz-time-picker-panel/div/div/div[2]/div[1]/ul/li[12]",1)
            f.Click_xpath("//*[@id='cdk-overlay-0']/nz-time-picker-panel/div/div/div[2]/div[2]/ul/li[1]",1)
            sample_letters = 'ABCDFEGHIJKLOPQRTSRETUIO'
            sample_letters2 = 'AABBCDFTEYGDUHDINDIDNFMPJOKLOPQCRTSCRECTUIZODS'
            rt1 = random.choice(sample_letters)
            rt2 = random.choice(sample_letters2)
            rfc = str(rt1) + "ECJ971112HM" + str(rt2)
            f.texto("id_rfc_m", rfc, .5)
            f.Click_oculto("id_btn_rfc_m", 1)
            f.limpiar("id_rfc_m",1)

            f.Click_xpath("(//input[@placeholder='HH:MM'])[2]",1)
            f.Click_xpath("(//li[contains(.,'15')])[1]",1)
            f.Click_xpath("(//li[contains(.,'04')])[2]",1)
            f.texto("id_rfc_m", rfc, .5)
            f.Click_oculto("id_btn_rfc_m", .5)
            f.limpiar("id_rfc_m", .5)



            #Medico

            nomM = fe.readData(path, hoja, r, 38)
            apM = fe.readData(path, hoja, r, 39)
            amM = fe.readData(path, hoja, r, 40)
            rfc = str(rt1) + "ECJ971112HM" + str(rt2)
            f.texto("id_rfc_m", rfc, 2 )
            f.Click_oculto("id_btn_rfc_m",1)

            #Fallo el curp
            val_rfc = f.existe_try_id("alert-danger", 1)
            # validando error del curp
            while val_rfc == "Existe":
                sample_letters = 'ABCDFEGHIRTJKLOPYUIOYTREDFERTYHQRTSRETUIO'
                sample_letters2 = 'AABBCDFTEYGDUHDINDIDNFMPJOKLOPQCRTSCRECTUIZODS'
                rt1 = random.choice(sample_letters)
                rt2 = random.choice(sample_letters2)
                rfc = str(rt1) + "ECJ971112HM" + str(rt2)
                f.texto("id_rfc_m", rfc, 2)
                f.Click_oculto("id_btn_rfc_m", 1)



            # insertar datos
            Rfc_error = f.existe_try_id("id_alert_warning", 1)
            if  Rfc_error == "Existe":
                #f.texto_xpath("//input[contains(@formcontrolname,'curpM')]", curp2, tg)
                f.texto("id_nombre_m", nomM + "-Medico", tg)
                f.texto("id_paterno_m", apM + "-Medico", tg)
                f.texto("id_materno_m", amM + "-Medico", tg)


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







