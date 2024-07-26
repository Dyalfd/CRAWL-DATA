import requests
from bs4 import BeautifulSoup
import os

# Fungsi untuk mendapatkan halaman HTML dari URL
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Fungsi untuk mendapatkan berita dari halaman utama Detik News
def get_news_links():
    base_url = 'https://news.detik.com/'
    html = get_html(base_url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        # Mengambil link berita dari halaman utama
        news_links = []
        for a in soup.find_all('a', class_='media__link'):
            link = a['href']
            if link.startswith('https://news.detik.com'):
                news_links.append(link)
        return news_links
    else:
        return []

# Fungsi untuk mengunduh gambar dari URL
def download_image(image_url, file_path):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Image saved to {file_path}")
        else:
            print(f"Failed to download image from {image_url}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Fungsi untuk mendapatkan detail berita dari link berita
def get_news_details(url):
    html = get_html(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        # Mengambil judul berita
        title = soup.find('h1', class_='detail__title').text
        # Mengambil tanggal berita
        date = soup.find('div', class_='detail__date').text.strip()
        # Mengambil gambar berita
        image_tag = soup.find('div', class_='detail__media-image')
        image_url = image_tag.find('img')['src'] if image_tag and image_tag.find('img') else 'No image available'

        # Menyimpan gambar jika ada
        if image_url and image_url != 'No image available':
            image_name = image_url.split('/')[-1]
            file_path = os.path.join('images', image_name)
            download_image(image_url, file_path)

        return {
            'title': title,
            'date': date,
            'image_url': image_url,
            'news_url': url
        }
    else:
        return None

# Fungsi utama untuk melakukan crawling dan scraping berita
def main():
    news_links = get_news_links()
    if news_links:
        if not os.path.exists('images'):
            os.makedirs('images')
        for link in news_links[:10]:  # Batasi hanya 10 berita untuk contoh
            news_details = get_news_details(link)
            if news_details:
                print(f"Title: {news_details['title']}")
                print(f"Date: {news_details['date']}")
                print(f"News URL: {news_details['news_url']}")
                print(f"Image URL: {news_details['image_url']}")
                print("-" * 80)
    else:
        print("Gagal mendapatkan link berita.")

if __name__ == "__main__":
    main()
