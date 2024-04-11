.. Blade Runner documentation master file, created by
   sphinx-quickstart on Tue Jan 23 02:05:37 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Blade Runner's documentation!
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Test Start
========================================

   cd tests
   pytest test_vk.py
   relax


Function Description
========================================

EX00/ex00_test.py
========================================

The ``ex00_test.ask_question(question)`` function:
.. py:function::ask_question(question)

   This first version of function for interaction with user.

   :param question: Dict with output values.
   :type question: dict[str].
   :return: choiced by user value.
   :rtype: int.


The ``ex00_test.run_test()`` function:
.. py:function::run_test()

   This main function of project it doing all.

EX01/ex01_test.py
========================================

The ``ex01_test.ask_answer(question)`` function:
.. py:function::ask_answer(question)

   This first version of function for interaction with user.

   :param question: Dict with output values.
   :type question: dict["question", "response"].
   :return: choised by user answer of question.
   :rtype: int.

The ``ex01_test.print_info(parameter)`` function:
.. py:function::print_info(parameter)

   This first version of function for output values range.

   :param parameter: current variable.
   :type parameter: str.

The ``ex01_test.ask_variable(parameter)`` function:
.. py:function::ask_variable(parameter):

   This first version of function for interaction with checkmate.

   :param parameter: current param.
   :type parameter: str.
   :return: choised by user answer value.
   :rtype: int.

The ``ex01_test.accessories_check(variables_change)`` function:
.. py:function::accessories_check(variables_change: dict[str, list])

   This second version of function accessor human or replicant.

   :param variables_change: data for research.
   :type variables_change: dict[str, list]
   :return: Human/Replicant.
   :rtype: str

The ``ex01_test.check_in_range(parameter, value)`` function:
.. py:function::check_in_range(parameter, value)

   This function for check value out of range or not.

   :param parameter: parameter.
   :type parameter: str
   :param value: gave by user value.
   :type value: int
   :return: out of range?.
   :rtype: bool

The ``ex01_test.open_file(path)`` function:
.. py:function::open_file(path):

   This function for open file.

   :param path : path to file.
   :type path : str
   :return: value on file.
   :rtype: json

The ``ex01_test.core(path)`` function:
.. py:function::core(path):

   This core function for project.

   :param path: path to file.
   :type path: str