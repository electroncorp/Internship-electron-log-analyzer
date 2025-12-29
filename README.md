#  Electron Corp – Remote Internship Technical Tasks

Welcome to the **Electron Corp Remote Internship Technical Assessment**.

This repository contains a **series of progressive technical tasks (Task 1 → Task 10)** designed to evaluate your **Python skills, software engineering practices, testing approach, and system design thinking**.

You are expected to complete these tasks **independently**, following professional development standards.

---

##  Internship Context

-  Company: **Electron Corp**
-  Internship Type: **Remote Technical Internship**
-  Focus Areas:
  - Python programming
  - Clean architecture
  - Testing & validation
  - REST-like services
  - Log analysis & security thinking
-  Duration: Defined by HR / supervisor
-  Mode: **100% Remote**

---

##  Repository Structure (MANDATORY)

You **MUST** follow the folder structure below exactly.

	electron-internship-tasks/
	│
	├── README.md
	├── tasks.txt
	├── Electron_Corp_Python_Internship_Tasks_FULL.pdf
	│
	├── tasks/
	│ ├── task1.py
	│ ├── task2.py
	│ ├── task3.py
	│ ├── task4.py
	│ ├── task5.py
	│ ├── task6.py
	│ ├── task7.py
	│ ├── task8.py
	│ ├── task9.py
	│ └── task10/
	│ ├── init.py
	│ ├── main.py
	│ ├── parser.py
	│ ├── aggregator.py
	│ ├── api.py
	│ ├── models.py
	│ ├── settings.py
	│ └── tests/
	│ ├── test_parser.py
	│ ├── test_aggregator.py
	│ └── test_api.py
	│
	├── log_analyzer/
	│ ├── sample_logs/
	│ │ ├── access.log
	│ │ └── error.log
	│ ├── reports/
	│ ├── screenshots/
	│ └── architecture_diagram.png


**Do not change folder names. Do not merge tasks.**

---

##  Tasks Overview

- **Tasks 1 → 9**:  
  Focus on Python fundamentals, data processing, validation, error handling, performance, and testing.

- **Task 10**:  
  A **mini-project** named **REST-like Log Analyzer**, simulating a real-world backend/security use case.

 Full task descriptions, requirements, and test cases are available in:
- `tasks.txt`
- `Electron_Corp_Python_Internship_Tasks_FULL.pdf`

---

##  Task 10 – Log Analyzer (Important)

Task 10 is a **core evaluation task**.

### You are expected to:
- Parse structured log files
- Aggregate metrics (status codes, IPs, response time, etc.)
- Expose REST-like endpoints (CLI or HTTP)
- Implement filtering & reporting
- Add **unit + integration tests**
- Follow clean architecture principles


---

##  Task Implementation Format (MANDATORY)
For **Tasks 1 → 9**, you are required to implement each task **as a Python function** following the format below.

###  Required Function Structure
Each task **must**:
- Be implemented as a function
- Receive inputs as **function arguments**
- Contain clear logic (no hardcoded values)
- Return a result (do NOT print inside the function)
- Be callable for testing

###  Function Template

```python
def task_name(input1, input2, ...):
    """
    Task description:
    - Explain what the function does
    - Describe inputs and outputs
    """
    # Step 1: input validation
    # Step 2: core logic
    # Step 3: return result
    return result

```

###  Example Task: Count HTTP Status Codes

Create a function that receives a list of HTTP status codes and returns a dictionary
containing the number of occurrences of each status code.

```python
def count_http_status_codes(status_codes):
    """
    Count occurrences of HTTP status codes.

    Args:
        status_codes (list): List of integer HTTP status codes

    Returns:
        dict: Dictionary with status codes as keys and counts as values
    """

    if not isinstance(status_codes, list):
        raise ValueError("Input must be a list")

    result = {}

    for code in status_codes:
        if not isinstance(code, int):
            raise ValueError("Status codes must be integers")

        if code in result:
            result[code] += 1
        else:
            result[code] = 1

    return result


```

###  Example Usage

```python
codes = [200, 404, 200, 500, 404, 200]
output = count_http_status_codes(codes)
print(output)

```

###  Expected Output

```python
{
    200: 3,
    404: 2,
    500: 1
}

```


##  Testing Requirements (MANDATORY)

Every task must include:
- Input validation
- Edge cases
- Error scenarios
- At least **5–10 test cases per task**

Task 10 must include:
- Unit tests
- Invalid data tests
- Performance-related tests (basic)


---

##  Documentation (MANDATORY)

Inside `necessary_documents_for_this_tasks/` you must provide:

| File | Description |
|----|----|
| `design_notes.md` | Architecture & design decisions |
| `assumptions.md` | Assumptions you made |
| `test_cases.md` | Test cases summary |
| `final_report.md` | What you built, challenges, improvements |



---

##  What We Evaluate

We will evaluate you on:

- Code clarity & readability
- Folder structure compliance
- Problem-solving approach
- Test quality
- Documentation quality
- Ability to follow instructions
- Engineering mindset (not just code)

---


##  Submission Instructions

1. Push your work to a **public GitHub repository**
2. Ensure all tasks are committed
3. Share the repository link with your supervisor

---


##  Final Note

This internship task simulates **real-world engineering expectations**.  
We are more interested in **how you think and structure your solution** than perfect output.

Good luck — and happy coding
**Electron Corp – Engineering Team**