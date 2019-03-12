
var bindEventTodoAdd = function(){
    console.log('go')
	input_area= document.querySelector('#myform')
	input_area.addEventListener('keypress', function(){
	    if(event.keyCode == 13){
	        console.log('entered')
	        input_value = input_area.value
	        first_list = document.querySelector('#mylist1')    //插入到列表中去
	        console.log(first_list)
	        var x = `<li class="list-group-item"><i class="far fa-square"></i>   ${input_value} <i class="fas fa-times cross-icon invisible"></i></li>`
	        first_list.insertAdjacentHTML('afterend', x)
	        var form ={ 'body': input_value }   //发送ajax请求去存储数据库
	        apiTodoAdd(form, function(r){
	            console.log(r)
	        }
	        )
	    }
	 }
	)
}




var bindEventTodoMark = function(){
	list_group= document.querySelector('#list-group')
	list_group.addEventListener('click', function(){
		the_target = event.target
		content= the_target.innerText
		if (the_target.firstElementChild.classList.contains('fa-square')){
			the_target.firstElementChild.classList.remove('fa-square')
			the_target.firstElementChild.classList.add('fa-check-square')
			console.log('改变了class') 
			var form ={ 'action': 'add_check', 'content': content }
			apiTodoMark (form, function(r){
				console.log(r)
			})

		}
		//-------------------------------------------------------------
		else {
			the_target.firstElementChild.classList.remove('fa-check-square')
        	the_target.firstElementChild.classList.add('fa-square')
        	var form={ 'action': 'remove_check', 'content':content}
        	apiTodoMark (form, function(r){
				console.log(r)
			})
		}

	})  //list_group



}




var bindEventTodoDelete = function(){
	list_group= document.querySelector('#list-group')
	list_group.addEventListener('dblclick', function(){
		console.log('dbclicked')
		the_target = event.target
		content= the_target.innerText
		the_target.remove()
		var form = {'action': 'remove_todo', 'content':content}
		apiTodoDelete (form, function(r){
				console.log('r')
			})

	})  //list_group


}


bindEventTodoAdd()
bindEventTodoMark()
bindEventTodoDelete()