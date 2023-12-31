// 改变标题颜色
function changeColor() {
    let el = document.getElementById("title1")
    el.setAttribute("style", "color:red")
}
// changeColor()

//第一个节点
function firstnode() {
    let el = document.getElementById("title1")
    let childnode = el.firstChild
    console.log(el.firstChild)
    // childnode.setAttribute("style","color:blue")
}

firstnode()