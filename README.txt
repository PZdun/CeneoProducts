# Patryk Zduńczak project for Data Science studies on Warsaw University of Technology 2022

# Framework for creating list of items basing on recommended ads in Google and listing their best price and link to shop from Ceneo

- selenium_ulilities.py - contains a function which creates a list of items based on a given phrase np. "Best phones 2022" (Google, Selenium)
- bs4_utilities.py - contains a function wich looks for the best offer of each product from a list. Function is adding columns with price and link. (Ceneo, BeautifulSoup)
- MAIN SCRIPT - main.py - script takes phrase, on which list of items is build. It returns results list_of_products.xlsx, which contains 3 columns:
    * product
    * cena
    * full_link

Program supports additional scenarios:
- Google doesn't show list of recomemnded products. Return of a program: 
    
    !!! Błąd !!! 
    B!!! Error !!! \n Wrong phrase. Google couldn't create lists of products. Give a correct phrase ex.: best phone 2022!

It can happen when we pass phrase like: "radio eska", or any other phrase which doesn't suggest a mainstream products

- Ceneo couldn't find product name from a list. In an excel file user will see an information in a particular row.

