function validateForm() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if (name == "" || email == "" || password == "") {
        alert("All fields are required");
        return false;
    }
    if (name.length < 3 || name.length > 10) {
        alert("Name must be at least 3 characters long");
        return false;
    }
    if (email.indexOf("@") == -1 || email.indexOf(".") == -1) {
        alert("Email is invalid");
        return false;
    }
    if (password.length < 6 || password.length > 12) {
        alert("Password must be at least 6 characters long");
        return false;
    }
    return true;
}