# ==========================================
# Sleep Quality Recommendation Module
# ==========================================


def get_recommendation(quality):

    quality = str(quality).lower()


    if quality in ["excellent", "good"]:

        return (
            "Your sleep quality is good. "
            "Continue maintaining a regular sleep schedule, "
            "exercise regularly and stay hydrated."
        )


    elif quality == "average":

        return (
            "Your sleep quality is average. "
            "Reduce stress, avoid late night mobile usage "
            "and maintain consistent sleeping hours."
        )


    else:

        return (
            "Your sleep quality is poor. "
            "Try sleeping 7-8 hours daily, "
            "reduce screen time before bed and avoid caffeine at night."
        )



# Extra Feature Recommendations

def get_extra_recommendation(
        screen_time,
        caffeine,
        mood,
        bedtime,
        wake_time):


    tips = []


    # Screen Time

    if screen_time > 90:

        tips.append(
            "Reduce screen time 30-60 minutes before sleep."
        )


    # Caffeine

    if caffeine.lower() in ["high", "moderate"]:

        tips.append(
            "Avoid caffeine before bedtime."
        )


    # Mood

    if mood.lower() in ["sad", "anxious"]:

        tips.append(
            "Practice relaxation activities like meditation."
        )


    # Sleep Time

    if bedtime > "23:00":

        tips.append(
            "Try sleeping earlier for better sleep quality."
        )


    return " ".join(tips)