from json import load


def ask_answer(question):
    """This first version of function for interaction with user.

        :param question: Dict with output values.
        :type question: dict["question", "response"].
        :return: choised by user answer of question.
        :rtype: int.
    """
    flag = True
    choice = 0
    while flag:
        print(question["question"])
        responses = question["responses"]
        for i, response in enumerate(responses):
            print(f"{i + 1}. {response}")
        choice = input("Choose a response (1-3): ")
        if choice.isdigit():
            choice = int(choice)
            flag = check_in_range("Question", choice)
            if flag:
                print("Unvalid value. Please retry")
    return choice


def print_info(parameter):
    """This first version of function for output values range.

        :param parameter: current variable.
        :type parameter: str.
    """
    match parameter:
        case "respiration":
            print("Correct value [12, 16]", end=" ")
        case "heart_rate":
            print("Correct value [60, 100]", end=" ")
        case "blushing_level":
            print("Correct value [1, 7]", end=" ")
        case 'pupillary_dilation':
            print("Correct value [2, 8]", end=" ")


def ask_variable(parameter):
    """This first version of function for interaction with checkmate.

        :param parameter: current param.
        :type parameter: str.
        :return: choised by user answer value.
        :rtype: int.
    """
    flag = True
    choice = 0
    while flag:
        print("input information about", parameter, ":", end=" ")
        print_info(parameter)
        choice = input()
        if choice.isdigit():
            choice = int(choice)
            flag = check_in_range(parameter, choice)
            if flag:
                print("Unvalid value. Please retry")
    return choice


def accessories_check(variables_change: dict[str, list]):
    """This second version of function accessor human or replicant.

        :param variables_change: data for research.
        :type variables_change: dict[str, list]
        :return: Human/Replicant.
        :rtype: str
    """
    flag = True
    averange = 0
    jump = [2, 20, 2, 3]
    for index, key in enumerate(variables_change.keys()):
        averange = sum(variables_change[key]) / len(variables_change[key])
        min_v = averange - jump[index]
        max_v = averange + jump[index]
        for value in variables_change[key]:
            if value <= min_v or value >= max_v:
                flag = False
    return "Human" if flag else "Replicant"


def check_in_range(parameter, value) -> bool:
    """This function for check value out of range or not.

         :param parameter: parameter.
         :type parameter: str
         :param value: gave by user value.
         :type value: int
         :return: out of range?.
         :rtype: bool
    """
    flag = True
    match parameter:
        case "Question":
            flag = 1 <= value <= 3
        case "respiration":
            flag = 1 <= value <= 30
        case "heart_rate":
            flag = 40 <= value <= 200
        case "blushing_level":
            flag = 1 <= value <= 7
        case 'pupillary_dilation':
            flag = 1 <= value <= 10
    return not flag


def open_file(path):
    """This function for open file.

         :param path : path to file.
         :type path : str
         :return: value on file.
         :rtype: json
    """
    question_list = None
    with open(path) as file:
        question_list = load(file)["questions"]
    return question_list


def core(path):
    """This core function for project.

        :param path: path to file.
        :type path: str
    """
    question_list = open_file(path)
    if question_list is not None:
        variable_change = {"respiration": [], "heart_rate": [], "blushing_level": [], 'pupillary_dilation': []}
        score = 0
        for question in question_list:
            score += ask_answer(question) - 1
            for key in variable_change.keys():
                ret_v = ask_variable(key)
                variable_change[key].append(ret_v)
        print(accessories_check(variable_change))
