var ul = $('#test-div>input');
var x=function(){
    console.log('wowo')
}

var y=function(){
    console.log('hello')
}
ul.val('change it!');
ul.change(y())


