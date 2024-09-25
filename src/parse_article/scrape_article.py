import requests
from bs4 import BeautifulSoup
import time
import json
import re

class FidelityNewsScraper:

    def __init__(self):
        # URL of the stock news website
        #self.URL = URL  # Replace with the target URL

        # Store previously seen articles (you can use a database or file for persistence)
        self.seen_articles = set()

# Function to scrape the website
    def check_news() -> list:
        try:
            # Send a request to the website
            #response = requests.get(URL)
            #response.raise_for_status()
            
            response = requests.get('https://www.fidelity.com/news/company-news')
            # Parse the website content with BeautifulSoup
            #soup = BeautifulSoup(response.text, 'html.parser')

            content = BeautifulSoup(response.text,'lxml')
            scripts = '\n'.join([script.text for script in content.find_all('script')])
            match_script = re.findall(r' var newsCatTableData .*',scripts)

            #match_script = soup.find_all('script',string=re.compile('newsCatTableData'))
            json_string = match_script[0][25:len(match_script[0])-1]
            json_list = json_string.split('},')
            dictionary_list = []
            for i in json_list[:-1]:
                val = i+'}'
                json_dict = json.loads(val)
                title = json_dict['title']

                article_dictionary[json_dict['title']] = json_dict['link']
                dictionary_list.append(json_dict)
            
            # Extract news titles or articles (this will depend on the website structure)
            # Example: If news titles are in <h2> tags
            #news_items = soup.find_all('h2', class_='news-title')  # Modify based on the site's HTML

            # Iterate through extracted news articles
            for json_dictionary in dictionary_list:
                title = item.get_text()

                # If the article title hasn't been seen before, it's new
                if title not in seen_articles:
                    print(f"New Article Found: {title}")
                    # Add the new article to the seen set
                    seen_articles.add(title)

                    # Optionally, notify the user via email, SMS, etc.
                    #notify_user(title)

        except Exception as e:
            print(f"Error occurred: {e}")

# Optional: Send a notification (email, SMS, etc.)
#def notify_user(new_article):
    # Example: Print for simplicity, but you could use email, SMS (Twilio), etc.
    # print(f"Notification: {new_article}")
    # You can integrate SMTP for email or Twilio for SMS notifications

    # Run the scraper periodically
    def run_monitor():
        while True:
            print("Checking for news updates...")
            check_news()
            time.sleep(600)  # Wait 10 minutes before checking again (adjust as needed)

if __name__ == "__main__":
    run_monitor()

