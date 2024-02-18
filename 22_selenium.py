from selenium import webdriver
from time  import sleep
dr = webdriver.Firefox()
dr.get("file:///C:/Users/igor/PycharmProjects/tip_calc/index.html")
# dr.get("https://github.com")
billamt = dr.find_element(by="id", value="billamt")
billamt.send_keys("100")
dr.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[3]").click()
dr.find_element(by="id", value="peopleamt").send_keys("5")
dr.find_element(by="id", value="musicQual").send_keys("5")
dr.find_element(by="id", value="calculate").click()
actual = dr.find_element(by="id", value="tip").text
expected = "9"
assert expected == actual
sleep(20)