function showHide(passwordId, toggleId) {
    const passwordField = document.getElementById(passwordId);
    const togglePassword = document.getElementById(toggleId);

    const isPasswordVisible = passwordField.type === "text";

    passwordField.type = isPasswordVisible ? "password" : "text";

    togglePassword.classList.toggle('fa-eye', isPasswordVisible);
    togglePassword.classList.toggle('fa-eye-slash', !isPasswordVisible);
}

