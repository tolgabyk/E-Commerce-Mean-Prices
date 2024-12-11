from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def amazon(urun):
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.amazon.com.tr")

    try:
        # Arama kutusuna eriş ve ürün ismini ara
        arama_yeri = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='twotabsearchtextbox']"))
        )
        arama_yeri.send_keys(urun)
        arama_yeri.send_keys(Keys.ENTER)

        fiyatlar = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@data-cy, 'price-recipe')]//span[@class='a-price-whole']"))
    )
        fiyat_listesi = [fiyat.text for fiyat in fiyatlar]
        return fiyat_listesi

    except Exception as e:
        print("Hata oluştu:", e)

    finally:
        driver.quit()

def n11(urun):
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  
    driver = webdriver.Chrome(options=options)

    arama_url = f"https://www.n11.com/arama?q={urun.replace(' ', '+')}"
    driver.get(arama_url)

    try:
        fiyatlarr = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@id='view']//ul[@class='list-ul']//ins"))
    )
        
        fiyatn11 = [fiyat.text for fiyat in fiyatlarr]

        return fiyatn11
    
    except Exception as e:
        print("n11 fiyatları çekilemedi:",e)
        
    finally:
        driver.quit()

def trendyol(urun):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,1024")
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    arama_url = f"https://www.trendyol.com/sr?q={urun}&qt={urun}&st={urun}&os=1"
    driver.get(arama_url)


    try:
        fiyatlar = WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.XPATH,"//div[@class='infinite-scroll']//div[@class='prc-box-dscntd']"))
        )
        fiyat_trendyol = [fiyat.text for fiyat in fiyatlar]
        return fiyat_trendyol
    
    except Exception as e:
        print("Trendyol Fiyatları Çekilemedi", e)

    driver.quit()
    

def hepsiburada(urun):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,1024")
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    arama_url = f"https://www.hepsiburada.com/ara?q={urun.replace(' ', '+')}"
    driver.get(arama_url)
        
    try:
        fiyatlar = WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH,"//div[@class='VVfQFa_rVJ7k5k6NHFV3']//li[@class='productListContent-zAP0Y5msy8OHn5z7T_K_']//div[@data-test-id='price-current-price']"))
        )
        fiyat_hepsiburada = [fiyat.text for fiyat in fiyatlar]
        return fiyat_hepsiburada
    
    except Exception as e:
        print("eBay fiyatları çekilemedi:", e)
        driver.quit()
