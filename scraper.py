import requests
from bs4 import BeautifulSoup

payload = {
    'q': 'kiran mukhyala',
    'src': 'typed_query',
    'f': 'top',
}

response = requests.get('https://twitter.com/search', params=payload)

if response.status_code == 200:
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the specific HTML elements that contain individual tweet content.
        tweet_elements = soup.find_all('div', class_='css-901oao r-111h2gw r-1qd0xha r-n6v787 r-16dba41 r-1sf4r6n r-bcqeeo r-qvutc0')
        
        for tweet_element in tweet_elements:
            # Extract and print the text content of each tweet.
            tweet_text = tweet_element.find('span')
            if tweet_text:
                print(tweet_text.get_text())
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
else:
    print(f"API request failed with status code {response.status_code}.")
