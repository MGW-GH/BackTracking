
const editButtons = document.getElementsByClassName("btn-edit");
const ratingText = document.getElementById("id_percentage_score");
const ratingForm = document.getElementById("ratingForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let ratingId = e.target.dataset.ratingId;
        
        let ratingContent = parseInt(document.getElementById(`rating${ratingId}`).innerText, 10);
        
        if (ratingText) {
            ratingText.value = ratingContent;
        } else {
            console.error("ratingText element not found");
        }

        submitButton.innerText = "Update";
        ratingForm.setAttribute("action", `/blog/${title}/edit_rating/${ratingId}`);
        console.log("Form action set to: ", ratingForm.action);  
    });
}


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let ratingId = e.target.getAttribute("data-rating-id");
      deleteConfirm.href = `delete_rating/${ratingId}`;
      deleteModal.show();
    });
  }


  const deleteStampButtons = document.getElementsByClassName("btn-delete-stamp");
  const deleteStampModal = new bootstrap.Modal(document.getElementById("deleteStampModal"));
  const deleteConfirmStamp = document.getElementById("deleteConfirmStamp");
  
  for (let button of deleteStampButtons) {
      button.addEventListener("click", (e) => {
          deleteStampModal.show();
      });
  }
