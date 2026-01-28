# Conference-Finder-AI-Agent
🎓 Conference Finder AI Agent

This project implements an intelligent Conference Recommendation Agent using Google ADK and LiteLLM.
The agent helps users find suitable conference websites based on the type of conference and research domain they want to publish in.

🚀 Features

Lists conference websites based on publication needs

Supports multiple conference types:

International conferences

National conferences

Regional conferences

IEEE conferences

Academic paper publishing conferences

Uses a custom tool (site_list) to fetch curated conference URLs

Provides a short summary of the listed conference sites

Powered by OpenRouter Nemotron Nano 12B model

🧠 How It Works

A LiteLLM model is initialized using OpenRouter.

A custom function site_list(domain) acts as a tool that returns predefined conference URLs.

An AI Agent:

Understands the user’s publication domain

Calls the site_list tool

Lists relevant conference websites

Explains them briefly in simple language

📂 Code Overview
🔹 Model Initialization
model = LiteLlm(
    model="openrouter/nvidia/nemotron-nano-12b-v2-vl:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

🔹 Conference Site Tool
def site_list(domain: str) -> list:
    """
    Returns conference site URLs for a given conference domain.
    """
    return sites.get(domain, [])

🔹 Agent Definition
root_agent = Agent(
    name="conference_agent",
    model=model,
    description="Conference agent",
    instruction="""
    you are an intelligent, helpful, respectful agent.
    list conference sites based on the domain and conference type.
    give a short summary for each.
    """,
    tools=[site_list],
)

🛠 Supported Domains

international_conferences

national_conferences

regional_conferences

ieee_conferences

academic_paper_publishing_conferences

Subject-specific domains:

AI / ML / Data Science

Engineering

Computer Science

Medical / Biotechnology

▶️ Usage

Provide the conference domain or type the user wants to publish in

The agent:

Fetches relevant conference websites

Displays a categorized list

Gives a brief explanation for each site

📌 Example Use Cases

Students searching for conferences to publish papers

Researchers identifying IEEE or international conferences

Academic project or research-support systems

🔑 Requirements

Python 3.8+

Google ADK

LiteLLM

OpenRouter API key (set as environment variable)

export OPENROUTER_API_KEY="your_api_key_here"

📄 Notes

Conference links are curated, not scraped live.

Ensure your API key is valid before running the agent.

✨ Author

Created as a tool-enabled AI agent for academic and research conference discovery using Google ADK.
