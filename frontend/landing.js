function toggle(){
    //If login form visible, hide it; make visible if hidden
    log = document.getElementById("login");

    if(log.style.display == "block"){
        log.style.display = "none";
    }
    else{
        log.style.display = "block";
    }

    //If newUser form visible, hide it; make visible if hidden
    nU = document.getElementById("newUser");

    if(nU.style.display == "block"){
        nU.style.display = "none";
    }
    else{
        nU.style.display = "block";
    }

    //Change button text
    butt = document.getElementById("tog");

    if (butt.innerHTML == "New User"){
        butt.innerHTML = "Go to Login";
    }
    else{
        butt.innerHTML = "New User";
    }
}