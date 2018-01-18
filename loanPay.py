from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import secrets

# create secrets.py in the same directory, define username, password, loadNum variables
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 7)


try:
    browser.get('https://secure.nelnet.net/Payment/Index')
    assert 'Login - Nelnet' in browser.title
    browser.find_element_by_name('usertype').click()
    browser.find_element_by_id('username').send_keys(secrets.username)
    browser.find_element_by_id('submit-username').click()
    browser.implicitly_wait(1)
    browser.find_element_by_id('Password').send_keys(secrets.password)
    browser.find_element_by_id('submit-password').click()
    wait.until(EC.title_is('Payment - Nelnet')) # had trouble with latency, so now we wait until the page is fully
    # loaded
    #wait.until(EC.element_to_be_clickable((By.ID, 'groupLevel')))
    browser.find_element_by_id('groupLevel').click()
    wait.until(EC.presence_of_element_located((By.ID, secrets.loanNum)))
    browser.find_element_by_id(secrets.loanNum).send_keys('100')
    browser.find_element_by_id('proceedButton').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Pay Now')]"))).click() # wait until the button is loaded
    browser.implicitly_wait(3)
    assert 'Confirmation Number' in browser.page_source
    print 'success!'
    browser.quit()

except KeyboardInterrupt:
    browser.quit()
