var btnSignin = document.querySelector("#signin");
var btnSignup = document.querySelector("#signup");

var body = document.querySelector("body");


btnSignin.addEventListener("click", function () {
   body.className = "sign-in-js"; 
});

btnSignup.addEventListener("click", function () {
    body.className = "sign-up-js";
})

function check_form(){
  var inputs = document.getElementsByClassName('required');
  var len = inputs.length;
  var valid = true;
  for (var i=0; i < len; i++){
    if (!inputs[i].value){valid = false}
  }
  if (!valid){
    alert('Preencha todos os campos para o cadastro.');
    return false;
  } else{ return true }
}

function check_form_log(){
  var inputs = document.getElementsByClassName('required_log');
  var len = inputs.length;
  var valid = true;
  for (var i=0; i < len; i++){
    if (!inputs[i].value){valid = false}
  }
  if (!valid){
    alert('Preencha todos os campos para logar.');
    return false;
  } else { return true }
}


  
