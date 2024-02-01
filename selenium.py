from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import re

# Function to remove emojis from text
def remove_emojis(text):
    # Remove emojis using regex
    emoji_pattern = re.compile("["
                               u"\U0001F000-\U0001F9FF"  
                               u"\U0001F300-\U0001F5FF"  
                               u"\U0001F600-\U0001F64F"  
                               u"\U0001F680-\U0001F6FF"  
                               u"\U0001F700-\U0001F77F"  
                               u"\U0001F780-\U0001F7FF"  
                               u"\U0001F800-\U0001F8FF"  
                               u"\U0001F900-\U0001F9FF"  
                               u"\U0001FA00-\U0001FA6F"  
                               u"\U0001FA70-\U0001FAFF"  
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text).replace('...', '').replace('"','').replace('..','').replace(',','').replace('\n','')

# Set up Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

# Define the base URL and the number of pages 
base_url = 'https://www.flipkart.com/redmi-note-13-pro-5g-fusion-purple-256-gb/product-reviews/itma6ec22746b464'
num_pages = 12  # Change this to the number of pages want to scrape

all_reviews = []
# Loop over the range of pages
for i in range(1, num_pages + 1):
    # Construct the URL for each page
    url = f"{base_url}?page={i}"
    driver.get(url)

    # Wait for the page to load
    time.sleep(2)

    # Extract reviews from the current page
    title_elements = driver.find_elements(By.CSS_SELECTOR, 'div.t-ZTKy')
    reviews = [title_element.text for title_element in title_elements]
    all_reviews.extend(reviews)

    try:
        click_next = driver.find_element(By.CSS_SELECTOR, 'a._1LKTO3')
        click_next.click()
        time.sleep(2)
    except NoSuchElementException:
        break

# Clean the reviews: Remove empty strings and emojis
reviews_cleaned = [remove_emojis(review) for review in all_reviews if review.strip()]

# Create a DataFrame from the cleaned data
df = pd.DataFrame({'Reviews': reviews_cleaned})

# Save the cleaned data to a CSV file
df.to_csv('flipkart_reviews_cleaned_one.csv', index=False)

print("Cleaned data saved to 'flipkart_reviews_cleaned_one.csv'")
