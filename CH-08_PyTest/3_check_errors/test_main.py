from main import weather
import pytest

def test_weather_check():
    w = weather()
    assert w.weather_check(35) == "Hot"
    assert w.weather_check(5) == "Cold"
    assert w.weather_check(20) == "Moderate"

def test_rain_check():
    w = weather()
    assert w.rain_check(0.8) == "It's likely to rain. Don't forget your umbrella!"
    assert w.rain_check(0.5) == "There's a chance of rain. You might want to carry an umbrella."
    assert w.rain_check(0.2) == "It's  unlikely to rain today."

def test_divide():
    w = weather()
    assert w.divide(10, 2) == 5
    assert w.divide(9, 3) == 3

    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        w.divide(5, 0)