# #!/usr/bin/env python
# # src/research_crew/main.py
# import os
# from research_crew.crew import ResearchCrew

# # Create output directory if it doesn't exist
# os.makedirs('output', exist_ok=True)

# def run():
#     """
#     Run the research crew.
#     """
#     inputs = {
#         'topic': 'Artificial Intelligence in Healthcare'
#     }

#     # Create and run the crew
#     result = ResearchCrew().crew().kickoff(inputs=inputs)

#     # Print the result
#     print("\n\n=== FINAL REPORT ===\n\n")
#     print(result.raw)

#     print("\n\nReport has been saved to output/report.md")

# if __name__ == "__main__":
#     run()

import os
from learning_crew.crew import LearningCrew

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def get_user_inputs():
    """Collect user learning preferences and background"""
    print("\n=== Personalized Learning System ===\n")
    
    # 1. What they want to learn
    learning_goal = input("What do you want to learn? (Be specific): ")
    
    # 2. Current knowledge level
    print("\nHow much do you already know about this topic?")
    print("1. Complete beginner")
    print("2. Some basic knowledge")
    print("3. Intermediate understanding")
    print("4. Advanced but want to deepen knowledge")
    current_level = input("Enter your choice (1-4): ")
    
    # 3. Target level
    print("\nWhat level do you want to reach?")
    print("1. Basic understanding")
    print("2. Intermediate proficiency")
    print("3. Advanced expertise")
    print("4. Expert level")
    target_level = input("Enter your choice (1-4): ")
    
    # 4. Application context
    application = input("Where are you planning to use this knowledge? (e.g., work, personal projects, academic): ")
    
    return {
        'learning_goal': learning_goal,
        'current_level': current_level,
        'target_level': target_level,
        'application_context': application
    }

def run():
    """Run the personalized learning crew"""
    
    # Get user inputs
    user_inputs = get_user_inputs()
    
    print(f"\n🎯 Creating personalized learning plan for: {user_inputs['learning_goal']}")
    print("⏳ This may take a few minutes...\n")
    
    # Create and run the learning crew
    result = LearningCrew().crew().kickoff(inputs=user_inputs)
    
    # Display results
    print("\n\n=== YOUR PERSONALIZED LEARNING PLAN ===\n")
    print(result.raw)
    
    print("\n📚 Your learning materials have been saved to the output/ directory")
    print("📋 Study plan: output/study_plan.md")
    print("📖 Learning content: output/learning_content.md")

if __name__ == "__main__":
    run()
