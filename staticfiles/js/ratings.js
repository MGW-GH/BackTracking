const editButtons = document.getElementsByClassName("btn-edit");
const ratingText = document.getElementById("id_body");
const ratingForm = document.getElementById("ratingForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let ratingId = e.target.getAttribute("rating_id");
    let ratingContent = document.getElementById(`rating${ratingId}`).innerText;
    ratingText.value = ratingContent;
    submitButton.innerText = "Update";
    ratingForm.setAttribute("action", `edit_rating/${ratingId}`);
  });
}