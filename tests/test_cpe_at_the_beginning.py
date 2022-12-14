import pytest
import sys

# setting path
sys.path.append("../src")
from validationOfStringCPE import validationOfTheBeginningOfTheString


def test_cpe_at_the_beginning() -> None:

    listOfPossibleInputs = ["wewe23:32", "daasw", "cpe2.3:3232"]

    for item in listOfPossibleInputs:
        with pytest.raises(ValueError):
            validationOfTheBeginningOfTheString(item)
