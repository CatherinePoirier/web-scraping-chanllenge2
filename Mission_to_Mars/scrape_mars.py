import requests

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import time
from IPython.display import HTML 



def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_titlelong= soup.find_all('div', class_="content_title")
    news_title=news_titlelong[1].text
    news_p= soup.find_all('div', class_="article_teaser_body")
    news_p=(news_p[0].text)

  
    url="https://www.jpl.nasa.gov/images?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)
    button = browser.find_by_css(".BaseImage")
    button.click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image= soup.find_all('img', class_="BaseImage")
    featured_image_url=(featured_image[0]['src'])

    
    url_space = "https://space-facts.com/mars/"
    tables = pd.read_html(url_space)
    df = tables[0]
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)
    html_table=df.to_html()
   
    

    
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(1)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser') 
    descriptions = soup.find_all('div', class_='description')

    h_title = []
    hold=[]
    for desc in descriptions:
            hold=desc.find('h3')
            print(hold)
            h_title.append(hold.contents)
    mars_hem_1=(h_title[0])
    mars_hem_2=(h_title[1])
    mars_hem_3=(h_title[2])
    mars_hem_4=(h_title[3])

    button = browser.find_by_css(".thumb")[0]
    button.click()
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_image1= soup.find('img', class_="wide-image").get("src")
    mars_image1=('https://astrogeology.usgs.gov' + mars_image1)

    browser.visit(url)  
    time.sleep(1)

    button = browser.find_by_css(".thumb")[1]
    button.click()
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_image2= soup.find('img', class_="wide-image").get("src")
    mars_image2=('https://astrogeology.usgs.gov' + mars_image2)
    browser.visit(url) 

    button = browser.find_by_css(".thumb")[2]
    button.click()

    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_image3= soup.find('img', class_="wide-image").get("src")
    mars_image3=('https://astrogeology.usgs.gov' + mars_image3)
    browser.visit(url)  

    button = browser.find_by_css(".thumb")[3]
    button.click()

    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_image4= soup.find('img', class_="wide-image").get("src")
    mars_image4=('https://astrogeology.usgs.gov' + mars_image4)

    browser.visit(url)  

    hemisphere_image_urls= [
                {"title": mars_hem_1[0], "img_url": mars_image1},
                {"title": mars_hem_2[0], "img_url": mars_image2},
                {"title": mars_hem_3[0], "img_url": mars_image3},
                {"title": mars_hem_4[0], "img_url": mars_image4}
                ]

    mars_data = {
            "news_title": news_title, 
            "paragraph": news_p,
            "featured_image": featured_image_url,
            "mars_facts": html_table,
            "hemisphere_images": hemisphere_image_urls
    }

    browser.quit()
    

    return mars_data

