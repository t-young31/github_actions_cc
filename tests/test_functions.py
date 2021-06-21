import pytest
import numpy as np
from example_module import sqrt


def test_sqrt():

    # Cannot square root a negative number with this function
    with pytest.raises(ValueError):
        _ = sqrt(-1.0)

    # but can with positive numbers
    assert np.isclose(sqrt(1.0), 1.0)
    assert np.isclose(sqrt(4.0), 2.0)
