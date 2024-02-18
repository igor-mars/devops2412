import requests
import random
from selenium import webdriver
import names

'''
Testing Github API - Create a program in python that goes to the following API and
checks that at least 5 git repositories exists - https://api.github.com/users/avielb/repos
'''
response = requests.get('https://api.github.com/users/avielb/repos')
count_repos = len(response.json())
assert count_repos >= 5

'''
Testing agify API - Create a program in python that generates 3 random names and
checks that the age from the reply in this link: https://api.agify.io/?name=<name> is
between 0 - 120
'''

for i in range(3):
    name = names.get_first_name()
    response = requests.get("https://api.agify.io/?name=" + name)
    data = response.json()
    age = data['age']
    assert age >=0 and age <= 120



'''
Testing universities API - Go to http://universities.hipolabs.com/search?country=Israel
and make sure that israel has at least 5 universities
'''
response = requests.get('http://universities.hipolabs.com/search?country=Israel')
count_repos = len(response.json())
assert count_repos >= 5

'''
Using Selenium go to https://www.ycombinator.com/ and test that the title is “Y
Combinator”
'''
driver = webdriver.Chrome()
driver.get('https://www.ycombinator.com/')
title = driver.title
assert title == 'Y Combinator'
driver.quit()


'''
Using selenium go to https://hub.docker.com and test the the title is “Docker Hub
Container Image Library | App Containerization”
'''
driver = webdriver.Chrome()
driver.get('https://hub.docker.com')
title = driver.title
assert title == 'Docker Hub Container Image Library | App Containerization'
driver.quit()




