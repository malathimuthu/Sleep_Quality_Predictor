// =============================
// Sleep Quality Predictor
// Dashboard JavaScript
// =============================


// Page Load Message

document.addEventListener("DOMContentLoaded", function(){

    console.log("Dashboard Loaded Successfully ✅");


    // Animate Summary Cards

    const cards = document.querySelectorAll(".summary-card");


    cards.forEach((card,index)=>{

        card.style.opacity="0";

        setTimeout(()=>{

            card.style.transition="0.5s";
            card.style.opacity="1";

        }, index*200);

    });


});




// Confirm Clear History

function confirmClear(){

    let result = confirm(
        "Are you sure you want to clear all history?"
    );


    if(result){

        window.location.href="/clear_history";

    }

}




// Auto Refresh Dashboard (Optional)

function refreshDashboard(){

    location.reload();

}


// Chart Resize Support

window.addEventListener("resize", function(){

    if(window.Chart){

        Chart.helpers.each(
            Chart.instances,
            function(instance){

                instance.resize();

            }
        );

    }

});