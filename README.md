# QA_89M_DemoWebShopSelenium

Selenium project for <https://demowebshop.tricentis.com/>.

## Homework

- HW 24.11.2026: find 10 tags with `By.TAG_NAME` and `By.CSS_SELECTOR`:
  `div`, `a`, `ul`, `li`, `span`, `input`, `img`, `strong`, `h2`, `form` (+ extra `label`, `h3`, `p`).
  Code: [`locators/tag_name_css_selectors.py`](locators/tag_name_css_selectors.py),
  report: [`homework/HW_24.11.2026.md`](homework/HW_24.11.2026.md)
- HW 25.11.2026: find 10 elements each with `By.ID`, `By.CLASS_NAME`, attribute (CSS `[attr]`),
  `By.NAME` and `By.XPATH`.
  Code: [`locators/id_class_name_attribute_xpath.py`](locators/id_class_name_attribute_xpath.py),
  report: [`homework/HW_25.11.2026.md`](homework/HW_25.11.2026.md)

## Run

```bash
pip install -r requirements.txt
python locators/tag_name_css_selectors.py
python locators/id_class_name_attribute_xpath.py
```
