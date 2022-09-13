"""
Part of a project. File contains utilities for gathering the data from Google
"""
import pandas as pd
from selenium import webdriver


def getListofProducts(url):
    df_oferts = pd.DataFrame(columns=["Product"])

    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = webdriver.Chrome('/Users/patryk/.../chromedriver')#use only without webdriver_manager

    try:
        driver.get(url)
        
        for i in range(20):
            product_google = driver.find_elements_by_class_name('pymv4e')[i].text
            df_oferts.at[i, 'Product'] = product_google
            print(product_google)

        nan_value = float("NaN")
        df_oferts.replace("", nan_value, inplace=True)

        df_oferts.dropna(subset = ["Product"], inplace=True)
        df_oferts = df_oferts.reset_index().drop(columns="index")
        driver.close()
        return df_oferts 
        #exception, when is no list of products in google
    except:
        print('\n !!! Error !!! \n Wrong phrase. Google couldnt create lists of products. Give a correct phrase ex.: best phone 2022!\n\n')
        return df_oferts
