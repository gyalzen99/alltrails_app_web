const menuButton= document.querySelector('.menuBtn')
const menuModel = document.querySelector('.rightSide')
const closeButton = document.querySelector('.closeBtn')
const navBar = document.querySelector('.topNavBar')

menuButton.addEventListener('click', () => {
    navBar.style.display = 'none'
    menuModel.style.display = 'block'
})

closeButton.addEventListener('click', () => {
    navBar.style.display = 'flex'
    menuModel.style.display = 'none'
})