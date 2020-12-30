import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class Funciones():
    def __init__(self, driver):
        self.driver = driver

        self.name = "(//input[contains(@type,'text')])[2]"
        self.password = "//input[contains(@id,'txtPassword')]"
        self.button = "//input[contains(@id,'btnLogin')]"

    def login(self, name, password):
        self.driver.find_element_by_xpath(self.name).send_keys(name)
        self.driver.find_element_by_xpath(self.password).send_keys(password)
        self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//login.png")
        self.driver.find_element_by_xpath(self.button).click()

    def texto_xpath(self, xpath, texto, tiempo):
        ##r = random.randint(1, 1000)
        t = self.driver.find_element_by_xpath(xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(t).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(tiempo)
        t = self.driver.find_element_by_xpath(xpath).clear()
        t = self.driver.find_element_by_xpath(xpath).send_keys(texto)
        print("Campo: "+str(xpath)+"--> Dato: "+str(texto))
        #self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//texto" + str(r) + ".png")
        return t

    def texto(self, id, texto):
        t = self.driver.find_element_by_id(id)
        actions = ActionChains(self.driver)
        actions.move_to_element(t).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(.5)
        t = self.driver.find_element_by_id(id).clear()

        t = self.driver.find_element_by_id(id).send_keys(texto)
        print("Campo: "+str(id)+"--> Dato: "+str(texto))
        #self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//texto" + str(r) + ".png")
        return t
    

    def Click_xpath(self, xpath, tiempo):
        e = self.driver.find_element_by_xpath(xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(e).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(.5)
        print("Boton nom: "+ str(xpath))
        time.sleep(tiempo)
        elemento = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        time.sleep(tiempo)
        elemento = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        #elemento = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
        try:
            elemento = self.driver.find_element_by_xpath(xpath).click()
            #elemento = self.driver.find_element_by_xpath(xpath).send_Keys(Keys.RETURN)
            print("Boton Presionado Ok: "+str(xpath))
            return e
        except NoSuchElementException:
            print("Boton Fallo: " + str(xpath))

    def Click(self, id):
        e = self.driver.find_element_by_id(id)
        actions = ActionChains(self.driver)
        actions.move_to_element(e).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(.5)
        print("Boton nom: "+ str(id))
        time.sleep(.5)
        elemento = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, id)))
        time.sleep(.5)
        elemento = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, id)))
        #elemento = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
        try:
            elemento = self.driver.find_element_by_id(id).click()
            #elemento = self.driver.find_element_by_xpath(xpath).send_Keys(Keys.RETURN)
            print("Boton Presionado Ok: "+str(id))
            return e
        except NoSuchElementException:
            print("Boton Fallo: " + str(id))

        # Click Oculto bueno

    def Click_oculto_xpath(self, xpath):
        e = self.driver.find_element_by_xpath(xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(e).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(.5)
        print("Boton nom: " + str(xpath))
        time.sleep(1)
        elemento = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        time.sleep(1)
        elemento = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        # elemento = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
        try:
            action = ActionChains(self.driver)
            action.move_to_element(elemento).click().perform()
            # elemento = self.driver.find_element_by_xpath(xpath).click()
            # elemento = self.driver.find_element_by_xpath(xpath).send_Keys(Keys.ENTER)
            print("Boton Presionado Ok: " + str(xpath))
            return e
        except NoSuchElementException:
            print("Boton Fallo: " + str(xpath))


    #Click Oculto bueno
    def Click_oculto(self, id):
        e = self.driver.find_element_by_id(id)
        actions = ActionChains(self.driver)
        actions.move_to_element(e).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(.5)
        print("Boton nom: "+ str(id))
        time.sleep(1)
        elemento = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, id)))
        time.sleep(1)
        elemento = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, id)))
        #elemento = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
        try:
            action = ActionChains(self.driver)
            action.move_to_element(elemento).click().perform()
            #elemento = self.driver.find_element_by_xpath(xpath).click()
            #elemento = self.driver.find_element_by_xpath(xpath).send_Keys(Keys.ENTER)
            print("Boton Presionado Ok: "+str(id))
            return e
        except NoSuchElementException:
            print("Boton Fallo: " + str(id))




    def Click_css(self, css):
        e = self.driver.find_element_by_css_selector(css).click()
        return e

    def Enter(self, xpath):
        '''
        ct = self.driver.find_element_by_xpath(xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(ct).perform()
        time.sleep(1)
        '''
        ct = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        cte = self.driver.find_element_by_xpath(xpath).send_keys(Keys.ENTER)
        return ct

    def Click_menus(self, xpath):
        e = self.driver.find_element_by_xpath(xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(e).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(2)
        e = self.driver.find_element_by_xpath(xpath)
        e = self.driver.find_element_by_xpath(xpath).click()
        #self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//Click" + str(r) + ".png")
        return e

    def combo_texto_xpath(self, xpath, texto):
        ct = self.driver.find_element_by_xpath(xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(ct).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(2)
        ct = Select(self.driver.find_element_by_xpath(xpath))
        ct.select_by_visible_text(texto)
        return ct

    def combo_texto(self, id, texto):
        ct = self.driver.find_element_by_id(id)
        actions = ActionChains(self.driver)
        actions.move_to_element(ct).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(2)
        ct = Select(self.driver.find_element_by_id(id))
        ct.select_by_visible_text(texto)
        return ct

    def combo_index(self, id, index):
        t = self.driver.find_element_by_id(id)
        actions = ActionChains(self.driver)
        actions.move_to_element(t).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(3)
        ct = Select(self.driver.find_element_by_id(id))
        ct.select_by_index(index)
        time.sleep(3)
        #self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//Check" + str(r) + ".png")
        return ct

    def combo_index_xpath(self, xpath, index):
        t = self.driver.find_element_by_xpath(xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(t).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(1)
        ct = Select(self.driver.find_element_by_xpath(xpath))
        ct.select_by_index(index)
        time.sleep(2)
        # self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//Check" + str(r) + ".png")
        return ct

    def check(self, xpath):
        #r = random.randint(1, 1000)
        ck = self.driver.find_element_by_xpath(xpath).click()
        #self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//Check" + str(r) + ".png")
        return ck

    def tiempo(self, tiempo):
        t = time.sleep(tiempo)
        return t

    def upload_xpath(self, xpath, ruta):
        t = self.driver.find_element_by_xpath(xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(t).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(1)
        up = self.driver.find_element_by_xpath(xpath).send_keys(ruta)

        return up

    def upload(self, id, ruta):
        t = self.driver.find_element_by_id(id)
        actions = ActionChains(self.driver)
        actions.move_to_element(t).perform()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(25) + ")")
        time.sleep(1)
        up = self.driver.find_element_by_id(id).send_keys(ruta)
        return up

    def Validar_Elemento(self, id):
        wait = WebDriverWait(self.driver, 10)
        v = wait.until(EC.visibility_of_element_located((By.ID, id)))
        return v

    def Validar_avilitado_xpat(self, xpath):
        e = self.driver.find_element_by_xpath(xpath)
        re = str(e.is_enabled())
        return re

    def scrolling(self, y):
        s = self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(y) + ")")
        return s

    def obtener_valor(self, xpath):
        val = self.driver.find_element_by_xpath(xpath).value
        return val

    def tab_enter(self,xpath):
        self.driver.find_element_by_xpath(xpath).send_keys(Keys.TAB+Keys.ENTER)

    def tab(self, xpath):
        self.driver.find_element_by_xpath(xpath).send_keys(Keys.TAB)

    def existe(self,xpath):
        isEnabled= self.driver.find_element_by_xpath(xpath)
        if(isEnabled):
            val="Ok"
        else:
            val="Falso"
        return val

    def existe2(self,xpath):
        isDisplayed= self.driver.find_element_by_xpath(xpath)
        if(isDisplayed):
            val="Ok"
        else:
            val="Falso"
        return val

    def existe_try_xpath(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
            v="Existe"
        except NoSuchElementException:
            v="Falso"
        return v

    def existe_try(self, id):
        try:
            self.driver.find_element_by_id(id)
            v = "Existe"
        except NoSuchElementException:
            v = "Falso"
        return v

    def existe_try_css(self, css):
        try:
            self.driver.find_element_by_css_selector(css)
            v = "Existe"
        except NoSuchElementException:
            v = "Falso"
        return v


    def elemento_enter(self,xpath):
        val=self.driver.find_element_by_xpath(xpath)
        val.send_keys(Keys.ENTER)
        return val



    def combo_index_existe(self,xpath):
        val = Select(self.driver.find_element_by_xpath(xpath))
        valo=len(val.options)
        return valo

    def combo_index_existe2(self,xpath):
        val = self.driver.find_elements_by_xpath(xpath)
        #valo=val.text
        return val




    def campo_enabled(self,xpath):
        f=self.driver.find_element_by_xpath(xpath).is_enabled()
        if(f):
            val="Activo"
        else:
            val="Inactivo"
        return val

    def limpiar(self,xpath):
        c=self.driver.find_element_by_xpath(xpath).clear()
        return c

    def tamano(self,css):
        v=self.driver.find_element_by_css_selector(css)
        return v

    def obtenerTexto(self,xpath):
        val=self.driver.find_element_by_xpath(xpath).text
        return val

    def combo_index_Ok(self,xpath):
        ct = self.driver.find_elements_by_xpath(xpath)
        ct=len(ct)
        return ct

    def localizar_elemento_id_limpiar(self, id):
        val = self.driver.find_element_by_id(id)
        actions = ActionChains(self.driver)
        actions.move_to_element(val).perform()
        val = self.driver.find_element_by_xpath(id).clear()
        return val

    def localizar_elemento_id(self, id):
        val = self.driver.find_element_by_id(id)
        actions = ActionChains(self.driver)
        actions.move_to_element(val).perform()
        time.sleep(1.5)
        return val

    def localizar_elemento_xpath(self, xpath):
        val = self.driver.find_element_by_xpath(xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(val).perform()
        time.sleep(1)
        print("Localizado")
        return val

    def localizar_elemento_xpath_limpiar(self, xpath):
        val = self.driver.find_element_by_xpath(xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(val).perform()
        val = self.driver.find_element_by_xpath(xpath).clear()
        return val

    def localizar_elemento_css_limpiar(self, css):
        val = self.driver.find_element_by_class_name(css)
        actions = ActionChains(self.driver)
        actions.move_to_element(val).perform()
        val = self.driver.find_element_by_xpath(css).clear()
        return val

    def localizar_elemento_css(self, css):
        val = self.driver.find_element_by_class_name(css)
        actions = ActionChains(self.driver)
        actions.move_to_element(val).perform()
        time.sleep(1)
        return val



