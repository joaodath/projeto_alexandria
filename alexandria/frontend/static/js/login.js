function validar() {
   // pegando o valor do nome pelos names
   var nome = document.getElementById("name");
   var email = document.getElementById("email");
   var password = document.getElementById("password")
 
   // verificar se o nome está vazio
   if (nome.value == "" || nome.value == null || nome.value.lenght < 3) {
     alert("Nome não informado");
     // Deixa o input com o focus
     nome.focus();
     // retorna a função e não olha as outras linhas
     return;
   }
   if (email.value == "" || email.value == null || email.value.indexOf('@') == -1 || email.value.indexOf('.') == -1) {
     alert("E-mail não informado");
     email.focus();
     return;
   }
   if (password.value == "" || password.value == null || password.value.lenght < 5) {
     alert("Senha não informada");
     senha.focus();
     return;
   }
   alert("Formulário enviado!");
   // envia o formulário
   //formulario.submit();
 }

// var nome = document.getElementById('name')
// var email = document.getElementById('email')
// var password = document.getElementById('password')
// var btnEnviar = document.getElementById('enviar')
// var nomeOk = false
// var emailOk = false
// var passwordOk = false
// btnEnviar.disabled = true

// nome.addEventListener('keyup', () => {
//    if (nome.value == "" || nome.value == null || nome.value.lenght < 3){
//       nome.style.borderColor = 'red'
//       nomeOk = false
//    } else{
//       nome.style.borderColor = 'green'
//    }

//    if (nomeok && emailOk && passwordOk){
//       btnEnviar.disabled = false
//    } else{
//       btnEnviar.disabled = true
//    }
// })

// email.addEventListener('keyup', () =>{
//    if (email.value == "" || email.value == null || email.value.indexOf('@') == -1 || email.value.indexOf('.') == -1){
//       email.style.borderColor = 'red'
//       emailOk = false
//    } else{
//       email.style.borderColor = 'green'
//    }

//    if (nomeok && emailOk && passwordOk){
//       btnEnviar.disabled = false
//    } else{
//       btnEnviar.disabled = true
//    }
// })

// password.addEventListener('keyup', () =>{
//    if (password.value == "" || password.value == null || password.value.lenght < 5){
//       password.style.borderColor = 'red'
//       passwordOk = false
//    } else{
//       passwordOk = true
//    }

//    if (nomeok && emailOk && passwordOk){
//       btnEnviar.disabled = false
//    } else{
//       btnEnviar.disabled = true
//    }
// })


// /* o parâmetro frm desta função significa: this.form, pois a chamada da função - validaForm(this) foi definida na tag form.*/
// function validaForm(frm) {
//    //Verifica se o campo nome foi preenchido e
//     //contém no mínimo três caracteres.
//     if(frm.name.value == "" || frm.name.value == null || frm.name.value.lenght < 3) {
//         //É mostrado um alerta, caso o campo esteja vazio.
//         alert("Por favor, indique o seu nome.");
//         //Foi definido um focus no campo.
//         frm.name.focus();
//         //o form não é enviado.
//         return false;
//     }
//     //o campo e-mail precisa de conter: "@", "." e não pode estar vazio
//     if(frm.email.value.indexOf("@") == -1 ||
//       frm.email.valueOf.indexOf(".") == -1 ||
//       frm.email.value == "" ||
//       frm.email.value == null) {
//         alert("Por favor, indique um e-mail válido.");
//         frm.email.focus();
//         return false;
//     }
//     // a senha não pode conter menos de 5 caracteres e não pode estar vazia.
//     if(frm.password.value == "" || frm.password.value == null || frm.password.value.lenght < 5) {
//       //É mostrado um alerta, caso o campo esteja vazio.
//       alert("Por favor, indique o seu nome.");
//       frm.password.focus();
//       return false;
//   }
//    }

