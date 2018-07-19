"""Code used to get the urls that will be accessed in the future
This code intended for a specific website and should not be used for other
websites without modification. This code should be broken down and modularized.
"""
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome

import time


def get_links(baseurl):
    nav_class_0 = '_class_name_0'
    nav_class_1 = '_class_name_1'

    links_dict = {}

    # send browser to baseurl
    browser.get(baseurl)

    # get html for the base page
    html = browser.page_source

    # use bs4 to parse the html
    soup = BeautifulSoup(html, 'html.parser')

    # find the title buttons to be clicked later
    nav_0 = soup.select('button.{}'.format(nav_class_0))
    nav_0_text = [elem.text for elem in nav_0]
    links_dict[nav_0_text[0]] = soup.select('a.{}'.format(nav_class_1))

    for idx in range(1, len(nav_0_text)):
        # find and click
        print(nav_0_text[idx])
        browser.execute_script("window.scrollTo(0,0)")
        browser.find_element_by_xpath('//button[text()="{}"]'.format(
            nav_0_text[idx])).click()
        # wait for some time to allow animation on webpage to complete if
        # needed
        time.sleep(1)
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        links_dict[nav_0_text[idx]] = soup.select('a.{}'.format(nav_class_1))

    return links_dict


if __name__ == "__main__":
    # open selenium browser and navigate to the base_url
    browser = Chrome()

    url = 'some-url.com'

    get_links(url)
