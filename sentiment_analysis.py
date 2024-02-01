# Import necessary libraries
import pandas as pd  # Pandas for data manipulation
from transformers import pipeline  # Hugging Face Transformers library for sentiment analysis
import matplotlib.pyplot as plt  # Matplotlib for data visualization

# Load the CSV file into a DataFrame
df = pd.read_csv('/content/flipkart_reviews_cleaned_one.csv')

# Create a sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Perform sentiment analysis and calculate sentiment scores
sentiment_scores = []

# Iterate through each review in the DataFrame
for review in df['Reviews']:
    # Perform sentiment analysis on each review using the pipeline
    analysis = sentiment_pipeline(review)[0]
    
    # We will consider 'positive' sentiment if the 'label' is 'POSITIVE' and 'negative' otherwise
    if analysis['label'] == 'POSITIVE':
        sentiment_scores.append(1)  # positive sentiment
    else:
        sentiment_scores.append(-1)  # negative sentiment

# Count positive, negative, and neutral sentiment scores
positive_count = sum(1 for score in sentiment_scores if score > 0)
negative_count = sum(1 for score in sentiment_scores if score < 0)
neutral_count = len(sentiment_scores) - positive_count - negative_count

# Create labels and sizes for the pie chart
labels = ['Positive', 'Negative', 'Neutral']
sizes = [positive_count, negative_count, neutral_count]
colors = ['lightgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0)  # explode the 1st slice (positive sentiment)

# Plot the pie chart with explode, shading, and rotation
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode, shadow=True)
plt.title('Sentiment Distribution of Reviews')
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
plt.show()  # Display the pie chart
