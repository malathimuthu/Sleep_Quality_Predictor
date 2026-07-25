// ===============================
// Sleep Quality Predictor
// Main JavaScript File
// ===============================


// Page Load

document.addEventListener("DOMContentLoaded", function(){

    console.log("Sleep Quality Predictor Loaded ✅");


});



// Form Validation

function validateForm(){

    let inputs = document.querySelectorAll(
        "input[required], select[required]"
    );


    for(let input of inputs){

        if(input.value.trim() === ""){

            alert(
                "Please fill all required fields"
            );

            input.focus();

            return false;

        }

    }


    return true;

}



// Predict Button Loading Effect

function showLoading(){

    let button = document.querySelector(
        ".predict-btn"
    );


    if(button){

        button.innerHTML =
        "⏳ Predicting...";


        button.disabled = true;

    }

}



// Reset Form

function resetForm(){

    let form = document.querySelector("form");


    if(form){

        form.reset();

    }

}



// Smooth Scroll

function scrollToSection(id){

    let section =
    document.getElementById(id);


    if(section){

        section.scrollIntoView({
            behavior:"smooth"
        });

    }

}



// Image Error Handling

function imageError(img){

    img.style.display="none";

    console.log(
        "Image not found"
    );

}