import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as BS


def parse(URL):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)
    html = driver.page_source
    soup = BS(html, "html.parser")
    last_video = soup.find("a", {"id": "video-title"})
    link = "https://www.youtube.com/" + last_video.get("href")
    title = last_video.get("title")
    driver.close()
    driver.quit()
    return title, link
