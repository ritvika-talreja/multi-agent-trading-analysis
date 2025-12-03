from crewai import Task

def create_tasks(agents):
    fetch_market_task = Task(
        description="Fetch and analyze latest market data for selected stock.",
        agent=agents["data_analyst"],
        expected_output="A summary of current stock conditions and insights."
    )

    strategy_task = Task(
        description="Develop a trading strategy based on the analysis.",
        agent=agents["strategy"],
        expected_output="A concise trading strategy with entry and exit points."
    )

    execution_task = Task(
        description="Recommend best execution approach for the strategy.",
        agent=agents["execution"],
        expected_output="Execution advice including timing, order type, etc."
    )

    risk_task = Task(
        description="Assess risk related to the proposed strategy.",
        agent=agents["risk"],
        expected_output="Risk assessment with mitigation steps."
    )

    return [fetch_market_task, strategy_task, execution_task, risk_task]
