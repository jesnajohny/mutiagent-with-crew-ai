# # src/research_crew/crew.py
# from crewai import Agent, Crew, Process, Task
# from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import SerperDevTool
# from crewai.agents.agent_builder.base_agent import BaseAgent
# from typing import List

# @CrewBase
# class ResearchCrew():
#     """Research crew for comprehensive topic analysis and reporting"""

#     agents: List[BaseAgent]
#     tasks: List[Task]

#     @agent
#     def researcher(self) -> Agent:
#         return Agent(
#             config=self.agents_config['researcher'], # type: ignore[index]
#             verbose=True,
#             tools=[SerperDevTool()]
#         )

#     @agent
#     def analyst(self) -> Agent:
#         return Agent(
#             config=self.agents_config['analyst'], # type: ignore[index]
#             verbose=True
#         )

#     @task
#     def research_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['research_task'] # type: ignore[index]
#         )

#     @task
#     def analysis_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['analysis_task'], # type: ignore[index]
#             output_file='output/report.md'
#         )

#     @crew
#     def crew(self) -> Crew:
#         """Creates the research crew"""
#         return Crew(
#             agents=self.agents,
#             tasks=self.tasks,
#             process=Process.sequential,
#             verbose=True,
#         )

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool

@CrewBase
class LearningCrew():
    """Learning crew for personalized education"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self) -> None:
        # Initialize tools
        self.file_writer = FileWriterTool()
    
    @agent
    def skill_identifier(self) -> Agent:
        return Agent(
            config=self.agents_config['skill_identifier'],
            verbose=True,
            allow_delegation=False
        )
    
    @agent  
    def learner_profiler(self) -> Agent:
        return Agent(
            config=self.agents_config['learner_profiler'],
            verbose=True,
            allow_delegation=False
        )
    
    @agent
    def path_scheduler(self) -> Agent:
        return Agent(
            config=self.agents_config['path_scheduler'],
            verbose=True,
            allow_delegation=False
        )
    
    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator'],
            verbose=True,
            allow_delegation=False,
            tools=[self.file_writer]
        )
    
    @task
    def identify_skill_gaps(self) -> Task:
        return Task(
            config=self.tasks_config['identify_skill_gaps']
        )
    
    @task
    def create_learner_profile(self) -> Task:
        return Task(
            config=self.tasks_config['create_learner_profile']
        )
    
    @task
    def design_learning_path(self) -> Task:
        return Task(
            config=self.tasks_config['design_learning_path']
        )
    
    @task
    def generate_learning_content(self) -> Task:
        return Task(
            config=self.tasks_config['generate_learning_content'],
            output_file='output/learning_content.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the learning crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
