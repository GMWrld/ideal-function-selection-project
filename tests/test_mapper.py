from core.mapper import MappingService


def test_max_deviation():

    mapper = MappingService()

    training = [1, 2, 3]

    ideal = [1.5, 2.5, 3.5]

    max_dev = mapper.calculate_max_deviation(
        training,
        ideal
    )

    assert max_dev == 0.5

def test_threshold():

    mapper = MappingService()

    threshold = mapper.calculate_threshold(
        0.5
    )

    assert threshold > 0.5

def test_test_deviation():

    mapper = MappingService()

    deviation = mapper.calculate_test_deviation(
        10,
        9.5
    )

    assert deviation == 0.5