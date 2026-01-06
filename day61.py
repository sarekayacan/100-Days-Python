#Social Media Scraper
from bs4 import BeautifulSoup
import csv

#HTML dosyasını oku
def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

#Anahtar kelimeleri vurgula
def highlight_keywords(text, keywords):
    for keyword in keywords:
        text = text.replace(keyword, keyword.upper())
    return text

#Postları HTML'den çıkar
def extract_posts(soup, keywords):
    posts = []

    post_elements = soup.find_all("div", class_="post")

    for post in post_elements:
        post_id = post.get("id")
        likes = post.get("data-likes")

        username = post.find("h2", class_="username").text.strip()
        content = post.find("p", class_="content").text.strip()
        timestamp = post.find("span", class_="timestamp").text.strip()

        content = highlight_keywords(content, keywords)

        posts.append({
            "post_id": post_id,
            "username": username,
            "content": content,
            "timestamp": timestamp,
            "likes": likes
        })

    return posts

#CSV dosyasına kaydet
def save_posts_to_csv(posts, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["post_id", "username", "content", "timestamp", "likes"]
        )
        writer.writeheader()
        writer.writerows(posts)

#Ana program
def main():
    print("Sosyal Medya Scraper Başladı")

    html_content = load_html("social_media.html")
    soup = BeautifulSoup(html_content, "html.parser")

    keywords = ["Python", "Flask"]

    posts = extract_posts(soup, keywords)
    save_posts_to_csv(posts, "social_media_posts.csv")

    print("Postlar başarıyla CSV dosyasına kaydedildi.")

if __name__ == "__main__":
    main()
