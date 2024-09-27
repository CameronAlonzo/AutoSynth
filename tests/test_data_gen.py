from autosynth import generate_synthetic_data

def test_data_generation():
    X, Y = generate_synthetic_data(100, 5)
    assert X.shape == (100, 5)
    assert len(Y) == 100