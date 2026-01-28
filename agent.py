from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.models.lite_llm import LiteLlm
import os

model = LiteLlm(
    model="openrouter/nvidia/nemotron-nano-12b-v2-vl:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def site_list(domain:str) -> list:
    """
    Returns conference site URLs for a given conference type domain.
    domain should be one of:
    ['international_conferences', 'national_conferences', 'regional_conferences', 'ieee_conferences', 'academic_paper_publishing_conferences']
    """
    sites =  {
    "international_conferences": [
        "https://www.allconferencealert.net/",
        "https://conferenceindex.org/",
        "https://waset.org/conferences",
        "https://www.conferencealerts.com/",
        "https://www.researchbib.com/",
        "https://10times.com/",
        "https://eventsinamerica.com/",
        "https://www.sciencedz.net/",
    ],

    "national_conferences": [
        "https://www.indianconferencealerts.com/",   # India-specific example
        "https://www.conferencealerts.com/country/",
        "https://nationalconferences.org/",
        "https://www.eventbrite.com/d/india/conference/",
    ],

    "regional_conferences": [
        "https://conferenceindex.org/region/",
        "https://www.allconferencealert.net/region/",
        "https://10times.com/region/",
        "https://localconferences.com/",
    ],

    "ieee_conferences": [
        "https://conferences.ieee.org/",               # Official IEEE conference catalog
        "https://ieeexplore.ieee.org/xpl/conhome.jsp", # IEEE Xplore conference listings
        "https://edas.info/",                          # IEEE paper submission platform
        "https://www.ieee.org/conferences_events/index.html",
    ],

    "academic_paper_publishing_conferences": [
        "https://academicsera.com/",
        "https://researchfora.com/",
        "https://globalconferencehub.com/",
        "https://worldresearchlibrary.org/",
        "https://iferd.in/",
        "https://wrfer.org/",
        "https://theires.org/",
    ],

    "subject_specific_conferences": {
        "ai_ml_data_science": [
            "https://www.ai-conferences.org/",
            "https://machinelearningconferences.org/",
            "https://neurips.cc/",
            "https://icml.cc/",
            "https://aaai.org/conference/",
        ],
        "engineering": [
            "https://asme.org/events/conferences",
            "https://www.ieee.org/conferences_events/",
            "https://www.iasted.org/",
        ],
        "computer_science": [
            "https://dblp.org/db/conf/",
            "https://easychair.org/conferences/",
        ],
        "medical_biotech": [
            "https://www.labroots.com/virtual-events",
            "https://www.medicalconferences.com/",
            "https://www.biomeetings.com/",
        ],
    },
}
    return sites.get(domain,[])


root_agent = Agent(
    name="conference_agent",
    model=model,
    description="Conference agent",
    instruction="""
    your an intelligent , helpfull , respectfull responsing agent.
    you need to list the conference site lists  for conferences in given domain of paper the user want to publish,type of conference the user want to publish[international,national..etc].
    give a small summary about the conference sites.
    use the tool- site_list tool provided for you .
    """,
    tools=[site_list],
)