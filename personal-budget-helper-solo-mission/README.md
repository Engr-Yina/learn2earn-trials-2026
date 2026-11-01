# Personal Budget Helper – Solo Mission

## Project Overview

The Personal Budget Helper is a beginner Python project developed as part of the Learn2Earn Trials 2026.

The project focuses on using Python functions to perform simple budget calculations and generate clear budget messages.

It demonstrates how to break a problem into smaller functions, test different scenarios, and improve code based on testing and feedback.

## Project Objectives

- Practise creating and using Python functions.
- Understand how function parameters and return statements work.
- Calculate the remaining balance from a given budget and expenses.
- Generate personalised budget messages.
- Test code using different inputs and compare expected results with actual results.

## Project Features

The project contains two main functions:

### 1. `budget_remaining()`

Calculates the amount of money remaining after deducting food and transport expenses from the total budget.

**Formula:**

`Remaining Budget = Total Budget - Food Expense - Transport Expense`

### 2. `budget_message()`

Generates a personalised message showing a person's remaining budget.

**Example output:**

`Ada has 500 naira remaining.`

## Project Structure

```text
personal-budget-helper-solo-mission/
│
├── first_solution.py
├── improved_solution.py
├── test_evidence.txt
├── reflection.txt
└── README.md
```

- **first_solution.py:** Contains the original code written during the task.
- **improved_solution.py:** Contains the improved version of the solution.
- **test_evidence.txt:** Documents test inputs, expected results, actual results, and test outcomes.
- **reflection.txt:** Contains personal reflections on the task and learning experience.
- **README.md:** Provides an overview and documentation of the project.

## Testing

The functions were tested using different scenarios to check whether they produced the expected results.

| Test Case | Description |
|---|---|
| Normal case | Calculates the remaining budget after expenses. |
| Zero expenses | Checks the result when no money is spent. |
| Overspending | Checks when expenses exceed the available budget. |
| Message test | Checks whether the correct name and balance appear in the message. |

The test evidence is documented in `test_evidence.txt`.

## Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

## How to Run the Project

1. Clone or download the repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run the Python solution:

```bash
python solution.py
```

## Key Lessons Learned

Through this project, I gained practical experience in:

- Writing reusable Python functions.
- Passing arguments into functions.
- Returning values instead of relying only on print statements.
- Using conditional thinking to understand different budget situations.
- Testing code with different inputs.
- Comparing expected and actual results.
- Improving code readability and organisation.

## Project Status

**Completed** – Developed as part of the Learn2Earn Trials 2026 Solo Mission.

---

**Author:** Vershima Matthew Yina  
**Learning Programme:** Learn2Earn Trials 2026  
**Project:** Personal Budget Helper
