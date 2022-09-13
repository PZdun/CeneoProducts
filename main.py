"""
Project made by Patryk Zduńczak during DataScience studies on Warsaw University of Technology
script to create list of recomended product from a given phrase
script is based on google recomendation list and polish platform Ceneo
"""

from webbrowser import get
from numpy import empty

from selenium_utilities import *
from bs4_utilities import *


def main():
    #get the phrase you are looking for
    fraza = input("Given phrase: ")
    fraza = fraza.replace(" ", "+")
    url = 'https://google.com/search?q=' + fraza
    
    #create list of product from Google
    df_oferts = getListofProducts(url)
    
    if df_oferts.empty:
        
        exit()
    else:
        #look for the best offers in Ceneo
        final_df = CreatePriceLinkTable(df_oferts)

        # create to ExcelWriter
        final_result = pd.ExcelWriter('list_of_products.xlsx')
        # write product data to excel
        final_df.to_excel(final_result)
        # save the product result excel
        final_result.save()
        print('\n Products data is successfully written into Excel File!\n')

if __name__ == '__main__':
	main()    