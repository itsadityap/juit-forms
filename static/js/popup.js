document.addEventListener("DOMContentLoaded", function() {
    var deleteEventLinks = document.querySelectorAll("[data-bs-toggle='modal'][data-bs-target='#deleteConfirmationModal']");
    
    deleteEventLinks.forEach(function(link) {
        link.addEventListener("click", function(event) {
            event.preventDefault(); // Prevent default link behavior
            
            var modalId = link.getAttribute("data-model-id");
            var formId = link.getAttribute("data-form-id");
            var modalTitle = link.getAttribute("data-model-name");
            var deleteUrl = `/form/${formId}/${modalTitle}/${modalId}/delete/`;
            
            document.getElementById("confirmDeleteButton").setAttribute("data-delete-url", deleteUrl);
        });
    });
    
    var confirmDeleteButton = document.getElementById("confirmDeleteButton");
    
    confirmDeleteButton.addEventListener("click", function() {
        var deleteUrl = confirmDeleteButton.getAttribute("data-delete-url");
        if (deleteUrl) {
            window.location.href = deleteUrl;
        }
    });
});

