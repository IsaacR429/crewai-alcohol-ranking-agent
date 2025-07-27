from crewai import Task
from agents import scraper_agent, reviewer_agent
import requests
from bs4 import BeautifulSoup

# Function to scrape alcohol brands
def get_alcohol_brands():
    url = "https://www.themanual.com/food-and-drink/best-liquor-brands/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    brands = []
    for link in soup.find_all("h2"):  # Adjust this selector as needed
        brands.append(link.text.strip())

    return brands[:3]  # Return three brands

# Task 1: Find Alcohol Brands
scraping_task = Task(
    description="Search online and find three random alcohol brands.",
    agent=scraper_agent,
    expected_output="A list of three alcohol brands."
)

# Task 2: Review the Brands
review_task = Task(
    description="Analyze online reviews and determine which alcohol brand is best.",
    agent=reviewer_agent,
    expected_output="A ranking of the best alcohol brands based on reviews."
)