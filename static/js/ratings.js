document.addEventListener("DOMContentLoaded", () => {
    const editButtons = document.getElementsByClassName("btn-edit");
    const ratingText = document.getElementById("id_percentage_score");  // Ensure this ID matches
    const ratingForm = document.getElementById("ratingForm");
    const submitButton = document.getElementById("submitButton");

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let ratingId = e.target.getAttribute("rating_id");
            
            // Get the rating content as an integer
            let ratingContent = parseInt(document.getElementById(`rating${ratingId}`).innerText, 10);
            
            // Update the form input value
            if (ratingText) { // Check if ratingText is not null
                ratingText.value = ratingContent;
            } else {
                console.error("ratingText element not found");
            }

            // Update button text and form action
            submitButton.innerText = "Update";
            ratingForm.setAttribute("action", `edit_rating/${ratingId}`);
            console.log("Form action set to: ", ratingForm.action);  
        });
    }
});