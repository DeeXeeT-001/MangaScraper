from bs4 import BeautifulSoup
import requests
from time import sleep


def findManga():
    htmlText = requests.get("https://mangakakalot.com/").text
    soup = BeautifulSoup(htmlText, "lxml")

    manga = soup.find("div", class_="itemupdate first")
    print(manga)


findManga()