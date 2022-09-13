"""
Part of a project. File contains utilities for gathering the data of products from Ceneo
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

def CreatePriceLinkTable(df_product):
    
    i=0
    for product in df_product["Product"]:
        try:
            print("---------------")
            print(product)
            print("---------------")
            product_to_link = product.replace(" ", "+")
            link = str("https://www.ceneo.pl/;szukaj-"+product_to_link+"?nocatnarrow=1")
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')

            #go to 1st site and select 1st item
            tekst_przycisk = soup.find_all('a', class_ = "js_seoUrl")
            tekst_przycsisk_prod_1 = tekst_przycisk[0]
            no_link = tekst_przycsisk_prod_1.attrs["href"]
            link_lista_sklepow = str("https://www.ceneo.pl"+no_link)

            page = requests.get(link_lista_sklepow)#go to webpage with the best product
            soup = BeautifulSoup(page.content, 'html.parser')
            wszystkie_oferty = soup.find_all('a', class_ = "product-price go-to-shop")
            wszystkie_oferty[0].get("href")
            
            #create DataFrame, which contains links and prices
            df_oferts = pd.DataFrame(columns=["cena", 'link'])
            for oferta in wszystkie_oferty: 
                ofert_list = []
                ofert_list.append(oferta.get_text())
                ofert_list.append(oferta.get("href"))
                
                df_oferts.loc[len(df_oferts)] = ofert_list

            #edition of 2 columns - format prices to float, formating link
            df_oferts["cena"]= df_oferts["cena"].str.replace(',', '.').str.replace('\n', '').str.replace('zł', '').str.replace(' ', '').astype(float)

            df_oferts["full_link"] = "https://www.ceneo.pl" + df_oferts["link"]
            df_oferts = df_oferts.drop(columns='link')

            df_oferts.sort_values(by="cena")
            df_best_offer = df_oferts.iloc[0,:]
           
            
            #fill price and link from df_best offer 
            df_product.at[i, 'cena'] = df_best_offer.at['cena']
            df_product.at[i, 'full_link'] = df_best_offer.at['full_link']
            
            i=i+1
        
        #exception in terms occurance of empty list in google ex. Bloomberg television, or given phrase is too long
        except:
            df_product.at[i, 'cena'] = 'Brak ceny dla ' + product
            df_product.at[i, 'full_link'] = "Brak linku dla " + product
            print(product, "is not available on Ceneo / Wrong product. Please check source file")
            i=i+1
            pass
            
    return df_product