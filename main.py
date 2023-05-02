from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Serviceオブジェクトを作成する
service = Service(executable_path=ChromeDriverManager().install())

# WebDriverを起動する
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
print("1")
# ブラウザを開く
driver.get('https://google.com')
print("2")

# ブラウザを操作する（例：検索ボックスにキーワードを入力する）
#search_box = driver.find_element_by_name('q')
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Python')
print("3")

# ブラウザを操作する（例：検索ボタンをクリックする）
search_button = driver.find_element(By.NAME, 'btnK')
search_button.click()

# ブラウザを閉じる
#driver.quit()
