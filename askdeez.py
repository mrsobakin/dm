import sys
import random
from dataclasses import dataclass


@dataclass
class Question:
    theme: str
    question: str
    answer: str


def parse_questions(lines):
    theme = ""
    question = ""
    answer = []

    for line in lines:
        if line.startswith("####"):
            yield Question(theme, question, "".join(answer).strip())
            question = line.removeprefix("####").strip()
            answer = []

        elif line.startswith("##"):
            yield Question(theme, question, "".join(answer).strip())
            theme = line.removeprefix("##").strip()
            answer = []

        else:
            answer.append(line)

    yield Question(theme, question, "".join(answer).strip())

with open(sys.argv[1]) as f:
    questions = list(parse_questions(f.readlines()))

while True:
    random.shuffle(questions)
    for question in questions:
        print("Theme:")
        print("   ", question.theme)
        print("Question:")
        print("   ", question.question)
        input()
        print("Answer:")
        print("   ", question.answer)
        input()
        print()
        print()
        print()
