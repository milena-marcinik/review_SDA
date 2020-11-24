from unittest.mock import MagicMock, patch

from .avg_calculator import AvgCalculator


def test_calculate_avg():
    data = [['1', '2', '3', '4', '5'], ['2', '4', '1', '12']]
    # return_value parameter  allows  to set the mock action to return what we defined.
    mock = MagicMock(return_value=data)

    with patch('Testing.mock.avg_calculator.AvgCalculator._get_content', mock):
        avg_calc = AvgCalculator('fake.txt')
        assert avg_calc.calculate() == [3.0, 4.75]


def test_get_raw_data():
    data = [['1', '2', '3', '4', '5'], ['2', '4', '1', '12']]
    mock = MagicMock(return_value=data)

    with patch('Testing.mock.avg_calculator.AvgCalculator._get_content', mock):
        avg_calc = AvgCalculator('fake.txt')
        assert avg_calc.get_data() == data
