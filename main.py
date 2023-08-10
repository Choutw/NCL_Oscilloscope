from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#set the path of chromeDriver
driver = webdriver.Chrome()

#set url
default_url = "http://192.168.50.133/scpictrl.htm"
driver.get(default_url)

#input command as key 
element = driver.find_element(By.XPATH, "//html/body/table/tbody/tr[5]/td[3]/table/tbody/tr[6]/td/form/table/tbody/tr[1]/td[3]/input")
element.send_keys("MEAS:RES:ACT? RMS")

#click the send button
button = driver.find_element(By.CSS_SELECTOR, "body > table > tbody > tr:nth-child(5) > td:nth-child(3) > table > tbody > tr:nth-child(6) > td > form > table > tbody > tr:nth-child(1) > td:nth-child(4) > input[type=submit]")
button.click()

#direct to inline frame by XPath
WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//html/body/table/tbody/tr[5]/td[3]/table/tbody/tr[6]/td/form/table/tbody/tr[5]/td[3]/iframe")))

#import local time
localtime = time.asctime(time.localtime(time.time()))

#identify element and get text method
Res = driver.find_element(By.XPATH, "//html/body").text
print("The response data is: " + Res + " @" + localtime)

#write the response data to file 
f = open("scpi_response_data.txt", "a")

f.write(Res)
f.write("\n")

f.close()

#move out of frame to parent page
driver.switch_to.default_content()
driver.quit()
