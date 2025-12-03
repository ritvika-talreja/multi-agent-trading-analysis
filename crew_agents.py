from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

def create_agents():
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()

    data_analyst_agent = Agent(
        role="Data Analyst",
        goal=(
            "Monitor and analyze market data in real-time to identify trends "
            "and predict market movements."
        ),
        backstory=(
            "Expert in financial markets, statistical modeling, and machine "
            "learning to generate real-time insights."
        ),
        verbose=True,
        allow_delegation=True,
        tools=[scrape_tool, search_tool]
    )

    trading_strategy_agent = Agent(
        role="Trading Strategy Developer",
        goal="Develop trading strategies based on insights and market trends.",
        backstory="Quantitative expert skilled in finance & modelling.",
        verbose=True,
        allow_delegation=True,
        tools=[scrape_tool, search_tool]
    )

    execution_agent = Agent(
        role="Trade Advisor",
        goal="Recommend optimal trade execution strategies.",
        backstory="Expert in execution timing, price action & liquidity.",
        verbose=True,
        allow_delegation=True,
        tools=[scrape_tool, search_tool]
    )

    risk_management_agent = Agent(
        role="Risk Advisor",
        goal="Evaluate and advise on risks in trading activities.",
        backstory="Risk modelling expert ensuring safety & compliance.",
        verbose=True,
        allow_delegation=True,
        tools=[scrape_tool, search_tool]
    )

    return {
        "data_analyst": data_analyst_agent,
        "strategy": trading_strategy_agent,
        "execution": execution_agent,
        "risk": risk_management_agent
    }
