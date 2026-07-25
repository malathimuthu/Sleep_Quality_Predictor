# ==========================================
# Sleep Quality Predictor
# Helper Functions
# ==========================================


# Sleep Quality Recommendation

def get_sleep_recommendation(quality):

    quality = str(quality).lower()


    if quality in ["excellent", "good"]:

        return (
            "Good sleep quality. "
            "Maintain your healthy routine, "
            "exercise regularly and keep a fixed sleep schedule."
        )


    elif quality == "average":

        return (
            "Average sleep quality. "
            "Reduce stress, avoid late night usage "
            "and maintain proper sleeping time."
        )


    else:

        return (
            "Poor sleep quality. "
            "Sleep 7-8 hours daily, reduce screen time "
            "and improve your lifestyle habits."
        )



# Extra Feature Tips

def get_extra_tips(screen_time, caffeine, mood):

    tips = []


    if screen_time > 90:

        tips.append(
            "Reduce screen time before bedtime."
        )


    if caffeine.lower() in ["high", "moderate"]:

        tips.append(
            "Avoid caffeine before sleeping."
        )


    if mood.lower() in ["sad", "anxious"]:

        tips.append(
            "Try relaxation activities before sleep."
        )


    return " ".join(tips)



# Sleep Category

def get_sleep_category(score):

    if score >= 8:

        return "Excellent"

    elif score >= 6:

        return "Good"

    else:

        return "Poor"