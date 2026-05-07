import requests
from bs4 import BeautifulSoup

def scrape_news_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text,'html.parser')
        
        headlines = []
        
        for tag in soup.find_all(['h1','h2','h3']):
            text = tag.get_text(strip=True)
            if text and len(text) > 10:
                headlines.append(text)
                
        if headlines:
            print("\n Top headlines found:\n")
            for i, headline in enumerate(headlines[:10],1):
                print(f"{i}.{headline}")
        else:
            print("no headlines found on the page. try another URL.")
            
    
    except requests.exceptions.MissingSchema:
        print("error: invalid url..")
    except requests.exceptions.ConnectionError:
        print("error: unable to connect to the website. check your internet")
    except Exception as e:
        print(f"an unexpected error occurred: {e}")
        
        
print("=== Simple Web Scraper ===")
url = input("enter a news website url === >")
scrape_news_headlines(url)
        