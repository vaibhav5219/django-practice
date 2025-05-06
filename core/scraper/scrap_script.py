import requests
from bs4 import BeautifulSoup
from .models import News
import os
import uuid
from .tasks import download_image

# def download_image(image_url, save_directory, image_name):
#     if not os.path.exists(save_directory):
#         os.makedirs(save_directory)
#     image_path = os.path.join(save_directory, image_name)
#     response = requests.get(image_url, stream=True)
#     if response.status_code == 200:
#         with open(image_name, 'wb') as file:
#             for chunk in response.iter_content(1024):
#                 file.write(chunk)
#     return image_path


def scrape_imdb_news():
    url = "https://www.imdb.com/news/movie/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = soup.find_all('div', class_='ipc-list-card--border-line')
    
    for idx, item in enumerate(news_items):
        if idx > 10:
            break
        
        title = item.find('a', class_="ipc-link ipc-link--base sc-781c1bad-2 jZxGAW")
        description = item.find('div', class_= "ipc-html-content-inner-div")
        image = item.find('img', class_="ipc-image")

        external_link = title['href']
        title = title.text.strip() if title else "No title"
        description = description.text.strip() if title else "No description"
        image = image['src']
        image_path = None

        if image:
            image_name = f"image_{uuid.uuid4()}.jpg"
            # image_path = download_image(image, 'downloads/', image_name)
            image_path = download_image.delay(image, 'downloads/', image_name) # type: ignore

        news = {
            "title" : title,
            "description" : description,
            "image" : image,
            "external_link" : external_link}
        
        News.objects.create(**news)
