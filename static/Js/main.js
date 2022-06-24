console.log("if youre working !!!")

let add_to_cart_btns = document.getElementsByClassName("btn-primary")
for(let i =0; i < add_to_cart_btns.length; i++) {
    addCartItemButton[i].addEventListener("click", addToCart)
}
function addToCart(event){
    let btn = event.target
    let btn_parent = btn.parentElement
    let btn_grandparent = btn.parentElement.parentElement
    let itemName = btn_parent.children[0].innerText
    // let itemPrice = 
    // let itemImage = 

    console.log(itemName)

}
