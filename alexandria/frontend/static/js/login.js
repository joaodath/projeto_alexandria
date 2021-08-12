function check_form(){
  var inputs = document.getElementsByClassName('required');
  var len = inputs.length;
  var valid = true;
  for (var i=0; i < len; i++){
    if (!inputs[i].value){valid = false}
  }
  if (!valid){
    alert('Preencha todos os campos.');
    return false;
  } else{ return true }
}

  
