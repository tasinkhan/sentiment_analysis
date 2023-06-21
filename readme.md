Sentiment Analysis Project

This project is an implementation of sentiment analysis using natural language processing techniques. It provides a framework to analyze the sentiment of textual data, allowing you to classify whether a piece of text expresses a positive, negative, or neutral sentiment.

Installation
To use this project, follow these steps:

Clone the repository: git clone https://github.com/tasinkhan/sentiment_analysis.git
Navigate to the project directory: cd sentiment_analysis
Install the required dependencies: pip install -r requirements.txt

Usage
To run the project, follow these steps:

Run the server: python3 manage.py runserver 8000
Open web browser and enter http://127.0.0.1:8000/analyze/ as url
Provide the text to analyze in following format:
{
    "text":"sample text to analyze"
}
