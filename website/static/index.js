function deleteNote(noteId) {
    // 1. Confirm deletion
    if (!confirm('¿Estás seguro de que deseas borrar esta nota?')) {
        return;
    }

    // 2. Replace button with spinner
    const deleteBtn = event.target;
    deleteBtn.disabled = true;
    deleteBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>';

    // 3. Fetch with error handling
    fetch('/delete-note', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ noteId: noteId }),   
    })
    .then((res) => {
        if (!res.ok) {
            throw new Error('Error deleting note');
        }
        return res.json();
    })
    .then(() => {
        // Success: reload the page
        window.location.href = "/";
    })
    .catch((error) => {
        // Error: show alert and reset button
        alert('Error deleting note: ' + error.message);
        deleteBtn.disabled = false;
        deleteBtn.innerHTML = '×';
    });
}


function togglePassword(button, inputId) {
    const input = document.getElementById(inputId);
    const openEye = button.querySelector(".eye-open");
    const closedEye = button.querySelector(".eye-closed");

    if (!input || !openEye || !closedEye) {
        console.error("Elemento no encontrado");
        return;
    }

    if (input.type === "password") {
        input.type = "text";
        openEye.classList.add("d-none");
        closedEye.classList.remove("d-none");
    } else {
        input.type = "password";
        closedEye.classList.add("d-none");
        openEye.classList.remove("d-none");
    }
}