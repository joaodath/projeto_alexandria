const getElement = (selector) => {
  const el = document.querySelector(selector)
  if (el) return el
  throw new Error(`Please check your classes : ${selector} does not exist`)
}

const sidebarToggle = getElement('.sidebar-toggle')
const sidebar = getElement('.sidebar')
const closeBtn = getElement('.close-btn')

sidebarToggle.addEventListener('click', function () {
  sidebar.classList.toggle('show-sidebar')
})

closeBtn.addEventListener('click', () => {
  sidebar.classList.remove('show-sidebar')
})

const modalBtn = getElement('.modal-btn')
const modal = getElement('.modal-overlay')
const closeBtn2 = getElement('.close-btn2')


modalBtn.addEventListener('click', function () {
  modal.classList.add('open-modal')
})
closeBtn2.addEventListener('click', function () {
  modal.classList.remove('open-modal')
})



// let inputNome = document.querySelector('#nome') /* Cria a variável inputNome e coloca nela o elemento que possui o id nome */
// let inputEmail = document.querySelector('#email') /* Cria a variável inputEmail e coloca nela o elemento que possui o id email */
// let textareaMensagem = document.querySelector('#mensagem') /* Cria a variável textareaMensagem e coloca nela o elemento que possui o id mensagem */
// let btnEnviar = document.querySelector('#enviar') /* Cria a variável btnEnviar e coloca nela o elemento que possui o id enviar */
// let nomeOk = false /* variável de controle para o botão */
// let emailOk = false /* variável de controle para o botão */
// let msgOk = false /* variável de controle para o botão */
// btnEnviar.disabled = true /* Desabilita o botão assim que inicia a página html */

// /* Só posso utilziar a arrow function (=>) quando a função não tiver nome */

// /* Adiciona um evento de keyup no inputNome e realiza a função */
// inputNome.addEventListener('keydown', () => { 
//    /* Verifica se o tamanho do valor do inputNome é menor que 2 */
//    if(inputNome.value.length < 2){
//       inputNome.style.borderColor = 'red' /* Troca a cor da borda do input para red */
//       nomeOk = false
//    } else {
//       inputNome.style.borderColor = 'green' /* Troca a cor da borda do input para green */
//       nomeOk = true
//    }

//    if(inputNome.value == '' || inputNome.value == undefined || inputNome.value == null) {
//       inputNome.style.borderColor = '#ccc'
//    }

//    /* Se todas as variáveis forem true habilita o botão */
//    if (nomeOk && emailOk && msgOk) {
//       btnEnviar.disabled = false
//    } else { /* se não, desabilita */
//       btnEnviar.disabled = true
//    }

// })


// /* Adiciona um evento de keyup no inputEmail e realiza a função */
// inputEmail.addEventListener('keyup', () => {
//    /* 
//    O indexOf procura um caractere no valor do inputEmail, se esse valor não existir ele retorna -1. 
//    Então essa expressão inputEmail.value.indexOf('@') == -1 é a mesmo coisa que:
//    Se no valor de inputEmail não existir @, faça...
//    || é o operador OU em JavaScript
//    && é o operador E em JavaScript
//    */
//    if(inputEmail.value.indexOf('@') == -1 || inputEmail.value.indexOf('.') == -1){
//       inputEmail.style.borderColor = 'red' /* Troca a cor da borda do input para red */
//       emailOk = false
//    } else {
//       inputEmail.style.borderColor = 'green' /* Troca a cor da borda do input para green */
//       emailOk = true
//    }  

//    /* Se todas as variáveis forem true habilita o botão */
//    if (nomeOk && emailOk && msgOk) {
//       btnEnviar.disabled = false
//    } else { /* se não, desabilita */
//       btnEnviar.disabled = true
//    }
// })

// /* Adiciona um evento de keyup no textareaMensagem e realiza a função */
// textareaMensagem.addEventListener('keyup', ()=>{
//    /* Verifica se o tamanho do valor do textareaMensagem é maior que 100  */
//    if(textareaMensagem.value.length > 100){
//       textareaMensagem.style.borderColor = 'red' /* Troca a cor da borda do input para red */
//       msgOk = false
//    } else {
//       textareaMensagem.style.borderColor = 'green' /* Troca a cor da borda do input para green */
//       msgOk = true
//    }

//    /* Se todas as variáveis forem true habilita o botão */
//    if (nomeOk && emailOk && msgOk) {
//       btnEnviar.disabled = false
//    } else { /* se não, desabilita */
//       btnEnviar.disabled = true
//    }
// })


// btnEnviar.addEventListener('click', () => {
//    /* Pega a div de carregamento */
//    let carregamento = document.querySelector('#carregamento')
//    /* Mostra a div de carregamento, adicionando o 'flex' ao display */
//    carregamento.style.display = 'flex'

//    /* Pega o Form */
//    let form = document.querySelector('form')
//    /* Esconde o Form, mudando o display pra 'none' */
//    form.style.display = 'none'
// })