from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")


    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_serch(browser):
    browser.get("https://demo.opencart.com")

    WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    #не задавйте вопросов, только так это работает
    i=0
    while i<1000000000:
        i+=1
    search_box=WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )
    search_box.send_keys("MacBook")

    search_button = browser.find_element(By.CLASS_NAME, "btn.btn-light.btn-lg")
    search_button.click()

    # Ждем появления результатов поиска
    product_name = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h4 a"))
    )
    assert "MacBook" in product_name.text

def test_add_to_cart(browser):
    browser.get("https://demo.opencart.com")

    #не задавйте вопросов, только так это работает
    i=0
    while i<1000000000:
        i+=1
    search_box=WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )
    search_box.send_keys("iPhone")

    search_button = browser.find_element(By.CLASS_NAME, "btn.btn-light.btn-lg")
    search_button.click()
    

    add_to_cart_button = browser.find_element(By.XPATH, "//*[@id='product-list']/div/div/div[2]/form/div/button[1]")
    actions = ActionChains(browser)
    actions.move_to_element(add_to_cart_button).perform()
    add_to_cart_button.click()


#<div class="alert alert-success alert-dismissible" style="opacity: 0.126333;"><i class="fa-solid fa-circle-check"></i> Success: You have added <a href="https://demo.opencart.com/en-gb/product/iphone">iPhone</a> to your <a href="https://demo.opencart.com/en-gb?route=checkout/cart">shopping cart</a>! <button type="button" class="btn-close" data-bs-dismiss="alert"></button></div>
    

#<button type="button" data-bs-toggle="dropdown" class="btn btn-lg btn-inverse btn-block dropdown-toggle show" aria-expanded="true"><i class="fa-solid fa-cart-shopping"></i> 1 item(s) - $123.20</button>  
    cart_button =WebDriverWait(browser, 100000000).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle"), "1 item(s) - $123.20"))
    #browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    assert cart_button



def test_delete_from_cart(browser):
    browser.get("https://demo.opencart.com")

    #не задавйте вопросов, только так это работает
    i=0
    while i<1000000000:
        i+=1
    search_box=WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )
    search_box.send_keys("iPhone")

    search_button = browser.find_element(By.CLASS_NAME, "btn.btn-light.btn-lg")
    search_button.click()
    

    add_to_cart_button = browser.find_element(By.XPATH, "//*[@id='product-list']/div/div/div[2]/form/div/button[1]")
    actions = ActionChains(browser)
    actions.move_to_element(add_to_cart_button).perform()
    add_to_cart_button.click()


#<div class="alert alert-success alert-dismissible" style="opacity: 0.126333;"><i class="fa-solid fa-circle-check"></i> Success: You have added <a href="https://demo.opencart.com/en-gb/product/iphone">iPhone</a> to your <a href="https://demo.opencart.com/en-gb?route=checkout/cart">shopping cart</a>! <button type="button" class="btn-close" data-bs-dismiss="alert"></button></div>
    

    #<div class="alert alert-success alert-dismissible" style="opacity: 0.568377;"><i class="fa-solid fa-circle-check"></i> Success: You have added <a href="https://demo.opencart.com/en-gb/product/iphone">iPhone</a> to your <a href="https://demo.opencart.com/en-gb?route=checkout/cart">shopping cart</a>! <button type="button" class="btn-close" data-bs-dismiss="alert"></button></div>
    alert_msg =WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"))
    )
    i=0
    while i < 400000000:
        i+=1
    #browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    cart_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle"))
    )
    actions.move_to_element(cart_button).perform()
    cart_button.click()
    #menu=WebDriverWait(browser, 10).until(
    #    EC.visibility_of_element_located((By.CLASS_NAME, "dropdown-menu dropdown-menu-end p-2 show"))
    #)
    #dropdown-menu dropdown-menu-end p-2 show
    #<button type="submit" data-bs-toggle="tooltip" class="btn btn-danger" aria-label="Remove" data-bs-original-title="Remove"><i class="fa-solid fa-circle-xmark"></i></button>
    remove=WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-danger"))
    )
    remove=browser.find_element(By.CSS_SELECTOR, "button.btn.btn-danger")
    remove.click()
    cart_button =WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle"), "0 item(s) - $0.00"))
    cart_button_text = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle").text

    assert cart_button_text == "0 item(s) - $0.00", f"Текст кнопки корзины: {cart_button_text}"
    #assert cart_button

fname="ilia4"
lname="kashkarov4"
emailf="kashkarov4@gmail.com"
passwordf="123456789"

def test_registr(browser):
    browser.get("https://demo.opencart.com")

    #не задавйте вопросов, только так это работает
    i=0
    while i<1000000000:
        i+=1
    
    button_my_acount=browser.find_element(By.LINK_TEXT, "My Account")
    button_my_acount.click()
    
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu.show"))
    )

    # Находим кнопку Register внутри выпадающего меню
    register_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
    )

    # Нажимаем на кнопку Register
    register_button.click()

    # Проверка, что страница регистрации загрузилась
    WebDriverWait(browser, 10).until(
        EC.url_to_be("https://demo.opencart.com/en-gb?route=account/register")
    )
    
    
    first_name=browser.find_element(By.NAME, "firstname")
    first_name.send_keys(fname)
    last_name=browser.find_element(By.NAME, "lastname")
    last_name.send_keys(lname)
    email_field=browser.find_element(By.NAME, "email")
    email_field.send_keys(emailf)
    
    password_field=browser.find_element(By.NAME, "password")
    browser.execute_script("arguments[0].scrollIntoView();", password_field)

    # Ожидание, пока элемент станет кликабельным
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(password_field)
    )
    password_field.send_keys(passwordf)

    checkbox=browser.find_element(By.NAME, "agree")
    browser.execute_script("arguments[0].scrollIntoView();", checkbox)
    # Ожидание, пока элемент станет кликабельным
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(checkbox)
    )
    browser.execute_script("arguments[0].click();", checkbox)
    #checkbox.click()

    continue_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
    #continue_button.click()
    browser.execute_script("arguments[0].click();", continue_button)

    WebDriverWait(browser, 10).until(
        EC.url_changes("https://demo.opencart.com/en-gb?route=account/register")
    )
    text_registr=browser.find_element(By.CSS_SELECTOR, "h1")
    assert text_registr.text=="Your Account Has Been Created!"

def test_login(browser):
    browser.get("https://demo.opencart.com")

    #не задавйте вопросов, только так это работает
    i=0
    while i<1000000000:
        i+=1
    
    button_my_acount=browser.find_element(By.LINK_TEXT, "My Account")
    button_my_acount.click()
    
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu.show"))
    )

    # Находим кнопку Register внутри выпадающего меню
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )

    # Нажимаем на кнопку Register
    login_button.click()

    # Проверка, что страница регистрации загрузилась
    WebDriverWait(browser, 10).until(
        EC.url_to_be("https://demo.opencart.com/en-gb?route=account/login")
    )
    
    
    email_field=browser.find_element(By.NAME, "email")
    email_field.send_keys(emailf)
    
    password_field=browser.find_element(By.NAME, "password")
    password_field.send_keys(passwordf)


    continue_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
    #continue_button.click()
    browser.execute_script("arguments[0].click();", continue_button)

    WebDriverWait(browser, 10).until(
        EC.url_changes("https://demo.opencart.com/en-gb?route=account/login")
    )

    text_myaccount=browser.find_element(By.LINK_TEXT, "Edit your account information")
    assert text_myaccount.text=="Edit your account information"