# pyrefly: ignore [missing-import]
from selenium import webdriver
# pyrefly: ignore [missing-import]
from selenium.webdriver.firefox.options import Options
# pyrefly: ignore [missing-import]
from selenium.webdriver.common.by import By
# pyrefly: ignore [missing-import]
from selenium.webdriver.support.ui import WebDriverWait
# pyrefly: ignore [missing-import]
from selenium.webdriver.support import expected_conditions as EC

import time 


def run_user():
    options = Options()
    options.add_argument("-headless")

    driver = webdriver.Firefox(options=options)
    start_time = time.time()
    success = False # assumption
    wait = WebDriverWait(driver, 10)

    try:
        # Open Website
        driver.get("https://www.saucedemo.com")

        # Login
        username = wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )

        password = driver.find_element(
            By.ID,
            "password"
        )

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")

        login_button = driver.find_element(
            By.ID,
            "login-button"
        )

        login_button.click()

        # Verify Login
        wait.until(
            EC.presence_of_element_located(
                (By.ID, "inventory_container")
            )
        )

        print("LOGIN SUCCESSFUL")

        # Open First Product
        first_product = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        first_product.click()

        print("PRODUCT OPENED")

        # Add To Cart
        add_to_cart = wait.until(
            EC.presence_of_element_located(
                (By.ID, "add-to-cart")
            )
        )

        add_to_cart.click()

        print("ITEM ADDED TO CART")

        # Verify Cart Count
        cart_badge = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )

        # print(f"ITEMS IN CART: {cart_badge.text}")

        # Open Cart
        cart_icon = driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_link"
        )

        cart_icon.click()

        print("CART OPENED")

        # # Remove Item
        # remove_button = wait.until(
        #     EC.presence_of_element_located(
        #         (By.ID, "remove")
        #     )
        # )

        # remove_button.click()

        # print("ITEM REMOVED")

        print("USER JOURNEY COMPLETED")
        success = True
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        execution_time = time.time() - start_time
        driver.quit()
        return {
            "success":success, 
            "execution_time":execution_time
        }


    


    