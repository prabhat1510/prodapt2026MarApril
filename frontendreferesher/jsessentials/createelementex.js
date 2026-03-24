function addNode() {
    var p = document.createElement("p");
    p.innerHTML = "This is a new paragraph";
    document.body.appendChild(p);
}

function deleteNode() {
    var p = document.getElementsByTagName("p");
    document.body.removeChild(p[p.length - 1]);
}