// Getting inputs for checking
function getInputs(){
//    let canMinus = true;
    let number = 0;
    errArray = [
        document.getElementById("errorName"),
        document.getElementById("errorText"),
        document.getElementById("errorTitle")
     ]
    let inpArray = [
        document.getElementById("name").value,
        document.getElementById("text").value,
        document.getElementById("title").value
    ];
    for (let i in inpArray){
        if(inpArray[i].length <= 5){
            errArray[i].innerHTML = "The input is not full";
            errArray[i].style = "color: red;";
        }
        else if (inpArray[i].length >= 6) {
            errArray[i].style = "color: green;";
            errArray[i].innerHTML = "Valid";
        }
    }
    if (inpArray[0].length >= 6 && inpArray[1].length >= 6 && inpArray[2].length >= 6){
        document.forms[0].submit();
    }
}
function getInputs1(){
//    let canMinus = true;
    let number = 0;
    errArray = [
        document.getElementById("errorName"),
        document.getElementById("errorEmail"),
        document.getElementById("errorPat")
     ]
    let inpArray = [
        document.getElementById("name").value,
        document.getElementById("email").value,
        document.getElementById("pat").value
    ];
    for (let i in inpArray){
        if(inpArray[i].length <= 5){
            errArray[i].innerHTML = "The input is not full";
            errArray[i].style = "color: red;";
        }
        else if (inpArray[i].length >= 6) {
            errArray[i].style = "color: green;";
            errArray[i].innerHTML = "Valid";
        }
    }
    if (inpArray[0].length >= 6 && inpArray[1].length >= 6 && inpArray[2].length >= 6){
        document.forms[0].submit();
    }
}
