from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")
   

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")


#class MainPageLocators():
    #LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_PRODUCT_BUTTON=(By.CSS_SELECTOR,".btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR,".product_main h1")
    PRODUCT_PRICE=(By.CSS_SELECTOR,".product_main .price_color")
    ADD_PRODUCT_MESSAGE=(By.CSS_SELECTOR,"#messages .alert:nth-child(1) .alertinner strong")
    BASKET_COST_MESSAGE=(By.CSS_SELECTOR,"#messages .alert:nth-child(3) .alertinner strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,"#messages .alert:nth-child(1)")