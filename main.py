from agents import scraper_agent, reviewer_agent  # Ensure this line is at the top
from crewai import Crew
from task import scraping_task, review_task  # Import tasks from task.py

# Create a Crew with the defined agents and tasks
crew = Crew(
    agents=[scraper_agent, reviewer_agent],
    tasks=[scraping_task, review_task]
)

# Run the crew (this executes the tasks)
print("🚀 Running CrewAI Agents...")
result = crew.kickoff()
print("✅ Crew execution completed!")
print(result)
