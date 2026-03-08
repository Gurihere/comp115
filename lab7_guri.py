"""
Lab 7 - Strings and Tuples 
(100 marks in total)

Author:  Gurjot
Due Date: This Friday (Mar. 6) 5 pm.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (10 marks: function implementation: 5 marks, unit tests: 5 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""
def reverse_str(s):
    """
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'

    Parameters:
    - s (string): The string to be reversed

    Returns:
    - (string): A reversed version of string s.

    """
    result = ""
    for char in s:
        result = char + result
    return result


# Unit tests
assert reverse_str("Abd") == "dbA"
assert reverse_str("COMP115") == "511PMOC"
assert reverse_str("app") == "ppa"
assert reverse_str("") == ""
assert reverse_str("a") == "a"


"""
Exercise 2 (10 marks: function implementation: 5 marks, unit tests: 5 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2

    Parameters:
    - s (string): The string in which vowels are counted.

    Returns:
    - (int): The total number of vowels in the string s.

    """
    count = 0
    for char in s.lower():
        if char in "aeiou":
            count += 1
    return count


# Unit tests
assert count_vowels("Apple") == 2
assert count_vowels("Hmmm") == 0
assert count_vowels("hello") == 2
assert count_vowels("") == 0
assert count_vowels("AEIOU") == 5


"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: in
"""
def remove_duplicates(s):
    """
    Removes duplicate characters from string s, keeping only the first
    occurrence of each character (case-sensitive).

    E.g.,
    >>> remove_duplicates("apple")
    'aple'
    >>> remove_duplicates("Popsipple")
    'Popsile'

    Parameters:
    - s (string): The string from which duplicate characters are removed.

    Returns:
    - (string): A new string with each character appearing only once,
                in the order they first appear in s.
    """
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result


# Unit tests
assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile"
assert remove_duplicates("pear") == "pear"
assert remove_duplicates("") == ""
assert remove_duplicates("aaa") == "a"


"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
"""
def find_index(s, t):
    """
    Finds and returns the lowest index of character t in string s.
    Returns -1 if t is not found in s.

    E.g.,
    >>> find_index("Abd", 'b')
    1
    >>> find_index("Abd", 'w')
    -1

    Parameters:
    - s (string): The string to search within.
    - t (string): The character to search for.

    Returns:
    - (int): The lowest index of t in s, or -1 if t is not found.
    """
    for i in range(len(s)):
        if s[i] == t:
            return i
    return -1


# Unit tests
assert find_index("Abd", 'b') == 1
assert find_index("Abdccc", 'c') == 3
assert find_index("Abd", 'w') == -1
assert find_index("", 'a') == -1
assert find_index("hello", 'h') == 0


"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')


def project_completion_day(day, days_to_completion):
    """
    Returns the day of the week when a project will be completed, given the
    current day and the number of days until completion.

    E.g.,
    >>> project_completion_day('Monday', 4)
    'Friday'
    >>> project_completion_day('Saturday', 2)
    'Monday'

    Parameters:
    - day (string): The current day of the week (e.g., 'Monday').
    - days_to_completion (int): The number of days until the project is done.

    Returns:
    - (string): The name of the day when the project will be completed.
    """
    start_index = days_week.index(day)
    end_index = (start_index + days_to_completion) % 7
    return days_week[end_index]


# Unit tests
assert project_completion_day('Monday', 4) == 'Friday'
assert project_completion_day('Monday', 7) == 'Monday'
assert project_completion_day('Saturday', 2) == 'Monday'
assert project_completion_day('Saturday', 1) == 'Sunday'
assert project_completion_day('Friday', 3) == 'Monday'


"""Log Parsing Exercise (20 marks - function implementation 10, unit test 5, function usage 5)
"""

def parse_log_line(line):
    """
    Parses a single log line into its four components: timestamp, level,
    module, and message.

    E.g.,
    >>> parse_log_line('2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s')
    ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')

    Parameters:
    - line (string): A single log line in the format:
                     "YYYY-MM-DD HH:MM:SS [LEVEL] module.py Message"

    Returns:
    - (tuple): A 4-element tuple of (timestamp, level, module, message) where:
               - timestamp (str): Date and time as "YYYY-MM-DD HH:MM:SS"
               - level (str): Severity level e.g. "ERROR", "WARNING", "INFO"
               - module (str): The Python module filename e.g. "database.py"
               - message (str): The log message text
    """
    parts = line.split()
    timestamp = parts[0] + ' ' + parts[1]
    level = parts[2][1:-1]          # strip surrounding [ ]
    module = parts[3]
    message = ' '.join(parts[4:])
    return (timestamp, level, module, message)


# Unit tests
line1 = '2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s'
assert parse_log_line(line1) == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')

line2 = '2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)'
assert parse_log_line(line2) == ('2024-03-05 14:32:18', 'WARNING', 'api.py', 'Slow query detected (2.3s)')

line3 = '2024-03-05 14:32:22 [INFO] server.py Server started on port 8000'
assert parse_log_line(line3) == ('2024-03-05 14:32:22', 'INFO', 'server.py', 'Server started on port 8000')


# Parse all lines from the sample log string
log_string = """
2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect
"""

parsed_logs = []
for line in log_string.split('\n'):
    if line.strip() != '':          # skip empty lines
        parsed_logs.append(parse_log_line(line.strip()))

# Print results to verify
for entry in parsed_logs:
    print(entry)


"""
Congratulations on finishing your lab7. Hope you feel more confident 
on function implementation.

Now you just need to upload it to your GitHub repository, and paste the link on e-learn. That's all.
"""