import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://rezka.ag')
browser.implicitly_wait(30)
item_to_search = 'побег'
browser.find_element_by_css_selector('[id="search-field"]').send_keys(item_to_search)
browser.find_element_by_css_selector('[id="search-field"]').send_keys(Keys.RETURN)
F = True
page = 1
while F:
    films = browser.find_elements_by_css_selector('[class="b-content__inline_item-link"]')
    for film in films:
        actual_item = film.text
        assert item_to_search in actual_item.lower()
    print('Page#' + str(page) + ' done.')
    page += 1
    if not (browser.find_element_by_css_selector('[class="b-navigation__next i-sprt"]').is_displayed()):
        print('End')
        F = False
    else:
        next = browser.find_element_by_css_selector('[class="b-navigation__next i-sprt"]')
        next.click()
browser.close()


    