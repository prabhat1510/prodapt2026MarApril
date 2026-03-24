function displayInfo() {
    document.getElementById("id1").innerHTML = "You study daily";
    document.getElementById("tId1").innerHTML = "Focus and listen properly";
    document.getElementById("id2").innerHTML = "You are a bad boy";
    document.getElementById("id3").innerHTML = "You are a notorious boy";
    console.log(document.getElementById("id3"))
    console.log(document.getElementsByTagName('p'))
    console.log(document.getElementsByTagName('text'))
    console.log("************************************")
    console.log(document.getElementsByClassName('c1'))
    console.log(document.getElementsByClassName('c2'))
    document.getElementsByClassName('c1')[0].innerHTML = "Bahut Bhook Lagi Hai";
    document.getElementsByClassName('c2')[0].innerHTML = "SAAARRRR you are very boring !!!";
}