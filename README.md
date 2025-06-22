[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Nm_KngMc)
# MSML606 Summer 2025 – Homework 2

## Overview

This assignment focuses on implementing fundamental data structures and evaluating expressions using stacks. You are expected to:

- Implement a custom stack class
- Validate parentheses using a stack
- Evaluate postfix expressions using a stack
- Submit both code and a report
- Descriptive question 
Question: Description of usefulness of postfix expressions, and the process to convert infix to postfix.

---

## 📝 Assignment Structure

1. **Implement in Python:**
   - A boilerplate `.py` template will be provided.
   - Write your solutions for:
     - Valid Parentheses Checker
     - Postfix Expression Evaluator

2. **Submit a Report (PDF/DOC):**
   - Describe your approach to both problems
   - Answer descriptive question 
   - Discuss time and space complexity (Big-O)

3. **Final Submission:**
   - Commit the code to github.
   - Zip your Python file and report into a single `.zip` archive
   - Upload the `.zip` file on ELMS/Canvas

---

## 📂 Project Structure (After Cloning)

```
├── homework2.py               # Python file where you write your code
├── test_cases_question1.csv   # Test cases for parentheses validation
├── test_cases_question2.csv   # Test cases for postfix evaluation
├── README.md                  # This file
```

---

## 💡 Problem Descriptions

### ✅ Problem 1: Valid Parentheses Using Stack

Given a string `s` containing only `(`, `)`, `{`, `}`, `[`, and `]`, determine if the input is a valid sequence.

Conditions for validity:
- Open brackets must be closed by the same type.
- Brackets must be closed in the correct order.
- Each closing bracket must correspond to an open one.

**Example Input:** `s = "()[]{}"`  
**Output:** `True`

---

### ➕ Problem 2: Postfix Calculator Using Stack

1. Understand infix vs. postfix expressions.
2. **Write-up**: Briefly explain:
   - Usefulness of postfix expressions
   - Process to convert infix to postfix
3. **Implement**: A postfix calculator that evaluates postfix strings using the stack from Problem 1.

**Input Example:** `"3 4 /"`  
**Output:** `1`

❗️ **Note:**  
- Do not use Python’s `eval()` function.
- Allowed operators: `+`, `-`, `*`, `/`
- All numbers are integers (positive or negative)

---

## 🧪 Testing

- GitHub Actions will automatically run test cases upon pushing your code.

---

## 📤 Submission Instructions

### 1. Clone the Assignment Repository

```bash
git clone <your-github-classroom-repo-url>
cd <your-repo>
```

### 2. Write Code and Report

- Edit `question1.py` and `question2.py` with your solutions

### 3. Add and Commit Your Changes

```bash
git add .
git commit -m "Completed HW2"
```

### 4. Push to GitHub

```bash
git push origin main
```

> Your tests will run automatically using GitHub Actions. Check the "Actions" tab on GitHub for results.

---

## 📊 Rubric (Total: 12 Marks)

| Criteria                            | Marks |
|-------------------------------------|-------|
| Stack Implementation                | 2     |
| Valid Parentheses Function          | 2     |
| Postfix Evaluation Function         | 2     |
| Code Readability & Edge Cases       | 3     |
| Description of Postfix Usefulness   | 1     |
| Report & Big-O Analysis             | 2     |

---

Good luck, and happy coding! 🧠💻
