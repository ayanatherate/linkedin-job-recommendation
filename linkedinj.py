# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 22:47:43 2022

@author: User
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import pandas 
import streamlit
import spacy



chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

url = 'https://www.linkedin.com/jobs/search?keywords=Data%20Scientist&location=India'
#driver = webdriver.Chrome(r"C:\Users\User\Desktop\PROGRAM_FILES\chromedriver.exe")
driver.get(url)


driver.maximize_window() 
driver.minimize_window() 
driver.maximize_window() 
driver.switch_to.window(driver.current_window_handle)
driver.implicitly_wait(10)


i = 2
while i <= 5+1: 
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    i = i + 1
    try:
        
        l=driver.find_element(By.XPATH, "/html/body/div/div/main/section/button").click()
        i=i+1
        time.sleep(5)
    except:
         pass

src=driver.page_source
soup = BeautifulSoup(src, 'lxml')



job_links=[]

names=soup.find_all('h4',{'class':'base-search-card__subtitle'})
roles=soup.find_all('div',{'class':'base-search-card__info'})
location=soup.find_all('span',{'class':'job-search-card__location'})

for item in range(len(names)):
    try:
        job_click_path = f'/html/body/div/div/main/section[2]/ul/li[{item+1}]/div/a'
        job_click = driver.find_element(By.XPATH,job_click_path).get_attribute('href')
        job_links.append(job_click)
    except:
        job_links.append('n')
    
names=[i.get_text() for i in names]
roles=[i.get_text() for i in roles]
location=[i.get_text() for i in location]
print(names)
st.write(names)


import spacy

# load pre-trained model
nlp = spacy.load('en_core_web_sm')


def extract_skills(resume_text):
    nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    
    # reading the csv file
    data = pd.read_csv(r"C:\Users\User\Desktop\DATASETS_ALL\skills_ - skills.csv") 
    
    # extract values
    skills = list(data.columns.values)
    
    skillset = []
    
    # check for one-grams
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
    
    # check for bi-grams and tri-grams 
    for token in nlp_text.noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)
    
    return [i.capitalize() for i in set([i.lower() for i in skillset])]


import re


jd=[]
post_time=[]
desc_c=[]
skill_list=[]
for link in job_links:
    
    if link!='n':
        driver.get(link)
        jd_click_path= 'html/body/main/section/div/div/section/div/div/section/div'
        
        jd0 = driver.find_element(By.XPATH,jd_click_path).get_attribute('innerText')
        jd0=re.sub('\n',' ',jd0)
        skills=extract_skills(jd0)
        
        str_skills=' '
        for i in skills:
            str_skills+=i+','+' '
        skill_list.append(str_skills)
        
        print(str_skills)
        jd.append(jd0)
        
        postedtimepath= 'html/body/main/section/div/section[2]/div/div/div/h4/div[2]/span'
        timej=driver.find_element(By.XPATH,postedtimepath).get_attribute('innerText')
        post_time.append(timej)
        time.sleep(3)
        #print(timej)
    else:
        jd.append('None')
        skill_list.append('None')
        post_time.append('None')
        
import pandas as pd

data_jobs=pd.DataFrame(list(zip(names,roles,location,post_time,job_links,jd,skill_list)),columns=['Company','Role','Location','Job Post Time','LinkedIN job link','Description','Skills Needed'])

print(data_jobs)
    
        
    
