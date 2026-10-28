from main import weather_check

# Test cases for weather_check function
def test_weather_check():
    assert weather_check(-5) == "Freezing"
    assert weather_check(10) == "Cold"
    assert weather_check(25) == "Warm"
    assert weather_check(35) == "Hot"

if __name__ == "__main__":
    test_weather_check()