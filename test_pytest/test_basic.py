import pytest


def test_basic_assertion():
    assert True


@pytest.fixture
def function_fixture():
    print('Fixture for each test')
    return 1


@pytest.fixture(scope='module')
def module_fixture():
    print('Fixture for module')
    return 2


# Como usar luminárias com teste no Pytest?
# Para usar o fixture no teste, você pode colocar o nome do fixture como argumento da função:

def test_function_fixture(function_fixture):
  assert function_fixture == 1


def test_yield_fixture(simple_yield_fixture):
  assert simple_yield_fixture == 3
