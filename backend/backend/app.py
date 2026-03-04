"""
AOVOX Core Application Entry Point
"""

from orchestrator import Orchestrator

def main():
    print("AOVOX Core Engine Initialized")

    user_input = input("Enter your request: ")

    orchestrator = Orchestrator()
    response = orchestrator.process(user_input)

    print("\nAOVOX Response:")
    print(response)


if __name__ == "__main__":
    main()
