
var z=$('input#zz')

var f=function(){
    var x = new XMLHttpRequest()
    x.open('get','http://127.0.0.1:5000/index')

    

    x.onreadystatechange=function(){
        console.log(x.readyState)
        console.log(x.status)
        
    }
    x.send()
    console.log(x.responseText)
}  
    

var g=function(){
    alert('hello')
}
g()
z.click(f)
