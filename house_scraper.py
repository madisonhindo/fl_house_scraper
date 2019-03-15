import time
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

csvfile = open("representative_information.csv", 'w', newline='', encoding='utf-8')
c = csv.writer(csvfile)
c.writerow(['name', ' district and party', ' address', ' phone number'])


driver = webdriver.Chrome('/Users/madisonhindo/Documents/python/fl_house_scraper/chromedriver')
rep_url = driver.get('https://www.myfloridahouse.gov/Sections/Representatives/representatives.aspx')

html = driver.page_source
bs = BeautifulSoup(html, "html.parser")

representative_list = []

def get_rep_profiles(rep_url, bs):
    global representative_list
    profile_list = bs.find_all('div', {'class' : 'team-box'})
    for profiles in profile_list:    
            representative_list.append(str(profiles.find('a').attrs['href']))
            time.sleep(1)
    
contact_links = []

def get_contact_link(representative_list):
   global contact_links
   for rep in representative_list:
        driver.get('https://www.myfloridahouse.gov/' + rep)
        html = driver.page_source
        bs = BeautifulSoup(html, 'html.parser')
        contact = bs.find('div', {'id' : 'sidenav'})
        contact_links.append(contact.find('a').attrs['href'])
        time.sleep(1)
 
get_rep_profiles(rep_url, bs)
get_contact_link(representative_list)

name_list = []
district_list = []

def get_names_and_district(representative_list):
    global name_list
    global district_list
    for rep in representative_list:
        driver.get('https://www.myfloridahouse.gov/' + rep)
        html = driver.page_source
        time.sleep(1)
        try:
                bs = BeautifulSoup(html, 'html.parser')
                name = bs.find('h1').get_text().strip()
                district = bs.find('h2').find_next('h2').get_text().strip()
                name_list.append(name)
                district_list.append(district)
        except:
                name_list.append('None')
                district_list.append('None')
        

get_names_and_district(representative_list)

address_list = []
phone_list = []

def get_contact_info(contact_links):
    for contact in contact_links:
        driver.get('https://www.myfloridahouse.gov/' + contact)
        html = driver.page_source
        time.sleep(1)
        try:
                bs = BeautifulSoup(html, 'html.parser')
                contact_information = bs.find('address')
                contact_info = contact_information.find('ul').find('li')
                address = contact_info.get_text().strip()
                phone = contact_info.find_next('li').get_text()
                address_list.append(address)
                phone_list.append(phone)
        except AttributeError:
                address_list.append('None')
                phone_list.append('None')

get_contact_info(contact_links)

def clean(input):
    return " ".join(str(input).split())

together_list = []

for i in range(len(name_list)):
    together = 'name: ' + clean(name_list[i]) + '\n' + 'district and party: ' + clean(district_list[i]) + '\n' + 'address: ' + clean(address_list[i]) + '\n' + 'phone: ' + clean(phone_list[i]) + '\n\n\n'
            
    together_list.append(together)

row = []
for together in together_list:
        row.append(together)
c.writerow(row)
csvfile.close()