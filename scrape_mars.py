from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # Scrape 1
    url_1 = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url_1)

    html_1 = browser.html
    soup = BeautifulSoup(html_1, 'html.parser')

    # add to dictionary 
    time.sleep(7)
    news_t = soup.find("div", class_="list_text").find("div", class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text


    # Scrape 2
    url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_2)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(7)
    browser.click_link_by_partial_text('more info')
    time.sleep(7)

    html2 = browser.html
    soup = BeautifulSoup(html2, 'html.parser')

    extension = soup.find("article").find("figure", class_="lede").a["href"]
    link = "https://www.jpl.nasa.gov"
    featured_image_url = link + extension



    # Scrape 3
    url_3 = "http://space-facts.com/mars/"
    tables = pd.read_html(url_3)
    tables

    mars_facts_df = tables[0]
    mars_facts_df.columns=["Key", "Value"]
    mars_facts_df = mars_facts_df.set_index("Key")
    mars_facts_df

    mars_facts = mars_facts_df.to_html(header=True, index=True)

    # Scrape 4
    hemisphere_image_urls = []

    url_4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Scrape Cerb
    browser.visit(url_4)
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(5)
    html_4 = browser.html
    soup = BeautifulSoup(html_4, 'html.parser')

    cerberus_title = soup.find("section", class_="block metadata").find("h2", class_="title").text
    cerberus_image = soup.find("div", class_="downloads").a["href"]

    # Create cerb dictionary
    cerberus = {
        "title": cerberus_title,
        "img_url": cerberus_image
    }
    
    # Append list with dictionary
    hemisphere_image_urls.append(cerberus)

    # Scrape Schiap
    browser.visit(url_4)
    time.sleep(5)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(5)
    html_5 = browser.html
    soup = BeautifulSoup(html_5, 'html.parser')

    schiap_title = soup.find("section", class_="block metadata").find("h2", class_="title").text
    schiap_image = soup.find("div", class_="downloads").a["href"]

    # Create schiap dictionary
    schiap = {
        "title": schiap_title,
        "img_url": schiap_image
    }
    
    # Append list with dictionary
    hemisphere_image_urls.append(schiap)

    # Scrape Syrtis
    browser.visit(url_4)
    time.sleep(5)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(5)
    html_6 = browser.html
    soup = BeautifulSoup(html_6, 'html.parser')

    syrtis_title = soup.find("section", class_="block metadata").find("h2", class_="title").text
    syrtis_image = soup.find("div", class_="downloads").a["href"]   

    # Create syrtis dictionary
    syrtis = {
        "title": syrtis_title,
        "img_url": syrtis_image
    }
    
    # Append list with dictionary
    hemisphere_image_urls.append(syrtis)

    # Scrape Valles
    browser.visit(url_4)
    time.sleep(5)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(5)
    html_7 = browser.html
    soup = BeautifulSoup(html_7, 'html.parser')

    valles_title = soup.find("section", class_="block metadata").find("h2", class_="title").text
    valles_image = soup.find("div", class_="downloads").a["href"]

    # Create valles dictionary
    valles = {
        "title": valles_title,
        "img_url": valles_image
    }

    # Append list with dictionary
    hemisphere_image_urls.append(valles)


     #___________________________________ # MongoDB

    # Create empty dictionary for all Mars Data.
    listings = {}
    
    listings["news_t"] = news_t
    listings["news_p"] = news_p

    listings["featured_image_url"] = featured_image_url
    listings["hemisphere_image_urls"] = hemisphere_image_urls
    listings["mars_facts"] = mars_facts

    return listings 
    
    
    