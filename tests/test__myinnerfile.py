import pytest

from astro_package.my_folder.myinnerfile import check_city


@pytest.mark.parametrize(
    argnames= "city_name, expected_result",
    argvalues=[('New York', True),('bengaluru',False),('chennai', False),('mumbai', False)])

def test_check_city_for_correct_city(city_name, expected_result):
    assert check_city(city_name) == expected_result
