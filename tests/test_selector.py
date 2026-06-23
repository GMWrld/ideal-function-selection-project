from core.selector import FunctionSelectionService


def test_sse_calculation():

    selector = FunctionSelectionService()

    training = [1, 2, 3]

    ideal = [1, 2, 3]

    sse = selector.calculate_sse(
        training,
        ideal
    )

    assert sse == 0