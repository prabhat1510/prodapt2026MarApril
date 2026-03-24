let parties = ["TMC", "BJD", "JDU", "RJD", "AIADMK", "DMK", "TVK", "PMK", "SAD", "LDF"]
let party = "DMK";

parties.forEach(element => {
    if (element == party) {
        console.log("Party Found")
    } else {
        console.log("Party Not Found")
    }
});
console.log("**************************************")
function searchParty(p) {
    return p == "AIADMK";
}

console.log(parties.find(searchParty));

console.log("**************************************")
function searchParty1(p) {
    return p != "AIADMK";
}
console.log(parties.filter(searchParty1));
console.log("**************************************")
console.log(parties.filter((e) => { return e != "RJD" }))
console.log("**************************************")
console.log(parties.map((e) => { return e.toUpperCase() }))