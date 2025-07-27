# crewai-alcohol-ranking-agent
Multi-agent CrewAI system for scraping and ranking top alcohol brands using GPT-4

#  CrewAI Agent: Alcohol Brand Scraper & Reviewer

This project uses CrewAI to run a two-agent workflow:
- **Scraper Agent**: finds alcohol brands from the web
- **Reviewer Agent**: ranks them based on online reviews using GPT-4

##  Objective

To explore multi-agent orchestration for automating a recommendation task — combining:
- Web scraping with BeautifulSoup
- LLM-based review summarization using OpenAI GPT-4
- Agent design and task delegation using CrewAI

##  Agents

- `scraper_agent`: "Web Researcher" — scrapes alcohol brand names
- `reviewer_agent`: "Alcohol Critic" — ranks brands based on sentiment in online reviews

##  Workflow

1. Scraper queries: [The Manual – Best Liquor Brands](https://www.themanual.com/food-and-drink/best-liquor-brands/)
2. Top 3 brands are passed to the Reviewer agent
3. Reviewer returns a ranked list with explanations

##  Technologies Used

- Python 3.11+
- [CrewAI](https://github.com/joaomdmoura/crewAI)
- `openai` for GPT-4
- `requests`, `BeautifulSoup` for web scraping
- `dotenv` for API key handling



## 🔐 Setup

1. Rename `.env.example` → `.env`  
2. Add your OpenAI API key:
```env
OPENAI_API_KEY=sk-...
