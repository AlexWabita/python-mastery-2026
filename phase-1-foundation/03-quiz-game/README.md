# Quiz Game with Score Tracking

An interactive command-line trivia game featuring random question selection, multiple categories, score tracking, and persistent high score leaderboard.

## Project Overview

This is my third project in my Python mastery journey, completing Phase 1: Foundation Through Action. It combines concepts from Projects 1.1 and 1.2 while introducing randomization, nested data structures, and game development patterns.

## Features

### Core Gameplay
- **Multiple Categories**: Python, General Knowledge, Technology, Math, Geography
- **Random Question Selection**: No duplicate questions in a single session
- **Multiple Game Modes**: Play 5, 10, or all available questions
- **Multiple Choice Format**: A, B, C, D answer options
- **Immediate Feedback**: Know if you're right or wrong instantly
- **Score Tracking**: See your performance after each game

### Persistent Features
- **High Score Leaderboard**: Top 10 scores saved across sessions
- **Player Names**: Track who achieved each score
- **Percentage Calculation**: Accuracy displayed alongside raw scores
- **Timestamp Recording**: When each score was achieved
- **JSON Storage**: Data persists between program runs

### User Experience
- **Clear Screen Between Questions**: Clean, focused interface
- **Progress Indicators**: "Question 3 of 5" tracking
- **Category Display**: Know what topic each question covers
- **Input Validation**: Handles invalid answers gracefully
- **Interactive Menu**: Easy navigation between game modes

## What I Learned

### New Python Concepts
- **random Module**: 
  - `random.sample()` for selecting multiple unique items
  - Difference between `sample()` (no duplicates) and `choice()` (can repeat)
- **Nested Data Structures**: Lists containing dictionaries
- **Lambda Functions**: `lambda x: x['percentage']` for sorting
- **enumerate() with Start Parameter**: `enumerate(items, 1)` to start counting from 1
- **List Slicing**: `sorted_scores[:10]` to get top 10
- **Key Parameter in sorted()**: Sorting by custom criteria

### Reinforced Concepts
- **File I/O**: Loading and saving JSON data
- **Global Variables**: When to use `global` (reassignment vs modification)
- **Error Handling**: FileNotFoundError for missing data files
- **Functions**: Breaking complex logic into manageable pieces
- **Dictionaries**: Accessing nested data with keys
- **String Formatting**: f-strings with alignment (`:<15`)
- **User Input Validation**: While loops until valid input received

### Key Insights
- **Data Structure Design**: How to organize complex data (questions with multiple fields)
- **Game Loop Patterns**: Menu → Action → Return to Menu flow
- **Randomization**: Making games replayable with different experiences
- **Score Systems**: Tracking, calculating, and displaying performance metrics
- **User Flow**: Guiding users through multi-step processes smoothly

## How to Use

### Requirements
- Python 3.11.9 or higher
- No external dependencies (uses Python standard library only)

### Running the Game
```bash
# Navigate to the project directory
cd phase-1-foundation/03-quiz-game

# Run the program
python quiz_game.py
```

### Main Menu Options

1. **Play Quiz (5 questions)**: Quick game with 5 random questions
2. **Play Quiz (10 questions)**: Standard game with 10 random questions
3. **Play Full Quiz (all questions)**: Challenge yourself with all available questions
4. **View High Scores**: See the leaderboard of top 10 performances
5. **Exit**: Save and close the game

### Gameplay Flow

1. Select game mode from menu
2. Enter your name
3. Answer each question by typing A, B, C, or D
4. Get immediate feedback on each answer
5. View your final score and percentage
6. Score automatically saved to leaderboard
7. Return to menu to play again or view high scores

## Example Session
```
==================================================
           🎮 QUIZ GAME - MAIN MENU 🎮
==================================================

1. Play Quiz (5 questions)
2. Play Quiz (10 questions)
3. Play Full Quiz (all questions)
4. View High Scores
5. Exit

Choose an option (1-5): 1

============================================================
           🎮 WELCOME TO THE QUIZ GAME! 🎮
============================================================

Enter your name: Alex

============================================================
Question 1/5 - Category: Python
============================================================

What keyword is used to create a function in Python?

  A) function
  B) def
  C) func
  D) define

Your answer (A/B/C/D): B
✅ Correct!

Press Enter to continue...

============================================================
                   🏆 QUIZ COMPLETE! 🏆
============================================================

Player: Alex
Score: 4/5
Percentage: 80.0%
============================================================
```

## Project Structure
```
03-quiz-game/
├── quiz_game.py         # Main game code
├── README.md           # Project documentation (this file)
├── requirements.txt    # Dependencies (empty - uses stdlib)
├── .gitignore         # Git ignore rules
└── data/
    └── high_scores.json  # High score storage (created automatically)
```

## Technical Implementation

### Question Bank Structure

Each question is stored as a dictionary with:
- `category`: Topic area (Python, Math, etc.)
- `question`: The question text
- `answers`: List of 4 options (A, B, C, D format)
- `correct`: The correct answer letter
```python
{
    "category": "Python",
    "question": "What keyword is used to create a function?",
    "answers": ["A) function", "B) def", "C) func", "D) define"],
    "correct": "B"
}
```

### Function Breakdown

- `clear_screen()`: Cross-platform screen clearing
- `load_high_scores()`: Load leaderboard from JSON (uses `global`)
- `save_high_scores()`: Persist leaderboard to JSON
- `add_high_score()`: Add new entry with calculated percentage
- `display_question()`: Show formatted question with options
- `get_player_answer()`: Validate and return user input
- `play_quiz()`: Main game loop - select questions, track score
- `display_high_scores()`: Show sorted top 10 leaderboard
- `main()`: Program menu and navigation

### High Score Sorting

Uses `sorted()` with lambda function to sort by:
1. Percentage (primary - higher is better)
2. Raw score (tiebreaker)
3. Both in descending order (`reverse=True`)
```python
sorted_scores = sorted(high_scores, key=lambda x: (x['percentage'], x['score']), reverse=True)
```

## Challenges Faced & Solutions

1. **Preventing Duplicate Questions**: Using `random.choice()` in loop could repeat questions
   - **Solution**: Used `random.sample()` which guarantees unique selection

2. **Question Numbering**: enumerate() starts at 0, but wanted "Question 1 of 5"
   - **Solution**: Learned `enumerate(items, 1)` to start counting from 1

3. **Sorting High Scores**: Needed to sort by percentage, not just raw score
   - **Solution**: Used lambda function with tuple for multi-criteria sorting

4. **Input Validation**: Players could enter invalid answers
   - **Solution**: While loop that repeats until valid A/B/C/D received

## Future Enhancements

- **Question Categories Filter**: Let players choose category before playing
- **Difficulty Levels**: Easy/Medium/Hard questions with different point values
- **Timed Mode**: Add countdown timer for each question
- **Hints System**: Allow players to use hints (50/50, skip, etc.)
- **Question Editor**: Add/edit/delete questions without editing code
- **Multiplayer Mode**: Two-player turn-based competition
- **Statistics Dashboard**: Track accuracy per category, streaks, etc.
- **Import Questions**: Load questions from external files or APIs

## What I've Mastered in Phase 1

Completing this project means I now understand:

✅ **Data Structures**: Lists, dictionaries, sets, nested structures  
✅ **Control Flow**: if/elif/else, while loops, for loops  
✅ **Functions**: Definition, parameters, return values, docstrings  
✅ **File I/O**: Reading, writing, JSON serialization  
✅ **Modules**: datetime, json, os, random  
✅ **Error Handling**: try/except blocks  
✅ **String Methods**: Manipulation and validation  
✅ **Global Variables**: When and how to use them  
✅ **User Input**: Validation and handling  
✅ **Code Organization**: Breaking problems into functions  

## Completion Status

✅ **COMPLETED** - January 2026

**Phase 1: Foundation Through Action - COMPLETE!**

This project successfully demonstrates mastery of Python fundamentals through practical application. Ready to advance to Phase 2: Structured Programming.

---

**Part of**: [Python Mastery 2026](https://github.com/AlexWabita/python-mastery-2026)  
**Phase**: 1 - Foundation Through Action (Final Project)  
**Developer**: [Alex Wabita](https://github.com/AlexWabita)  
**Next**: Phase 2 - Structured Programming