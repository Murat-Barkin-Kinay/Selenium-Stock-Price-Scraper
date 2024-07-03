from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_stock_price(ticker):
    driver = webdriver.Chrome()
    url = f"https://finance.yahoo.com/quote/{ticker}"
    driver.get(url)
    while True: 
        try:
            driver.implicitly_wait(10)
            price_element = driver.find_element(By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[1]/span')
            price = price_element.text
            print(f"The current stock price of {ticker} is: ${price}")
            time.sleep(2)
        except Exception as e:
            print(f"Error: {e}")
            driver.quit()

def main():
    ticker = input("Enter the stock ticker whose price you want logged: ")
    get_stock_price(ticker)

if __name__ == "__main__":
    main()
