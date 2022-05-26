function red() {
    var e = document.getElementById("cat-body");

    if (!e) return true;
    if (e.style.backgroundColor == "red") {
        e.style.backgroundColor = ""
    } else {
        e.style.backgroundColor = "red"
    }
    return true;
}

function pink() {
    var e = document.getElementById("cat-body");

    if (!e) return true;
    if (e.style.backgroundColor == "pink") {
        e.style.backgroundColor = ""
    } else {
        e.style.backgroundColor = "pink"
    }
    return true;
}

function yellow() {
    var e = document.getElementById("cat-body");

    if (!e) return true;
    if (e.style.backgroundColor == "yellow") {
        e.style.backgroundColor = ""
    } else {
        e.style.backgroundColor = "yellow"
    }
    return true;
}


/*var pet = {
    'name' : "",
    'hungry' : true,
    'weight' : 0,
    'age' : 0,
    'photo' : "",
};


function feed(pet) {
    if (pet.hungry === true) {

    } else  {
    console.log("I'm full. I already ate!");
    }
}

function doSomething () {
    alert("It's Done!");
};
doSomething();





const Pet = prompt ("Name your pet");
document.write(Action);
let Energy = 0;
let Happiness = 0;
document.write(Energy);
document.write(Happiness);
for (i=0; i<6; i++){
    var Action = prompt ("feed, pet, or walk?");
    if (Action === "feed") {
        Energy = (Energy + 2);
    } else if (Action === "pet") {
        Happiness = (Happiness + 1);
    } else if (Action === "walk")
    {
        Happiness = ( Happiness + 2); 
        Energy = (Energy - 1);
    } 
}; 
console.log (Pet)
console.log (Happiness)
console.log (Energy)
console.log(+ Pet + " has " + Happiness + " happiness and " + Energy + " energy");*/