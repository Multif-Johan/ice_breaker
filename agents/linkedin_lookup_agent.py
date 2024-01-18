from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

def lookup(name:str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin Profile page.
                    Your answer should only contain a URL"""
    #Tool: name = name of what the agent will do, func = function of agent, description what the llm reads to choose what to use
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page", 
            func="?",
            description="useful for when you need to get the Linkedin Page URL"
            )
        ]
    #Agent type different type of reasoning process 
    #verbose IMPORTANT: tells agent that we want to be aware of the reasoning every process
    agent = initialize_agent(tools=tools_for_agent,llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    prompt_template = PromptTemplate(template=template, input_variables={'name_of_person'})
    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    
    return linkedin_profile_url