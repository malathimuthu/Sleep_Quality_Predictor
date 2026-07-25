// ===================================
// Sleep Quality Predictor
// Form Validation JavaScript
// ===================================


// Predict Form Validation

function validateSleepForm(){

    let age = document.getElementsByName("age")[0].value;
    let sleep = document.getElementsByName("sleep_duration")[0].value;
    let activity = document.getElementsByName("physical_activity")[0].value;
    let stress = document.getElementsByName("stress_level")[0].value;
    let heart = document.getElementsByName("heart_rate")[0].value;
    let steps = document.getElementsByName("daily_steps")[0].value;
    let screen = document.getElementsByName("screen_time")[0].value;


    // Age Check

    if(age < 1 || age > 100){

        alert("Please enter valid age");
        return false;

    }


    // Sleep Duration Check

    if(sleep < 0 || sleep > 24){

        alert("Sleep duration should be between 0-24 hours");
        return false;

    }


    // Physical Activity Check

    if(activity < 0){

        alert("Activity value cannot be negative");
        return false;

    }


    // Stress Level Check

    if(stress < 1 || stress > 10){

        alert("Stress level should be between 1 and 10");
        return false;

    }


    // Heart Rate Check

    if(heart < 30 || heart > 200){

        alert("Enter valid heart rate");
        return false;

    }


    // Daily Steps Check

    if(steps < 0){

        alert("Steps cannot be negative");
        return false;

    }


    // Screen Time Check

    if(screen < 0){

        alert("Screen time cannot be negative");
        return false;

    }


    return true;

}



// Confirm Prediction

function confirmPrediction(){

    return confirm(
        "Do you want to predict your sleep quality?"
    );

}