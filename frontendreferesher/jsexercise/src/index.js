function validateForm(name, email, contact, account) {
    let isValid = true;

    // Clear previous errors
    document.getElementById("nameError").innerText = "";
    document.getElementById("emailError").innerText = "";
    document.getElementById("contactError").innerText = "";
    document.getElementById("accountError").innerText = "";

    // Name validation (alphabets only)
    let nameRegex = /^[A-Za-z ]+$/;
    if (!nameRegex.test(name)) {
        document.getElementById("nameError").innerText = "Please enter only alphabets";
        isValid = false;
    }

    // Email validation
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        document.getElementById("emailError").innerText = "Please enter valid email";
        isValid = false;
    }

    // Contact validation (10 digits, starts with 7-9)
    let contactRegex = /^[7-9][0-9]{9}$/;
    if (!contactRegex.test(contact)) {
        document.getElementById("contactError").innerText = "Enter valid 10-digit number starting with 7-9";
        isValid = false;
    }

    // Account type validation
    if (account === "") {
        document.getElementById("accountError").innerText = "Please select account type";
        isValid = false;
    }

    return isValid;
}

function addCustomer() {
    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let contact = document.getElementById("contact").value.trim();
    let account = document.getElementById("account").value;

    if (!validateForm(name, email, contact, account)) {
        return;
    }

    // Create customer object
    let customer = {
        name: name,
        email: email,
        contact: contact,
        account: account
    };

    // Add to table
    let table = document.getElementById("customerTable");
    let row = table.insertRow();

    row.insertCell(0).innerText = customer.name;
    row.insertCell(1).innerText = customer.email;
    row.insertCell(2).innerText = customer.contact;
    row.insertCell(3).innerText = customer.account;

    // Clear form
    document.getElementById("name").value = "";
    document.getElementById("email").value = "";
    document.getElementById("contact").value = "";
    document.getElementById("account").value = "";
}