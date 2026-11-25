"""HW 24.11 - demowebshop.tricentis.com

Find 10 tags using two strategies: By.TAG_NAME and By.CSS_SELECTOR.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://demowebshop.tricentis.com/"

driver = webdriver.Chrome()

try:
    # open site
    driver.get(URL)
    driver.maximize_window()

    # 1. div
    div = driver.find_element(By.TAG_NAME, "div")
    div_1 = driver.find_element(By.CSS_SELECTOR, "div")

    # 2. a (links)
    a_list = driver.find_elements(By.TAG_NAME, "a")
    a_list_1 = driver.find_elements(By.CSS_SELECTOR, "a")
    print("a:", len(a_list), len(a_list_1))

    # 3. ul
    ul = driver.find_element(By.TAG_NAME, "ul")
    ul_1 = driver.find_element(By.CSS_SELECTOR, "ul")

    # 4. li
    li_list = driver.find_elements(By.TAG_NAME, "li")
    li_list_1 = driver.find_elements(By.CSS_SELECTOR, "li")
    print("li:", len(li_list), len(li_list_1))

    # 5. span
    span = driver.find_element(By.TAG_NAME, "span")
    span_1 = driver.find_element(By.CSS_SELECTOR, "span")

    # 6. input
    input_box = driver.find_element(By.TAG_NAME, "input")
    input_1 = driver.find_element(By.CSS_SELECTOR, "input")

    # 7. img
    img_list = driver.find_elements(By.TAG_NAME, "img")
    img_list_1 = driver.find_elements(By.CSS_SELECTOR, "img")
    print("img:", len(img_list), len(img_list_1))

    # 8. strong
    strong = driver.find_element(By.TAG_NAME, "strong")
    strong_1 = driver.find_element(By.CSS_SELECTOR, "strong")
    print("strong:", strong.text)

    # 9. h2
    h2_list = driver.find_elements(By.TAG_NAME, "h2")
    h2_list_1 = driver.find_elements(By.CSS_SELECTOR, "h2")
    print("h2:", len(h2_list), len(h2_list_1))

    # 10. form
    form = driver.find_element(By.TAG_NAME, "form")
    form_1 = driver.find_element(By.CSS_SELECTOR, "form")

    # extra: label, h3, p
    label = driver.find_element(By.TAG_NAME, "label")
    label_1 = driver.find_element(By.CSS_SELECTOR, "label")

    h3_list = driver.find_elements(By.TAG_NAME, "h3")
    h3_list_1 = driver.find_elements(By.CSS_SELECTOR, "h3")
    print("h3:", len(h3_list), len(h3_list_1))

    p = driver.find_element(By.TAG_NAME, "p")
    p_1 = driver.find_element(By.CSS_SELECTOR, "p")

    # both strategies must point to the same elements
    assert div == div_1
    assert len(a_list) == len(a_list_1)
    assert ul == ul_1
    assert len(li_list) == len(li_list_1)
    assert span == span_1
    assert input_box == input_1
    assert len(img_list) == len(img_list_1)
    assert strong == strong_1
    assert len(h2_list) == len(h2_list_1)
    assert form == form_1
    assert label == label_1
    assert len(h3_list) == len(h3_list_1)
    assert p == p_1
    print("All locators found: TAG_NAME == CSS_SELECTOR")

finally:
    driver.quit()
