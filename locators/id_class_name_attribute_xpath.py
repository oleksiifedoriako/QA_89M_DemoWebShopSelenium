"""HW 25.11.2026 - demowebshop.tricentis.com

Find 10 elements by each strategy: By.CLASS_NAME, By.ID, attribute (CSS [attr]),
By.NAME and By.XPATH.

Скрипт открывает главную страницу Demo Web Shop и ищет по 10 элементов
пятью способами:
  1) By.ID           - по уникальному атрибуту id;
  2) By.CLASS_NAME   - по ОДНОМУ классу из атрибута class;
  3) атрибут         - CSS-селектор вида [атрибут='значение'];
  4) By.NAME         - по атрибуту name (часть на главной, часть на странице Log in);
  5) By.XPATH        - XPath-выражения разных видов (@атрибут, text(), contains(),
                       starts-with(), индекс, оси parent/ancestor).
В конце сравнивает часть результатов между стратегиями: разные локаторы
одного и того же элемента должны возвращать один и тот же WebElement.

Запуск:  python locators/id_class_name_attribute_xpath.py
"""
# webdriver - модуль для управления браузером (запуск Chrome, открытие страниц и т.д.)
from selenium import webdriver
# By - набор стратегий поиска: By.ID, By.CLASS_NAME, By.NAME, By.CSS_SELECTOR, By.XPATH...
from selenium.webdriver.common.by import By
# WebDriverWait + expected_conditions (EC) - явные ожидания:
# ждём, пока условие станет истинным (по умолчанию проверка каждые 0.5 с)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Адреса вынесены в константы, чтобы менять их в одном месте
URL = "https://demowebshop.tricentis.com/"
LOGIN_URL = URL + "login"

# Запускаем новое окно Chrome.
# С Selenium 4.6+ chromedriver скачивается автоматически (Selenium Manager)
driver = webdriver.Chrome()
# Явное ожидание: максимум 10 секунд на каждое условие
wait = WebDriverWait(driver, 10)

# try/finally: блок finally выполнится ВСЕГДА, даже если внутри try
# возникнет ошибка (NoSuchElementException, TimeoutException, AssertionError),
# и браузер закроется
try:
    # open site
    driver.get(URL)
    driver.maximize_window()
    # Ждём, пока появится строка поиска в шапке - значит, страница отрисовалась.
    # presence_of_element_located - элемент есть в DOM (видимость не важна)
    wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))

    # ------------------------------------------------------------------
    # 1. By.ID - 10 элементов
    # ------------------------------------------------------------------
    # id по стандарту HTML должен быть уникальным на странице, поэтому это
    # самый быстрый и надёжный локатор. Если id есть - используем его.
    # find_element() вернёт первый элемент или бросит NoSuchElementException.
    print("--- By.ID ---")
    # 1) строка поиска в шапке
    search_input = driver.find_element(By.ID, "small-searchterms")
    # 2) пункт "Shopping cart" в шапке (тег li)
    top_cart_link = driver.find_element(By.ID, "topcartlink")
    # 3) выпадающая мини-корзина (появляется при наведении на корзину)
    flyout_cart = driver.find_element(By.ID, "flyout-cart")
    # 4) поле email в блоке подписки на новости
    newsletter_email = driver.find_element(By.ID, "newsletter-email")
    # 5) кнопка "Subscribe"
    subscribe_button = driver.find_element(By.ID, "newsletter-subscribe-button")
    # 6) блок опроса "Community poll"
    poll_block = driver.find_element(By.ID, "poll-block-1")
    # 7) первый вариант ответа опроса (radio "Excellent")
    poll_answer_1 = driver.find_element(By.ID, "pollanswers-1")
    # 8) кнопка "Vote"
    vote_button = driver.find_element(By.ID, "vote-poll-1")
    # 9) слайдер-баннер на главной
    slider = driver.find_element(By.ID, "nivo-slider")
    # 10) кнопка мобильного меню (видна только на узком экране, но в DOM есть)
    mob_menu_button = driver.find_element(By.ID, "mob-menu-button")
    # get_attribute("value") - значение атрибута value (для кнопок это надпись)
    print("search placeholder:", search_input.get_attribute("value"))
    print("subscribe button:", subscribe_button.get_attribute("value"))
    print("vote button:", vote_button.get_attribute("value"))
    # tag_name - имя тега найденного элемента
    print("topcartlink tag:", top_cart_link.tag_name)

    # ------------------------------------------------------------------
    # 2. By.CLASS_NAME - 10 элементов
    # ------------------------------------------------------------------
    # By.CLASS_NAME принимает ТОЛЬКО ОДИН класс без точки и пробелов.
    # Для class="button-1 search-box-button" можно искать "search-box-button",
    # а строка "button-1 search-box-button" даст ошибку (InvalidSelector):
    # для нескольких классов нужен CSS ".button-1.search-box-button".
    print("--- By.CLASS_NAME ---")
    # 1) блок с логотипом
    header_logo = driver.find_element(By.CLASS_NAME, "header-logo")
    # 2) список ссылок в шапке (Register, Log in, Cart, Wishlist)
    header_links = driver.find_element(By.CLASS_NAME, "header-links")
    # 3) ссылка "Register"
    register_link = driver.find_element(By.CLASS_NAME, "ico-register")
    # 4) ссылка "Log in"
    login_link = driver.find_element(By.CLASS_NAME, "ico-login")
    # 5) поле поиска (то же, что small-searchterms, но найдено по классу)
    search_box_text = driver.find_element(By.CLASS_NAME, "search-box-text")
    # 6) кнопка "Search" (у неё два класса, берём один - search-box-button)
    search_box_button = driver.find_element(By.CLASS_NAME, "search-box-button")
    # 7) верхнее меню категорий
    top_menu = driver.find_element(By.CLASS_NAME, "top-menu")
    # 8) блок "Categories" в левой колонке
    category_block = driver.find_element(By.CLASS_NAME, "block-category-navigation")
    # 9) карточки товаров на главной - их несколько, берём список
    product_items = driver.find_elements(By.CLASS_NAME, "product-item")
    # 10) подвал сайта
    footer = driver.find_element(By.CLASS_NAME, "footer")
    # .text - видимый текст элемента
    print("register:", register_link.text, "| login:", login_link.text)
    print("product-item count:", len(product_items))

    # ------------------------------------------------------------------
    # 3. Attribute - 10 элементов через CSS-селектор по атрибуту
    # ------------------------------------------------------------------
    # Отдельной стратегии By.ATTRIBUTE в Selenium нет, поиск по любому
    # атрибуту делается CSS-селектором (или XPath с @атрибут):
    #   [attr='v']   - значение равно v
    #   [attr^='v']  - начинается с v
    #   [attr$='v']  - заканчивается на v
    #   [attr*='v']  - содержит v
    #   [attr]       - атрибут просто есть
    print("--- Attribute (CSS [attr]) ---")
    # 1) ссылка Register по точному href
    attr_register = driver.find_element(By.CSS_SELECTOR, "a[href='/register']")
    # 2) ссылка Wishlist по точному href
    attr_wishlist = driver.find_element(By.CSS_SELECTOR, "a[href='/wishlist']")
    # 3) кнопка поиска по type
    attr_submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    # 4) та же кнопка, но по value - ещё один способ
    attr_search_value = driver.find_element(By.CSS_SELECTOR, "input[value='Search']")
    # 5) логотип по альтернативному тексту картинки
    attr_logo = driver.find_element(By.CSS_SELECTOR, "img[alt='Tricentis Demo Web Shop']")
    # 6) картинка, у которой в src есть слово logo (*= "содержит")
    attr_logo_src = driver.find_element(By.CSS_SELECTOR, "img[src*='logo']")
    # 7) ссылка RSS: href начинается с /news/rss (^= "начинается с")
    attr_rss = driver.find_element(By.CSS_SELECTOR, "a[href^='/news/rss']")
    # 8) все radio-кнопки опроса
    attr_radios = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
    # 9) все кнопки "Add to cart" по value
    attr_add_to_cart = driver.find_elements(By.CSS_SELECTOR, "input[value='Add to cart']")
    # 10) подпись к первому варианту опроса: label с атрибутом for
    attr_label = driver.find_element(By.CSS_SELECTOR, "label[for='pollanswers-1']")
    print("rss link:", attr_rss.get_attribute("href"))
    print("radios:", len(attr_radios), "| add to cart buttons:", len(attr_add_to_cart))
    print("label for pollanswers-1:", attr_label.text)

    # ------------------------------------------------------------------
    # 4. XPath - 10 элементов
    # ------------------------------------------------------------------
    # //  - искать на любом уровне вложенности
    # /   - прямой потомок
    # [@attr='v']             - условие по атрибуту
    # [text()='v']            - точный текст узла (берётся из HTML, а не из экрана!)
    # contains(@attr,'v')     - атрибут содержит подстроку
    # starts-with(@attr,'v')  - атрибут начинается с подстроки
    # (//xpath)[N]            - N-й результат (нумерация с 1!)
    # parent:: / ancestor::   - оси: подняться к родителю / предку
    print("--- By.XPATH ---")
    # 1) поле поиска по id
    xp_search = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
    # 2) ссылка "Log in" по точному тексту
    xp_login = driver.find_element(By.XPATH, "//a[text()='Log in']")
    # 3) категория Books: href содержит /books.
    #    Внимание: @class='...' сравнивает ВСЮ строку class целиком,
    #    поэтому пишем оба класса: "block block-category-navigation"
    xp_books = driver.find_element(By.XPATH, "//div[@class='block block-category-navigation']//a[contains(@href,'/books')]")
    # 4) логотип: путь от блока по прямым потомкам
    xp_logo = driver.find_element(By.XPATH, "//div[@class='header-logo']/a/img")
    # 5) кнопка "Subscribe" по value
    xp_subscribe = driver.find_element(By.XPATH, "//input[@value='Subscribe']")
    # 6) названия всех товаров на главной (список)
    xp_titles = driver.find_elements(By.XPATH, "//h2[@class='product-title']/a")
    # 7) заголовок "Categories". В HTML текст "Categories", а на экране
    #    CSS делает его заглавными (CATEGORIES). text() видит именно HTML.
    xp_categories = driver.find_element(By.XPATH, "//strong[text()='Categories']")
    # 8) ссылка Register: href начинается с /register
    xp_register = driver.find_element(By.XPATH, "//a[starts-with(@href,'/register')]")
    # 9) первая карточка товара - индекс в скобках
    xp_first_item = driver.find_element(By.XPATH, "(//div[@class='item-box'])[1]")
    # 10) колонка "Information" в подвале: находим h3 по тексту внутри footer,
    #      а parent::div поднимает нас на уровень вверх - к самой колонке
    xp_info_column = driver.find_element(
        By.XPATH, "//div[@class='footer']//h3[text()='Information']/parent::div")
    print("xpath login:", xp_login.text, "| books:", xp_books.text)
    print("titles:", len(xp_titles), "->", xp_titles[0].text)
    print("categories .text:", xp_categories.text)
    print("first item title:", xp_first_item.find_element(By.CLASS_NAME, "product-title").text)
    print("info column class:", xp_info_column.get_attribute("class"))

    # ------------------------------------------------------------------
    # 5. By.NAME - 10 элементов (5 на главной + 5 на странице Log in)
    # ------------------------------------------------------------------
    # By.NAME ищет по атрибуту name. Он есть у полей форм (input, select,
    # textarea) и у тегов <meta>. На главной уникальных name мало,
    # поэтому вторую половину ищем на странице входа.
    print("--- By.NAME ---")
    # главная страница
    # 1) строка поиска - name="q"
    name_q = driver.find_element(By.NAME, "q")
    # 2) поле подписки
    name_newsletter = driver.find_element(By.NAME, "NewsletterEmail")
    # 3) radio опроса: у всех 4 вариантов name один и тот же ("группа")
    name_poll = driver.find_elements(By.NAME, "pollanswers-1")
    # 4) мета-тег description (в <head>, на экране не виден)
    name_description = driver.find_element(By.NAME, "description")
    # 5) мета-тег keywords
    name_keywords = driver.find_element(By.NAME, "keywords")
    print("poll radios by one name:", len(name_poll))
    print("meta description:", name_description.get_attribute("content"))

    # Проверки для главной страницы - пока мы на ней.
    # Разные стратегии, указывающие на ОДИН элемент, возвращают равные
    # WebElement (сравнение == идёт по внутреннему id элемента в браузере).
    assert search_input == search_box_text == xp_search == name_q
    assert newsletter_email == name_newsletter
    assert subscribe_button == xp_subscribe
    assert register_link == attr_register == xp_register
    assert login_link == xp_login
    assert search_box_button == attr_submit == attr_search_value
    assert attr_logo == attr_logo_src == xp_logo
    assert poll_answer_1 == attr_radios[0] == name_poll[0]
    assert len(attr_radios) == len(name_poll) == 4
    assert len(product_items) == len(attr_add_to_cart) == len(xp_titles)
    # header_logo, header_links и т.д. просто должны найтись (иначе было бы исключение),
    # а здесь проверяем, что они действительно на месте и вложены правильно
    assert header_logo.find_element(By.TAG_NAME, "img") == xp_logo
    assert top_menu.tag_name == "ul" and category_block.is_displayed() and footer.is_displayed()
    assert attr_wishlist.get_attribute("class") == "ico-wishlist"
    assert attr_label.text == "Excellent"
    assert xp_categories.text == "CATEGORIES"  # .text отдаёт текст так, как он виден
    assert flyout_cart and poll_block and slider and mob_menu_button and top_cart_link
    assert name_keywords.tag_name == "meta"

    # страница Log in
    driver.get(LOGIN_URL)
    # Ждём поле Email - признак, что форма входа загрузилась
    wait.until(EC.visibility_of_element_located((By.NAME, "Email")))
    # 6) поле Email
    name_email = driver.find_element(By.NAME, "Email")
    # 7) поле Password
    name_password = driver.find_element(By.NAME, "Password")
    # 8) чекбокс "Remember me?". Внимание: name="RememberMe" есть ещё у
    #    скрытого input type=hidden, find_element вернёт ПЕРВЫЙ - чекбокс
    name_remember = driver.find_element(By.NAME, "RememberMe")
    # 9) мета-тег generator
    name_generator = driver.find_element(By.NAME, "generator")
    # 10) мета-тег viewport
    name_viewport = driver.find_element(By.NAME, "viewport")
    print("Email type:", name_email.get_attribute("type"))
    print("Password type:", name_password.get_attribute("type"))
    print("RememberMe type:", name_remember.get_attribute("type"))
    print("generator:", name_generator.get_attribute("content"))
    print("viewport:", name_viewport.get_attribute("content"))

    # Проверки для страницы Log in: By.NAME == By.ID == XPath
    assert name_email == driver.find_element(By.ID, "Email")
    assert name_password == driver.find_element(By.XPATH, "//input[@type='password']")
    assert name_remember.get_attribute("type") == "checkbox"
    assert len(driver.find_elements(By.NAME, "RememberMe")) == 2

    # Сюда доходим, только если все проверки прошли
    print("All locators found: ID, CLASS_NAME, attribute, NAME, XPATH")

finally:
    # quit() закрывает все окна и завершает сессию драйвера
    driver.quit()
