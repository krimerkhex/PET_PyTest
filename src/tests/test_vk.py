import pytest
import ex01.ex01_test as testing_func

replicant_test_data = [
    {'respiration': [15, 17, 21, 1, 28, 26, 8, 26, 28, 26],
     'heart_rate': [171, 44, 106, 76, 74, 155, 119, 101, 108, 116],
     'blushing_level': [4, 1, 6, 1, 7, 6, 3, 1, 6, 5],
     'pupillary_dilation': [3, 4, 4, 1, 3, 4, 6, 9, 4, 1]},
    {'respiration': [21, 18, 9, 5, 16, 23, 3, 30, 1, 7],
     'heart_rate': [61, 100, 134, 46, 43, 139, 59, 101, 101, 154],
     'blushing_level': [2, 3, 7, 6, 5, 7, 5, 1, 1, 7],
     'pupillary_dilation': [5, 2, 8, 5, 10, 4, 3, 3, 4, 10]},
    {'respiration': [30, 7, 1, 1, 16, 22, 18, 21, 23, 25],
     'heart_rate': [84, 135, 76, 185, 92, 197, 112, 85, 196, 189],
     'blushing_level': [7, 5, 6, 7, 1, 5, 3, 7, 4, 1],
     'pupillary_dilation': [9, 6, 10, 9, 7, 4, 8, 4, 4, 10]},
    {'respiration': [1, 28, 11, 12, 4, 16, 24, 19, 20, 5],
     'heart_rate': [84, 169, 143, 147, 133, 66, 121, 121, 138, 186],
     'blushing_level': [4, 7, 6, 1, 5, 2, 2, 3, 1, 6],
     'pupillary_dilation': [10, 4, 3, 3, 9, 6, 9, 2, 2, 4]},
    {'respiration': [25, 30, 23, 2, 14, 27, 18, 17, 13, 6],
     'heart_rate': [109, 152, 155, 161, 189, 67, 134, 63, 116, 55],
     'blushing_level': [7, 3, 4, 5, 4, 2, 2, 7, 2, 2],
     'pupillary_dilation': [10, 2, 5, 5, 9, 3, 1, 6, 10, 3]}
]

human_test_data = [
    {'respiration': [14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
     'heart_rate': [14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
     'blushing_level': [14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
     'pupillary_dilation': [14, 14, 14, 14, 14, 14, 14, 14, 14, 14]},
    {'respiration': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
     'heart_rate': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
     'blushing_level': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
     'pupillary_dilation': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]},
    {'respiration': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
     'heart_rate': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
     'blushing_level': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
     'pupillary_dilation': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]},
    {'respiration': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     'heart_rate': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     'blushing_level': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     'pupillary_dilation': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
]


class TestHumanOrReplicant:
    @pytest.mark.parametrize("variable_change", replicant_test_data)
    def test_replicant(self, variable_change):
        """This fuction checks of definition replicant.

            :param variable_change:  checking data.
            :type variable_change: list[dict].
        """
        assert 'Replicant' == testing_func.accessories_check(variable_change)

    @pytest.mark.parametrize("variable_change", human_test_data)
    def test_human(self, variable_change):
        """This fuction checks of definition human.

            :param variable_change:  checking data.
            :type variable_change: list[dict].
        """
        assert 'Human' == testing_func.accessories_check(variable_change)

    def test_unvalid_file(self):
        """This fuction checks what will hepening when no file."""
        assert testing_func.core("")
