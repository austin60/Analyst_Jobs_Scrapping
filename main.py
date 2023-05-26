from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

  
site='https://www.linkedin.com/jobs/data-analysis-jobs/?currentJobId=3601149469&originalSubdomain=ke'
path=Service('C:\\Users\\Admin\\Downloads\\chromedriver_win32')
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=path,options=options)
driver.get(site)

jobs=driver.find_elements(By.CLASS_NAME, "base-search-card__info")

position=[]
company=[]
location=[]
posted=[]

for job in jobs:
   position.append(job.find_element(By.TAG_NAME, 'h3').text)
   company.append(job.find_element(By.TAG_NAME, 'h4').text)
   posted.append(job.find_element(By.TAG_NAME, 'time').text)
   location.append(job.find_element(By.TAG_NAME, 'span').text)

driver.quit()

df=pd.DataFrame({'position':position,'company':company,'location':location,'posted':posted})
df.to_csv('data_analyst_jobs.csv',index=False)
print(df)