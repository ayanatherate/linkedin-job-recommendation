
from selenium import webdriver
#selenium is used to automate web browsers
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import os
import re
import math
from sklearn.feature_extraction.text import CountVectorizer as cv
cv=cv()
from sklearn.metrics.pairwise import cosine_similarity as cosim

#taking user inputs
Role=str(input('Enter job role: '))
Country=str(input('Enter country: '))
no_jobs=int(input('Enter no of jobs to scrape:'))
skill_user=list(map(str, input('Enter your skills, space separated (ex: Python numpy pandas): ').split(' ')))   
#print(skill_user)

url = f'https://www.linkedin.com/jobs/search?keywords={Role}&location={Country}'

#preventing chrome browser from popping up while scraping
chrome_options = webdriver.ChromeOptions()
#chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
#driver = webdriver.Chrome(r"C:\Users\User\Desktop\PROGRAM_FILES\chromedriver.exe")
driver.get(url)

driver.maximize_window() 
driver.minimize_window() 
driver.maximize_window() 
driver.switch_to.window(driver.current_window_handle)
driver.implicitly_wait(10)

#enabling scrolling till page limit
i = 2
while i <= math.floor(0.07*(no_jobs//10)): 
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

#scraping job names, roles, location
names=soup.find_all('h4',{'class':'base-search-card__subtitle'})
roles=soup.find_all('span',{'class':'sr-only'})
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



import spacy

# load pre-trained model
nlp = spacy.load('en_core_web_sm')

#function to extract skills from job description corpus
def extract_skills(resume_text):
    nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    
    # reading the csv file
    data = pd.read_csv(r"https://raw.githubusercontent.com/ayanatherate/findmyjobbot/main/skills%20-%20skills%20(1).csv") 
    
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

#function to scrape educational qualification requirements from job description corpus
def extract_edu_qualf(x):
    find=['Bachelor of Engineering','Master of Engineering','bachelor of technology','master of technology','BTech','MTech','Bsc','Msc'
          'Bachelor of Business Administration','Master of Business Administration','bba','mba'
         'bachelor of computer applications','master of computer applications','bca','mca','bcom'
          'mcom','phd']
    
    for i in find:
        pattern = i.lower()
        x = x.replace('.', '')
        if pattern == 'bachelor of engineering':
            return 'btech'
        elif pattern == 'master of engineering':
            return 'mtech'
        elif pattern == 'bachelor of technology':
            return 'btech'
        elif pattern == 'master of technology':
            return 'mtech'
        elif pattern == 'bachelor of business administration':
            return 'bba'
        elif pattern == 'master of business administration':
            return 'mba'
        elif pattern == 'bachelor of computer applications':
            return 'bca'
        elif pattern == 'master of computer applications':
            return 'mca'
        else:
            truth = re.findall(pattern, x.lower())
            if truth:
                return pattern






jd=[]
post_time=[]
desc_c=[]
skill_list=[]
skill_scores=[]
edu_qualf=[]

#visits each job url scraped from main page and scrapes job description,
# compares cosine similarity score with user's skills
for link in job_links:
    
    if link!='n':
        driver.get(link)
        jd_click_path= 'html/body/main/section/div/div/section/div/div/section/div'
        
        jd0 = driver.find_element(By.XPATH,jd_click_path).get_attribute('innerText')
        jd0=re.sub('\n',' ',jd0)
        
        
        skills=extract_skills(jd0)
    
        edu=extract_edu_qualf(jd0)
        
        edu_qualf.append(edu)
        
        str_skills=''
        str_user_skills=''
        
        for i in skills:
            str_skills+=i+','+' '
        skill_list.append(str_skills)
        
        #print(str_skills)
        
        for i in skill_user:
            str_user_skills+=i+','+' '
        #skill_list.append(str_user_skills)
        
        try:
            cv.fit([str_skills])
        except ValueError:
            cv.fit(['None'])
        cv_=cv.transform([str_skills]).toarray()
        cv_user=cv.transform([str_user_skills]).toarray()
        
        
        score=cosim(cv_,cv_user)[0][0]
        skill_scores.append(round((100*score),2))
        
        #print(str_skills)
        jd.append(jd0)
        
        postedtimepath= 'html/body/main/section/div/section[2]/div/div/div/h4/div[2]/span'
        timej=driver.find_element(By.XPATH,postedtimepath).get_attribute('innerText')
        post_time.append(timej)
        
        if no_jobs<15:
            time.sleep(10)
        else:
            time.sleep(5)
        #print(timej)
    else:
        jd.append('None')
        skill_list.append('None')
        post_time.append('None')
print()        

#saves to dataframe
data_jobs=pd.DataFrame(list(zip(names,roles,location,post_time,job_links,jd,skill_list,edu_qualf,skill_scores)),columns=['Company','Role','Location','Job Post Time','LinkedIN job link','Description','Skills Needed','Qualif Requirement found','Skill Match(%)'])

#data cleaning
def removen(x):
    import re
    x=re.sub('\n',' ',x)
    return x

data_jobs['Company']=data_jobs['Company'].apply(lambda x: removen(x))
data_jobs['Role']=data_jobs['Role'].apply(lambda x: removen(x))
data_jobs['Location']=data_jobs['Location'].apply(lambda x: removen(x))

def matchtime(x):
    
    """
    ranks (assigns a number) to jobs
    according to time (of job posting) for final sorting

    """
    x=x.split(' ')
    
    rank=0
    if 'hour'in x:
        rank+=int(x[0])+100
    elif 'hours' in x:
        rank+=int(x[0])+100
        
    elif 'week' in x:
        rank+=int(x[0])+1000
    elif 'weeks' in x:
        rank+=int(x[0])+1000
        
    elif 'day' in x:
        rank+=int(x[0])+10000
    elif 'days' in x:
        rank+=int(x[0])+10000
        
    elif 'month' in x:
        rank+=int(x[0])+100000
    elif 'months' in x:
        rank+=int(x[0])+100000
        
    elif 'year' in x:
        rank+=int(x[0])+1000000
    elif 'years' in x:
        rank+=int(x[0])+1000000
    else:
        rank+=1000000
    return rank
        
        
data_jobs['rank']=data_jobs['Job Post Time'].apply(lambda x: matchtime(x))
print(data_jobs)

#sorting
data_jobs.sort_values(by=['Skill Match(%)'],ascending=False,inplace=True)
data_jobs.sort_values(by=['rank'],ascending=True,inplace=True)

data_jobs.reset_index(drop=True,inplace=True)
data_jobs.drop(['rank'],axis=1,inplace=True)

print()
print()
print()
print()
print()
print(f"On an average, your skills matched with:{sum(data_jobs['Skill Match(%)'])/len(data_jobs)} % of all Skill requirements of jobs in this list.")

print()
print('Task Finished. Open your Downloads folder to find a csv named "saved_scraped_jobs" ')
data_jobs.to_csv('../Downloads/saved_scraped_jobs.csv')
