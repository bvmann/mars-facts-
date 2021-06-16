#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import pandas as pd 
import requests 
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    mars_data={}
    url = "https://redplanetscience.com/#"





    executable_path={'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome',**executable_path, headless=False)
    
    browser.visit(url)
    

    html=browser.html
    soup = BeautifulSoup(html,"html.parser")

    news_title=soup.find('div',class_="content_title").get_text()
    news_p=soup.find('div',class_="article_teaser_body").get_text()


    browser.quit()

    executable_path={'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome',**executable_path, headless=False)
    space_imageurl="https://spaceimages-mars.com/"
    browser.visit(space_imageurl)

    html=browser.html
    soup = BeautifulSoup(html,"html.parser")
    img_url = soup.find("img",class_="headerimage fade-in")["src"]


    img_url=space_imageurl + img_url


    browser.quit()



#used Pandas to read galaxyfacts website
    marsfacts_url="https://galaxyfacts-mars.com/"
    marstable=pd.read_html(marsfacts_url)




#chose which table I wanted and created mars 
    mars = marstable[1]


    mars.set_index(mars[0],drop=True,inplace=True)


    


    mars.drop([0],axis=1,inplace=True)


    


    mars.rename(columns={'1':'Mars Stats'},inplace=True)
    mars





    mars.index.rename("Mars",inplace=True)


  


    mars["Mars Stats."]=mars[1]


 


    mars.drop([1],axis=1,inplace=True)





    mars_table=mars_html=mars.to_html().replace("\n"," ")



    executable_path={'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome',**executable_path, headless=False)
    hemisphere_url="https://marshemispheres.com"
    browser.visit(hemisphere_url)



    html=browser.html
    soup=BeautifulSoup(html,'html.parser')



    soup.find("a",class_="itemLink product-item")['href']



    body = soup.find('div', class_='collapsible results')

    categories = body.find("a",class_="itemLink product-item",href=True)




    stuff = body.find_all("h3")




    hemis=[]
    for x in stuff:
        spheres=x.text.strip()
        hemis.append(spheres)




    import time


    hemisphere_image_urls =[]


    for x in hemis:
        browser.links.find_by_partial_text(x).click()


        html=browser.html
        soup=BeautifulSoup(html,'html.parser')
        #image url 
        download = soup.find("div",class_="downloads")
        img_source=download.find_all('li')
        pic_url=img_source[0].find('a',target='_blank')['href']
        img_url=hemisphere_url+"/"+pic_url 
        #title
        cover=soup.find('div',class_='cover')
        title=cover.find('h2',class_="title")
        title=title.text.strip()

        hs={"title":title,"img_url":img_url}
        hemisphere_image_urls.append(hs)
        time.sleep(2)
        #back to start page 
        browser.links.find_by_partial_text('Back').click()


   


    browser.quit()
    
    mars_data["news_title"]=news_title
    mars_data["news_body"]=news_p
    mars_data["feat_image"]=img_url
    mars_data["mars_table"]=mars_table
    mars_data["hemisphere_urls"]=hemisphere_image_urls
    

    return mars_data






