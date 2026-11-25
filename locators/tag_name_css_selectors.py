"""HW 24.11 - demowebshop.tricentis.com

Find 10 tags using two strategies: By.TAG_NAME and By.CSS_SELECTOR.

Скрипт открывает главную страницу Demo Web Shop и ищет 10 HTML-тегов
двумя способами: по имени тега (By.TAG_NAME) и CSS-селектором (By.CSS_SELECTOR).
В конце проверяет, что оба способа нашли одни и те же элементы.

Запуск:  python locators/tag_name_css_selectors.py
"""
# webdriver - модуль для управления браузером (запуск Chrome, открытие страниц и т.д.)
from selenium import webdriver
# By - набор стратегий поиска: By.ID, By.CLASS_NAME, By.TAG_NAME, By.CSS_SELECTOR, By.XPATH...
from selenium.webdriver.common.by import By

# Адрес тестируемого сайта вынесен в константу, чтобы менять его в одном месте
URL = "https://demowebshop.tricentis.com/"

# Запускаем новое окно Chrome.
# С Selenium 4.6+ chromedriver скачивается автоматически (Selenium Manager)
driver = webdriver.Chrome()

# try/finally: блок finally выполнится ВСЕГДА, даже если внутри try
# возникнет ошибка (например, NoSuchElementException), и браузер закроется
try:
    # open site
    # get() открывает страницу и ждёт её полной загрузки
    driver.get(URL)
    # Разворачиваем окно на весь экран, чтобы вёрстка была десктопной
    driver.maximize_window()

    # find_element(...)  -> возвращает ПЕРВЫЙ найденный элемент
    #                       (если не найден - исключение NoSuchElementException)
    # find_elements(...) -> возвращает СПИСОК всех найденных элементов
    #                       (если не найдено - пустой список [])
    #
    # By.TAG_NAME, "div"     - поиск по имени тега
    # By.CSS_SELECTOR, "div" - CSS-селектор по типу (тегу), находит те же элементы

    # 1. div - блочный контейнер; первый div - обёртка всей страницы
    div = driver.find_element(By.TAG_NAME, "div")
    div_1 = driver.find_element(By.CSS_SELECTOR, "div")

    # 2. a (links) - ссылки: меню, категории, товары, футер.
    # Их много, поэтому берём список и выводим количество через len()
    a_list = driver.find_elements(By.TAG_NAME, "a")
    a_list_1 = driver.find_elements(By.CSS_SELECTOR, "a")
    print("a:", len(a_list), len(a_list_1))

    # 3. ul - неупорядоченный список; первый - ссылки в шапке (Register, Log in, Cart)
    ul = driver.find_element(By.TAG_NAME, "ul")
    ul_1 = driver.find_element(By.CSS_SELECTOR, "ul")

    # 4. li - пункты списков (меню, категории, футер)
    li_list = driver.find_elements(By.TAG_NAME, "li")
    li_list_1 = driver.find_elements(By.CSS_SELECTOR, "li")
    print("li:", len(li_list), len(li_list_1))

    # 5. span - строчный контейнер для текста (например, счётчик корзины)
    span = driver.find_element(By.TAG_NAME, "span")
    span_1 = driver.find_element(By.CSS_SELECTOR, "span")

    # 6. input - поле ввода; первое на странице - строка поиска в шапке
    input_box = driver.find_element(By.TAG_NAME, "input")
    input_1 = driver.find_element(By.CSS_SELECTOR, "input")

    # 7. img - картинки: логотип, баннер, фото товаров
    img_list = driver.find_elements(By.TAG_NAME, "img")
    img_list_1 = driver.find_elements(By.CSS_SELECTOR, "img")
    print("img:", len(img_list), len(img_list_1))

    # 8. strong - жирный текст; первый - заголовок боковой колонки "CATEGORIES".
    # .text возвращает видимый текст элемента
    strong = driver.find_element(By.TAG_NAME, "strong")
    strong_1 = driver.find_element(By.CSS_SELECTOR, "strong")
    print("strong:", strong.text)

    # 9. h2 - заголовки второго уровня (названия товаров на главной)
    h2_list = driver.find_elements(By.TAG_NAME, "h2")
    h2_list_1 = driver.find_elements(By.CSS_SELECTOR, "h2")
    print("h2:", len(h2_list), len(h2_list_1))

    # 10. form - форма; первая - форма поиска в шапке
    form = driver.find_element(By.TAG_NAME, "form")
    form_1 = driver.find_element(By.CSS_SELECTOR, "form")

    # extra: label, h3, p
    # label - подпись к полю формы
    label = driver.find_element(By.TAG_NAME, "label")
    label_1 = driver.find_element(By.CSS_SELECTOR, "label")

    # h3 - заголовки третьего уровня (блоки в футере)
    h3_list = driver.find_elements(By.TAG_NAME, "h3")
    h3_list_1 = driver.find_elements(By.CSS_SELECTOR, "h3")
    print("h3:", len(h3_list), len(h3_list_1))

    # p - абзац текста
    p = driver.find_element(By.TAG_NAME, "p")
    p_1 = driver.find_element(By.CSS_SELECTOR, "p")

    # both strategies must point to the same elements
    # Проверки: оба способа должны находить одни и те же элементы.
    # WebElement сравниваются через == по внутреннему id элемента в браузере,
    # для списков сравниваем количество найденных элементов.
    # Если проверка не пройдёт - будет AssertionError, а finally закроет браузер.
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
    # Сюда доходим, только если все проверки прошли
    print("All locators found: TAG_NAME == CSS_SELECTOR")

finally:
    # quit() закрывает все окна и завершает сессию драйвера
    # (close() закрыл бы только текущую вкладку)
    driver.quit()
