import pytest
from prueba2 import edad

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (1, "Eres menor"),
      (0,"Eres menor"),
      (100, "Eres mayor")
      
    ]
  )
def test_edad_params(input_n1, expected):
    assert edad(input_n1) == expected