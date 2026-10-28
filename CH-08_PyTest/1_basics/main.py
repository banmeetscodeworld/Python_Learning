def weather_check(temp:float)-> str:
    if temp<0:
        return "Freezing"
    elif temp<20:
        return "Cold"
    elif temp<30:
        return "Warm"
    else:
        return "Hot"