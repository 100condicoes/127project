from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL dos Exoplanetas da NASA
#START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(8)

planets_data = []

# Defina o método de coleta de dados dos exoplanetas
def scrape():

    #for i in range(1,2):
        #while(True):
            #time.sleep(2)
            

            # Objeto BeautifulSoup
    soup = BeautifulSoup(browser.page_source, "html.parser")

            #current_page_num = int(soup.find_all("input", attrs={"class", "page_num"})[0].get("value"))

            #if current_page_num < i:
              #  browser.find_element(By.XPATH, value='//[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            #elif current_page_num > i:
              #  browser.find_element(By.XPATH, value='//[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            #else:
                #break       
        
    StarTable= soup.find("table", attrs={"class","wikitable"})
    TableBody= StarTable.find("tbody")
    tableRows = TableBody.find_all("tr")

        # Loop para encontrar o elemento dentro das tags ul e li
    #for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
    for row in tableRows:

        tableCalls = row.find_all("td")
           
        temp_list = []

        #for index, li_tag in enumerate(li_tags):

            # #if index == 0:                   
            #    temp_list.append(li_tag.find_all("a")[0].contents[0])
            # #else:
            #     try:
            #         temp_list.append(li_tag.contents[0])
            #     except:
            #         temp_list.append("")

            # hyperlink_li_tag = li_tags[0]
        for cowData in tableCalls:
            data = cowData.text.strip()
            temp_list.append(data)
            
            #temp_list.append("https://exoplanets.nasa.gov"+hyperlink_li_tag.find_all("a", href=True)[0]["href"])
            planets_data.append(temp_list)

    # browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    # print(f'Coleta Concluída {i} ...' )
    
scrape()
#print(planets_data)
stars_data = []
for i in range(0,len(planets_data)):

    Star_names = planets_data[i][1]
    Distance = planets_data[i][3]
    Mass = planets_data[i][5]
    Radius = planets_data[i][6]
    Lum = planets_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

print(stars_data)

#headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink"]
headers = ["stars_name", "Distance", "Mass", "Radius", "Lum"]


#planet_df_1 = pd.DataFrame(planets_data, columns=headers)
stars_data_df = pd.DataFrame(stars_data, columns=headers)

#planet_df_1.to_csv("update_dados_coletados.csv", index=True, index_label="id")
stars_data.to_csv("estrelas_encontradas.csv", index=True, index_label="id")