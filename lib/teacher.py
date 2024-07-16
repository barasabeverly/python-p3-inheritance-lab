#!/usr/bin/env python

from user import User

import random

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):

    
    def teach(self,knowledge):
        self.knowledge = knowledge
    random_number = random.randint(1, 10)
    for _ in range(5):
        random_number = random.randint(1, 10)
    print("Random number between 1 and 10:", random_number)
