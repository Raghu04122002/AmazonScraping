import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


def get_url(search_term):
    template = 'https://www.amazon.in/s?k={0}'
    search_term = search_term.replace(' ','+')
    url = template.format(search_term)
    url+= '&page={}'
    return url

def extract_record(item):
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.in'+atag.get('href')
    try:
         price_parent = item.find('span','a-price')
         price = price_parent.find('span','a-offscreen').text
    except AttributeError:
        return
    try:
        
         rating = item.i.text
         rating_count = item.find('span',{'class':'a-size-base', 'dir':'auto'}).text
    except AttributeError:
        rating=''
        review_count=''

    result = (description,price,rating,review_count,url)
    
    return result

def main(search_term):
    driver = webdriver.Chrome()
    records =[]
    url = get_url(search_term)

    for page in range(1,21):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source,'html.parser')
        results = soup.find_all('div',{'data-component-type':'s-search-result'})
        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)

    driver.close()
   
    df = pd.DataFrame(records, columns=['product', 'price', 'rating', 'rating_count', 'product url'])
    df.to_csv('results.csv', index=False)



main('bags')

    
                

        
        




    

    

    

    

