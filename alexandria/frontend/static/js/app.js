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