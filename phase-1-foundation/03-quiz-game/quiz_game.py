import random
import json
from datetime import datetime
import os

# Question bank - list of dictionaries
QUESTIONS = [
    {
        "category": "Python",
        "question": "What keyword is used to create a function in Python?",
        "answers": ["A) function", "B) def", "C) func", "D) define"],
        "correct": "B"
    },
    {
        "category": "Python",
        "question": "Which data type is mutable in Python?",
        "answers": ["A) tuple", "B) string", "C) list", "D) integer"],
        "correct": "C"
    },
    {
        "category": "Python",
        "question": "What does the len() function do?",
        "answers": ["A) Returns the length", "B) Deletes items", "C) Sorts items", "D) Reverses items"],
        "correct": "A"
    },
    {
        "category": "General Knowledge",
        "question": "What is the capital of Kenya?",
        "answers": ["A) Mombasa", "B) Nairobi", "C) Kisumu", "D) Nakuru"],
        "correct": "B"
    },
    {
        "category": "General Knowledge",
        "question": "How many continents are there?",
        "answers": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "correct": "C"
    },
    {
        "category": "Technology",
        "question": "What does CPU stand for?",
        "answers": ["A) Central Process Unit", "B) Computer Personal Unit", "C) Central Processing Unit", "D) Central Processor Unit"],
        "correct": "C"
    },
    {
        "category": "Technology",
        "question": "What year was Python first released?",
        "answers": ["A) 1989", "B) 1991", "C) 1995", "D) 2000"],
        "correct": "B"
    },
    {
        "category": "Math",
        "question": "What is 15% of 200?",
        "answers": ["A) 20", "B) 25", "C) 30", "D) 35"],
        "correct": "C"
    },
    {
        "category": "Math",
        "question": "What is the square root of 144?",
        "answers": ["A) 10", "B) 11", "C) 12", "D) 13"],
        "correct": "C"
    },
    {
        "category": "Geography",
        "question": "Which is the largest ocean?",
        "answers": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "correct": "D"
    }
]

# Global variable for high scores
high_scores = []


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def load_high_scores():
    """Load high scores from JSON file."""
    global high_scores
    try:
        with open('data/high_scores.json', 'r') as file:
            high_scores = json.load(file)
    except FileNotFoundError:
        high_scores = []


def save_high_scores():
    """Save high scores to JSON file."""
    with open('data/high_scores.json', 'w') as file:
        json.dump(high_scores, file, indent=2)


def add_high_score(name, score, total_questions):
    """Add a new high score entry."""
    score_entry = {
        "name": name,
        "score": score,
        "total": total_questions,
        "percentage": round((score / total_questions) * 100, 1),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    high_scores.append(score_entry)
    save_high_scores()


def display_question(question_data, question_num, total):
    """Display a single question with its answers."""
    print(f"\n{'='*60}")
    print(f"Question {question_num}/{total} - Category: {question_data['category']}")
    print(f"{'='*60}")
    print(f"\n{question_data['question']}\n")
    
    for answer in question_data['answers']:
        print(f"  {answer}")
    print()


def get_player_answer():
    """Get and validate player's answer."""
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        else:
            print("❌ Invalid input! Please enter A, B, C, or D.")


def play_quiz(num_questions=5):
    """Main quiz game logic."""
    clear_screen()
    print("="*60)
    print("           🎮 WELCOME TO THE QUIZ GAME! 🎮")
    print("="*60)
    
    player_name = input("\nEnter your name: ").strip()
    if not player_name:
        player_name = "Anonymous"
    
    # Select random questions
    if num_questions > len(QUESTIONS):
        num_questions = len(QUESTIONS)
    
    selected_questions = random.sample(QUESTIONS, num_questions)
    
    score = 0
    
    # Ask each question
    for i, question_data in enumerate(selected_questions, 1):
        display_question(question_data, i, num_questions)
        player_answer = get_player_answer()
        
        if player_answer == question_data['correct']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {question_data['correct']}")
        
        input("\nPress Enter to continue...")
        clear_screen()
    
    # Display final results
    percentage = (score / num_questions) * 100
    print("="*60)
    print("                   🏆 QUIZ COMPLETE! 🏆")
    print("="*60)
    print(f"\nPlayer: {player_name}")
    print(f"Score: {score}/{num_questions}")
    print(f"Percentage: {percentage:.1f}%")
    print("="*60)
    
    # Save high score
    add_high_score(player_name, score, num_questions)
    
    return score, num_questions



def display_high_scores():
    """Display all high scores."""
    clear_screen()
    print("="*60)
    print("                   🏆 HIGH SCORES 🏆")
    print("="*60)
    
    if not high_scores:
        print("\nNo high scores yet! Be the first to play!\n")
        return
    
    # Sort by percentage, then by score
    sorted_scores = sorted(high_scores, key=lambda x: (x['percentage'], x['score']), reverse=True)
    
    print(f"\n{'Rank':<6}{'Name':<15}{'Score':<12}{'%':<8}{'Date':<20}")
    print("-"*60)
    
    for i, entry in enumerate(sorted_scores[:10], 1):  # Top 10
        print(f"{i:<6}{entry['name']:<15}{entry['score']}/{entry['total']:<9}{entry['percentage']:<8.1f}{entry['date']:<20}")
    
    print("="*60)


def main():
    """Main program loop."""
    load_high_scores()
    
    while True:
        clear_screen()
        print("="*60)
        print("           🎮 QUIZ GAME - MAIN MENU 🎮")
        print("="*60)
        print("\n1. Play Quiz (5 questions)")
        print("2. Play Quiz (10 questions)")
        print("3. Play Full Quiz (all questions)")
        print("4. View High Scores")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == '1':
            play_quiz(5)
            input("\nPress Enter to return to menu...")
        elif choice == '2':
            play_quiz(10)
            input("\nPress Enter to return to menu...")
        elif choice == '3':
            play_quiz(len(QUESTIONS))
            input("\nPress Enter to return to menu...")
        elif choice == '4':
            display_high_scores()
            input("\nPress Enter to return to menu...")
        elif choice == '5':
            print("\nThanks for playing! Goodbye! 👋")
            break
        else:
            print("\n❌ Invalid choice! Please choose 1-5.")
            input("\nPress Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()