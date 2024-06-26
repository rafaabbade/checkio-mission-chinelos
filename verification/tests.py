"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
         {
        "input": [5, [4, 2, 0, 3, 2], 2, [1, 3]],
        "answer": 1
    },
    {
        "input": [4, [1, 3, 2, 5], 4, [3, 3, 3, 4]],
        "answer": 3
    },
    {
        "input": [3, [0, 0, 0], 3, [1, 2, 3]],
        "answer": 0
    },
    {
        "input": [3, [1, 5, 5], 6, [1, 1, 2, 2, 3, 3]],
        "answer": 5
    },
    {
        "input": [5, [10, 0, 10, 0, 10], 5, [2, 4, 1, 3, 5]],
        "answer": 3
    }
    ]
}
