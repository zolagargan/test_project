from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException 
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.add_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        self.add_button.click()

    
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_BUTTON), "add_to_basket_button is not presented"


    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_MESSAGE), "add_to_basket_message is not presented"

    
    def should_be_basket_cost_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_COST_MESSAGE), "basket_cost_message is not presented"

    
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "product_name is not presented"


    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "product_price is not presented"


    def message_product_name_is_correct(self):
        assert self.is_element_in_message(*ProductPageLocators.PRODUCT_NAME, *ProductPageLocators.ADD_PRODUCT_MESSAGE), "different product name"
    

    def message_basket_cost_is_correct(self):
        assert self.is_element_in_message(*ProductPageLocators.PRODUCT_PRICE, *ProductPageLocators.BASKET_COST_MESSAGE), "basket cost is not equal product price"


    def is_element_in_message(self, element_how, element_what, message_how, message_what):
        element = self.browser.find_element(element_how, element_what).text
        message = self.browser.find_element(message_how, message_what).text
        if element in message:
            return True
        return False


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def shoud_add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_add_to_basket_message()
        self.should_be_basket_cost_message()
        self.should_be_product_name()
        self.should_be_product_price()
        self.message_product_name_is_correct()
        self.message_basket_cost_is_correct()