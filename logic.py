def get_advice(crop, weather):
    if crop.lower() == "paddy" and weather == "rain":
        return "Rain expected! Delay irrigation for now."
    elif crop.lower() == "brinjal":
        return "Watch for pest outbreaks this season."
    else:
        return "No special advice today. Carry on with normal practices."
