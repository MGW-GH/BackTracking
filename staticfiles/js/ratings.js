
const editButtons = document.getElementsByClassName("btn-edit");
const ratingText = document.getElementById("id_percentage_score");  // Ensure this ID matches
const ratingForm = document.getElementById("ratingForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

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

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let ratingId = e.target.getAttribute("rating_id");
      deleteConfirm.href = `delete_rating/${ratingId}`;
      deleteModal.show();
    });
  }


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        // Assuming you have a data attribute for the stamp title
        const stampTitle = e.target.getAttribute("data-title");
        // Set the href for the delete confirmation
        deleteConfirm.href = `/blog/stamp/delete/${stampTitle}/`; // Adjust this path to match your URL structure
        deleteModal.show();
    });
}