# Разбор кода: `locators/tag_name_css_selectors.py`

ДЗ 24.11: создать проект для <https://demowebshop.tricentis.com/> и найти 10 тегов стратегиями **TAG_NAME** и **CSS-селекторами**.

## Структура проекта

```
QA_89M_DemoWebShopSelenium/
├── locators/
│   ├── __init__.py                 # делает папку Python-пакетом (пустой)
│   └── tag_name_css_selectors.py   # основной скрипт ДЗ
├── requirements.txt                # зависимости: selenium
├── README.md                       # краткое описание и запуск
├── CODE_EXPLANATION.md             # этот файл
└── .gitignore                      # стандартный Python .gitignore
```

## 1. Импорты

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
```

- `webdriver` — модуль для управления браузером. Через него создаём экземпляр Chrome.
- `By` — класс с константами стратегий поиска: `By.ID`, `By.CLASS_NAME`, `By.TAG_NAME`, `By.CSS_SELECTOR`, `By.XPATH` и т.д. В этом ДЗ используем две: `By.TAG_NAME` и `By.CSS_SELECTOR`.

## 2. Запуск браузера

```python
URL = "https://demowebshop.tricentis.com/"
driver = webdriver.Chrome()
```

- `URL` вынесен в константу: адрес меняется в одном месте.
- `webdriver.Chrome()` открывает новое окно Chrome. Начиная с Selenium 4.6, драйвер (chromedriver) скачивается автоматически через **Selenium Manager**, ставить его вручную не нужно.

## 3. Блок `try / finally`

```python
try:
    ...
finally:
    driver.quit()
```

`finally` выполняется **всегда**, даже если элемент не найден и вылетело исключение (`NoSuchElementException`). Браузер гарантированно закрывается, «висящих» процессов Chrome не остаётся.

> `driver.quit()` закрывает все окна и завершает сессию драйвера, а `driver.close()` закрывает только текущую вкладку. В конце теста нужен `quit()`.

## 4. Открытие сайта

```python
driver.get(URL)
driver.maximize_window()
```

- `get()` открывает страницу и ждёт окончания её загрузки (событие `load`).
- `maximize_window()` разворачивает окно, чтобы вёрстка была «десктопной» и элементы не прятались за адаптивным меню.

## 5. `find_element` и `find_elements`

| Метод | Что возвращает | Если ничего не найдено |
|---|---|---|
| `find_element(by, value)` | **первый** подходящий `WebElement` | бросает `NoSuchElementException` |
| `find_elements(by, value)` | **список** всех подходящих элементов | возвращает пустой список `[]` |

Для тегов, которых на странице много (`a`, `li`, `img`, `h2`, `h3`), используется `find_elements` и печатается `len(...)`, то есть их количество. Для остальных берётся первый элемент.

## 6. Стратегия TAG_NAME и CSS-селектор по тегу

```python
div   = driver.find_element(By.TAG_NAME, "div")
div_1 = driver.find_element(By.CSS_SELECTOR, "div")
```

- `By.TAG_NAME, "div"` ищет элементы по имени HTML-тега.
- `By.CSS_SELECTOR, "div"` делает то же самое: в CSS простое имя тега (type selector) выбирает все элементы с этим тегом.

Поэтому оба вызова возвращают **один и тот же** элемент. CSS мощнее, его можно уточнять:

| CSS | Что найдёт |
|---|---|
| `div` | все `<div>` |
| `.header` | элементы с `class="header"` |
| `#small-searchterms` | элемент с `id="small-searchterms"` |
| `input[type='submit']` | `<input>` с атрибутом `type="submit"` |
| `ul.top-menu > li` | `<li>`, прямые потомки `<ul class="top-menu">` |

## 7. Десять найденных тегов

| # | Тег | Метод | Что это на demowebshop |
|---|---|---|---|
| 1 | `div` | `find_element` | первый контейнер страницы (`div.master-wrapper-page`) |
| 2 | `a` | `find_elements` | все ссылки: меню, категории, товары, футер (**95**) |
| 3 | `ul` | `find_element` | первый список: ссылки в шапке (Register / Log in / Cart) |
| 4 | `li` | `find_elements` | пункты всех списков (**77**) |
| 5 | `span` | `find_element` | первый `span`: текст/счётчик в шапке |
| 6 | `input` | `find_element` | первое поле ввода: поиск в шапке |
| 7 | `img` | `find_elements` | все картинки: логотип, товары, баннер (**10**) |
| 8 | `strong` | `find_element` | заголовок боковой колонки, текст `CATEGORIES` |
| 9 | `h2` | `find_elements` | заголовки, например названия товаров (**7**) |
| 10 | `form` | `find_element` | форма поиска в шапке |

Дополнительно: `label`, `h3` (**4**) и `p`.

Числа в скобках получены при запуске 25.11.2026. Если сайт обновится, они могут измениться.

### Вывод в консоль

```python
print("a:", len(a_list), len(a_list_1))   # a: 95 95
print("strong:", strong.text)              # strong: CATEGORIES
```

- `len(list)` — количество найденных элементов.
- `.text` — видимый текст элемента.

## 8. Проверки (assert)

```python
assert div == div_1
assert len(a_list) == len(a_list_1)
...
print("All locators found: TAG_NAME == CSS_SELECTOR")
```

- `WebElement` сравниваются через `==` по внутреннему ID элемента в браузере. `div == div_1` равно `True`, значит обе стратегии нашли **один и тот же DOM-узел**.
- Для списков сравниваются длины.
- Если хоть одна проверка не пройдёт, вылетит `AssertionError`, `finally` закроет браузер, а итоговое сообщение не напечатается.

## 9. Запуск

```powershell
pip install -r requirements.txt
python locators/tag_name_css_selectors.py
```

Ожидаемый вывод:

```
a: 95 95
li: 77 77
img: 10 10
strong: CATEGORIES
h2: 7 7
h3: 4 4
All locators found: TAG_NAME == CSS_SELECTOR
```

## 10. Итог: TAG_NAME и CSS_SELECTOR

| | `By.TAG_NAME` | `By.CSS_SELECTOR` |
|---|---|---|
| Синтаксис | только имя тега | тег, класс, id, атрибуты, иерархия |
| Точность | низкая: тегов обычно много | высокая, если уточнить селектор |
| Когда применять | посчитать элементы (`a`, `img`) или найти уникальный тег (`form`, `title`) | почти всегда, основная стратегия |
