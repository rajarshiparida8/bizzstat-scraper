from GoogleNews import GoogleNews
import json
from datetime import datetime

def get_news(query="sports", lang="en", period="7d"):
    googlenews = GoogleNews(lang=lang, period=period)
    googlenews.search(query)
    results = googlenews.result()

    # Add fetch timestamp (as string)
    for article in results:
        article["fetched_at"] = datetime.now()

    return results

if __name__ == "__main__":from GoogleNews import GoogleNews
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def fetch_image_url(article_url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}  # prevent blocking
        response = requests.get(article_url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        og_image = soup.find("meta", property="og:image")
        twitter_image = soup.find("meta", property="twitter:image")

        if og_image and og_image.get("content"):
            return og_image["content"]
        elif twitter_image and twitter_image.get("content"):
            return twitter_image["content"]
    except Exception as e:
        print(f"⚠️ Error fetching image from {article_url}: {e}")

    return "https://via.placeholder.com/150"  # fallback

def get_news(query="sports", lang="en", period="7d"):
    googlenews = GoogleNews(lang=lang, period=period)
    googlenews.search(query)
    results = googlenews.result()

    for article in results:
        article["fetched_at"] = datetime.now()
        article["img"] = fetch_image_url(article.get("link", ""))

    return results

if __name__ == "__main__":
    news_data = get_news()
    with open("news_output.json", "w", encoding="utf-8") as f:
        json.dump(news_data, f, ensure_ascii=False, indent=4, default=str)

    print("✅ News data saved to news_output.json!")

    news_data = get_news()
    with open("news_output.json", "w", encoding="utf-8") as f:
        json.dump(news_data, f, ensure_ascii=False, indent=4,default=str)
    print("✅ News data saved to news_output.json!")