const burgerBtn = document.getElementById("burger")
const menuBlock = document.getElementById("menuBlock")
burgerBtn.addEventListener("click", function () {
    burgerBtn.classList.toggle("active")
    menuBlock.classList.toggle("activeMenu")
})
