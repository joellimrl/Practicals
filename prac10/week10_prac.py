"""
Todo:
1. from scratch (rows(n))

2. Wikipedia API (Create a new file cal
led wiki.py and write a small script that prompts the user for a page title or search phrase,
then prints the summary of that page. Use a simple loop that continues doing this until
the user enters blank)

3. Feedback evaluation (Learnjcu-> Feedback -> CP1404 Teaching and Subject Feedback)

4. Submit word file containing 1 & 2.

5. Online Test 5
"""

"""
Revision practice

Given:
subjects = {"CP1404":[60, 70, 80],
            "CP1401":[70, 80, 90]}
print the above data with string formatting like the following:
    CP1404    60%    70%    80.00%
"""

def get_rows(n):
    if n == 1:
        return 1
    else:
        return n + get_rows(n-1)

print("You need {} blocks. ".format(get_rows(6)))

import wikipedia

print(wikipedia.search("Barack Obama"))
