#Wikipedia Article Scraper
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import quote

FILE_NAME = "wikipedia_data.json"

def get_wikipedia_page(topic):
    topic_encoded = quote(topic.replace(" ", "_"))
    url = f"https://tr.wikipedia.org/wiki/{topic_encoded}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Sayfa alınamadı: {url} | Status code: {response.status_code}")
        return None

def get_article_title(soup):
    return soup.find("h1").text

def get_article_summary(soup):
    paragraphs = soup.find_all("p")

    for p in paragraphs:
        text = p.text.strip()
        if text:
            return text
    return "Özet bulunamadı."

def get_headings(soup):
    headings = []
    for tag in soup.find_all(["h2", "h3"]):
        headings.append(tag.text.strip())
    return headings[:5]

def get_related_links(soup):
    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/wiki/") and ":" not in href:
            links.add("https://tr.wikipedia.org" + href)

    return list(links)[:5]

def save_to_json(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    all_data = {}

    while True:
        topic = input("\nWikipedia konusu (çıkmak için q): ").strip()
        if topic.lower() == "q":
            break

        page = get_wikipedia_page(topic)
        if not page:
            continue

        soup = BeautifulSoup(page, "html.parser")

        title = get_article_title(soup)
        summary = get_article_summary(soup)
        headings = get_headings(soup)
        links = get_related_links(soup)

        all_data[topic] = {
            "title": title,
            "summary": summary,
            "headings": headings,
            "related_links": links
        }

        print("\nBAŞLIK:", title)
        print("\nÖZET:", summary)
        print("\nBAŞLIKLAR:")
        for h in headings:
            print("-", h)

        print("\nİLGİLİ LİNKLER:")
        for l in links:
            print(l)

    save_to_json(all_data)
    print("\nVeriler JSON dosyasına kaydedildi.")

main()