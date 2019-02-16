console.log('执行topic.js')
var ajax = function(method, path, data, responseCallback) {
    var r = new XMLHttpRequest()
    // 设置请求方法和请求地址
    r.open(method, path, true)
    // 设置发送的数据的格式为 application/json
    // 这个不是必须的
    r.setRequestHeader('Content-Type', 'application/json')
    // 注册响应函数
    r.onreadystatechange = function() {
        if(r.readyState === 4) {
            // r.response 存的就是服务器发过来的放在 HTTP BODY 中的数据
            responseCallback(r.response)
        }
    }
    // 把数据转换为 json 格式字符串
    data = JSON.stringify(data)
    // 发送请求
    r.send(data)
}


var api_topic = function(theTopic, callback) {
    var path = '/topic/'+ theTopic
    ajax('GET', path, '', callback)
}

// var insertopicData(x, y){
//     pass
//     console.log('here')
// }

var add_topicData = function(topic_data){
    var main_content = document.getElementsByClassName("main_content")[0];
    while(main_content.hasChildNodes()){
      main_content.removeChild(main_content.firstChild);}
    var list1 = [];
    for (x in topic_data){
       t =`
            <p><a href="/detail/${x} " class="content_title">${topic_data[x]}</a></p>

            <HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#f1f1f1 SIZE=1>
          `
        main_content.insertAdjacentHTML("beforeEnd", t);
      }
     }



var load = function() {
  var allTopics = document.getElementsByClassName("topics")[0];
  allTopics.addEventListener('click', function(event){
    var self = event.target
    if(self.classList.contains('topic_span')){
        theTopic= self.innerHTML
      }
      api_topic(theTopic, function(r){
        console.log('查看返回：', r)
        topic_data = JSON.parse(r)
        add_topicData(topic_data)
      })
    })

}

load()
