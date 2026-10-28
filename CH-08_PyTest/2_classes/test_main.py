from main import weather

def test_weather_check():
    w = weather()
    assert w.weather_check(35) == "Hot"
    assert w.weather_check(5) == "Cold"
    assert w.weather_check(20) == "Moderate"

def test_rain_check():
    w = weather()
    assert w.rain_check(0.5) == "There's a chance of rain. You might want to carry an umbrella."
    assert w.rain_check(0.2) == "It's unlikely to rain today."