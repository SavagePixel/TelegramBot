import requests
from bs4 import BeautifulSoup

url = ""
http_proxy = "http://118.107.44.181:8000"
proxies = {"http": http_proxy}


def get_AllCount():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    r = requests.get("https://crypto.com/price")
    soup = BeautifulSoup(r.text, "lxml")
    MoneyCounts = soup.find_all("tr", class_="css-1cxc880")
    file = open("CoinData.txt", "w+")
    for item in MoneyCounts:
        MoneyCost = item.find("div", class_="css-b1ilzc").text
        MoneyName = item.find("div", class_="css-ttxvk0").find("p").text
        MoneyDifference = item.find("td", class_="css-1b7j986").text
        with open("CoinData.txt", "a") as file:
            file.write(f"<b>{MoneyName}</b>: <u>{MoneyCost}$</u>  {MoneyDifference}\n")



def main():
    get_AllCount()


if __name__ == "__main__":
    main()
