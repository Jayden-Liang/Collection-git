var ajax = function(method, path, data, responseCallback) {
    var r = new XMLHttpRequest()           // 设置请求方法和请求地址
    r.open(method, path, true)
    csrf_token = document.querySelector('#csrf_token')
    r.setRequestHeader("X-CSRFToken", csrf_token.value) 
    r.setRequestHeader('Content-Type', 'application/json') 
    r.onreadystatechange = function() {     // 注册响应函数
        if(r.readyState === 4) {
            responseCallback(r.response)   
        }  // r.response 存的就是服务器发过来的放在 HTTP BODY 中的数据
    }
    // 把数据转换为 json 格式字符串
    data = JSON.stringify(data)
    // 发送请求
    r.send(data)
}


var apiTodoAdd = function(form, callback) {
    var path ='/api/todo/add'
    console.log('apihere')
    ajax('POST', path, form, callback)
}


var apiTodoMark = function(form, callback){
    var path = '/api/todo/mark'
    ajax('POST', path, form, callback)
}

var apiTodoDelete = function(form, callback) {
    var path ='/api/todo/delete'
    ajax('POST', path, form, callback)
}