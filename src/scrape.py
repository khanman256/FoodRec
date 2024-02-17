from bs4 import BeautifulSoup
import requests
import datetime
import os

# gets the today's current schedule
def getToday():
    t = datetime.datetime.now()
    today = t.strftime("%A")
    return today
    
def download_pdf(url, save_path):
    file_name = os.path.basename(url)
    pdf_path = os.path.join(save_path, file_name)
    
    response =  requests.get(url)
    with open("menu.pdf", "wb") as f:
        f.write(response.content)

    return pdf_path

if __name__ == '__main__':
    # add your user agent based on your device
    # can do this by searching it up
    HEADERS = {"User-Agent": "", "Accept-Language": "en-US, en;q=0.5"}

    URL = "https://binghamton.sodexomyway.com/dining-near-me/c4-dining-hall"

    webpage = requests.get(URL, headers=HEADERS, timeout=10)

    soup = BeautifulSoup(webpage.content, "html.parser")

    today = getToday()

    links = soup.find_all('a', title=True)

    for link in links:
        title = link['title']
        if today.lower() in title.lower():
            pdf_url = link['href']
            save_directory = "src"
            download_pdf(pdf_url, save_directory)
        