
from application import get_operating_system


def test_get_operating_system(mocker):
    # Mock the slow function and return True always
    mocker.patch('application.is_windows', return_value=True)

    assert get_operating_system() == 'Windows'

