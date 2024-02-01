<h1 align="center">Sentiment-Analysis-of-Product-Reviews</h1>

The project's goal is sentiment analysis on the product reviews of the 'Redmi Note 13 Pro 5G Fusion Purple 256 GB' using Hugging Face's Transformers library and visualize the sentiment distribution through a pie chart

<table style="width: 100%;">
    <tr>
        <td style="width: 50%; text-align: left;">
            <img width="500" src="https://github.com/Quantabhi/Sentiment-Analysis-of-Product-Reviews/assets/117148458/e65debc1-93ef-463b-bb7d-b99af0313283"" alt="Image 1">
        </td>
        <td style="width: 50%; text-align: right;">
            <img width="400" src="https://github.com/Quantabhi/Sentiment-Analysis-of-Product-Reviews/assets/117148458/9c81a0a8-cd3e-4577-9392-55484eeb477a" alt="Image 2">
        </td>
    </tr>
</table>

<h1 align="center"> Getting Started </h1>

<h2>Library Use</h2>
    <ul>
        <li><code>pip install pandas</code></li>
        <li><code>pip install transformers</code></li>
        <li><code>pip install matplotlib</code></li>
        <li><code>pip install selenium</code></li>
    </ul>


  <h2>1. Web Scraping:</h2>
    <p>Use Selenium (<code>selenium.py</code>) to scrape reviews from multiple pages and Set up a Chrome WebDriver and loop through the pages, extracting reviews and handling pagination.</p>

  <h2>2. Clean Data:</h2>
    <p>Define a function (<code>remove_emojis</code>) to remove emojis from text. Clean the scraped reviews by removing empty strings, emojis, and other unnecessary characters.</p>
  <h2>3. Save Cleaned Data:</h2>
    <p>Save the cleaned review data to a CSV file (<code>flipkart_reviews_cleaned_one.csv</code>).</p>
    
   <h2>4. Sentiment Analysis:</h2>
    <p>Create a (<code>sentiment_analysis.py</code>) sentiment analysis pipeline using Hugging Face's Transformers library. Iterate through each cleaned review, perform sentiment analysis, and assign sentiment scores. Count the number of positive, negative, and neutral sentiment scores.</p>
    
  <h2>5. Visualization:</h2>
    <p>Generate a pie chart to visualize the distribution of sentiment in the reviews.</p>


