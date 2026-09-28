from src.predict import predict


def test_prediction_returns_number():
    features = [
        3.5,      # MedInc
        25.0,     # HouseAge
        5.0,      # AveRooms
        1.0,      # AveBedrms
        1000.0,   # Population
        3.0,      # AveOccup
        34.0,     # Latitude
        -118.0    # Longitude
    ]

    result = predict(features)

    assert isinstance(result, float)


def test_prediction_is_finite():
    features = [
        3.5,
        25.0,
        5.0,
        1.0,
        1000.0,
        3.0,
        34.0,
        -118.0
    ]

    result = predict(features)

    assert result == result  # not NaN