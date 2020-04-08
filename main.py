from queue import Queue
from time import sleep
from sympy import *
from sympy.parsing.latex import parse_latex
from selenium import webdriver
import requests

driver = webdriver.Chrome()
i=150
q=[1,2,3,4,5]

while i!=0:
    try:
            if q[0]==q[1] and q[1]==q[2] and q[2]==q[3]and q[3]==q[4]:
                driver.close()
                driver = webdriver.Chrome()
                q = [1, 2, 3, 4, 5]

            driver.get("view-source:http://tasks.sprush.rocks:8084/")
            if 'SPR{' in driver.page_source:
                print(driver.page_source)
                exit(0)
            i=int(driver.page_source.split("Осталось:")[1].split('<')[0])
            q=q[1:]
            q.append(i)
            print(q)
            main_page = driver.page_source.split("$$")[1]
            response = requests.get(f"http://api.wolframalpha.com/v2/query?input=\"{main_page} approximate\"&appid=R6J573-3Q9RU2PK5K")
            eq=response.text.split("<plaintext>")[1].split("</plaintext>")[0].replace("≈","=").split("=")[-1].replace("×","*").replace("^","**").replace('...','')
            print(eq)
            if '**' in eq:
                st=str(int(eval(eq)))
            else:
                st=str(eval(eq))
            if '.' in st:
                while st[len(st)-1]=='0':
                    st=st[:-1]
                if st[len(st)-1]=='.':
                    st=st[:-1]
            print(st)
            driver.get("http://tasks.sprush.rocks:8084/")
            if 'SPR{' in driver.page_source:
                print(driver.page_source)
                exit(0)
            el=driver.find_element_by_xpath("/html/body/div/center/form/input")
            el.send_keys(st)
            el.submit()
    except SyntaxError:
        continue