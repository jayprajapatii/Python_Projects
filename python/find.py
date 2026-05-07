import requests
from bs4 import BeautifulSoup

# 🔹 List of web pages you want to check
urls = [
    "https://www.wikipedia.org/",
    "https://www.python.org/",
    "https://www.youtube.com/",
    "https://www.example.com/"
]

# 🔹 Website/domain you want to search for
target_site = "youtube.com"

print(f"Searching for '{target_site}' in pages...\n")

for url in urls:
    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()  # Raise error if page not accessible
        page_content = response.text

        if target_site in page_content:
            print(f"✅ Found '{target_site}' in {url}")
        else:
            print(f"❌ Not found in {url}")

    except Exception as e:
        print(f"⚠️ Error fetching {url}: {e}")
