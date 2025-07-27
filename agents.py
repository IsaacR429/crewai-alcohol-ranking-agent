import os
from pathlib import Path
from crewai import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# ✅ Explicitly set the .env path
env_path = Path(__file__).parent / ".env"
dotenv_loaded = load_dotenv(dotenv_path=env_path)

# ✅ Debug: Print if `.env` file is loaded
print(f"✅ dotenv loaded: {dotenv_loaded}")

# ✅ Debug: Check if API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("⚠️ OPENAI_API_KEY is missing! Check if it's set in the .env file or as an environment variable.")
else:
    print(f"✅ OPENAI_API_KEY found: {api_key[:5]}*****")  # Masked for security

# Initialize OpenAI model
openai_model = ChatOpenAI(model="gpt-4", temperature=0.7, api_key=api_key)

# Define Scraper Agent
scraper_agent = Agent(
    role="Web Researcher",
    goal="Find three random alcohol brands from the internet",
    backstory="An expert in internet research, capable of finding alcohol brands quickly.",
    llm=openai_model
)

# Define Reviewer Agent
reviewer_agent = Agent(
    role="Alcohol Critic",
    goal="Evaluate the best alcohol brand based on online reviews",
    backstory="A professional alcohol reviewer who analyzes online reviews to determine quality.",
    llm=openai_model
)


