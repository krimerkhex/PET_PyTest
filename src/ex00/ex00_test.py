import json
import random
from variables import G_RESPIRATION_RANGE, G_HEART_RATE_RANGE, G_BLUSHING_LEVELS, G_PUPILLARY_DILATION_RANGE


def ask_question(question):
    """This first version of function for interaction with user.

        :param question: Dict with output values.
        :type question: dict[str].
        :return: choiced by user value.
        :rtype: int.
    """
    print(question["question"])
    responses = question["responses"]
    for i, response in enumerate(responses):
        print(f"{i + 1}. {response}")
    choice = input("Choose a response (1-3): ")
    return int(choice)


def run_test():
    """This main function of project it doing all. NO DECOMPOSOTION."""
    with open("questions.json") as file:
        questions = json.load(file)["questions"]
    variable_change = {"respiration": [], "heart_rate": [], "blushing_level": [], 'pupillary_dilation': []}
    score = 0
    for question in questions:
        score += ask_question(question)
        variable_change["respiration"].append(random.randint(G_RESPIRATION_RANGE[0], G_HEART_RATE_RANGE[1]))
        variable_change["heart_rate"].append(random.randint(G_HEART_RATE_RANGE[0], G_HEART_RATE_RANGE[1]))
        variable_change["blushing_level"].append(random.choice(G_BLUSHING_LEVELS))
        variable_change["pupillary_dilation"].append(
            random.randint(G_PUPILLARY_DILATION_RANGE[0], G_PUPILLARY_DILATION_RANGE[1]))
    decision = "Human" if score >= 12 else "Replicant"
    print(f"The subject is classified as: {decision}")
    print(variable_change)
