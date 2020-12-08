
d=document;
/**
* Основная функция.
* @param {Object} [settings] - предваритиельные настройки
*/
window.note = function(settings) {

  /**
  * Настройки по умолчанию
  */
  settings = Object.assign({},{
    callback:    false,
    content:     "",
    time:        4.5,
    type:        "info"
  }, settings);

  if(!settings.content.length) return;

  /**
  * Функция создания элементов
  * @param {String} name - название DOM-элемента
  * @param {Object} attr - объект с атрибутами
  * @param {Object} append - DOM-элемент, в который будет добавлен новый узел
  * @param {String} [content] - контент DOM-элемента
  */
  var create = function(name, attr, append, content) {
    var node = d.createElement(name);

     for(var val in attr) { 
      if(attr.hasOwnProperty(val)) node.setAttribute(val, attr[val]); 
    }

     if(content) node.insertAdjacentHTML("afterbegin", content);
     
     append.appendChild(node);
     
     if(node.classList.contains("note-item-hidden")) node.classList.remove("note-item-hidden");
     
     return node;
  };

  /**
  * Генерация элементов
  */
  var noteBox = d.getElementById("notes") || create("div", { "id": "notes" }, d.body);
  
  var noteItem = create("div", {
      "class": "note-item",
      "data-show": "false",
      "role": "alert",
      "data-type": settings.type
  }, noteBox),
    noteItemText = create("div", { "class": "note-item-text" }, noteItem, settings.content),
    noteItemBtn = create("button", {
      "class": "note-item-btn",
      "type": "button",
      "aria-label": "Скрыть"
    }, noteItem);

  /**
  * Функция проверки видимости алерта во viewport
  * @returns {boolean}
  */
  var isVisible = function() {

    var coords = noteItem.getBoundingClientRect();

    return (
      coords.top >= 0 &&
      coords.left >= 0 &&
      coords.bottom <= (window.innerHeight || d.documentElement.clientHeight) && 
      coords.right <= (window.innerWidth || d.documentElement.clientWidth) 
    );
  };
      
  /**
  * Функция удаления алертов
  * @param {Object} [el] - удаляемый алерт
  */
  var remove = function(el) {
    el = noteItem;
    el.setAttribute("data-show","false");

    window.setTimeout(function() {
      el.remove();
    }, 250);

    if(settings.callback) settings.callback(); // callback
  };

  /**
  * Удаление алерта по клику на кнопку
  */
  noteItemBtn.addEventListener("click", function() { remove(); });

  /**
  * Визуальный вывод алерта
  */
  window.setTimeout(function() {
    noteItem.setAttribute("data-show","true");
  }, 250);


  /**
  * Проверка видимости алерта и очистка места при необходимости
  */
  if(!isVisible()) remove(noteBox.firstChild);

  /**
  * Автоматическое удаление алерта спустя заданное время
  */
  window.setTimeout(remove, settings.time * 1000);
}

function token(){
    return $.ajax({
      headers:{
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
        url:'http://localhost:8080/api/auth/login',
        type: 'POST',
        dataType:'json',
        data: '{"username":"tenant@thingsboard.org", "password":"tenant"}',
    });
}

$TOKEN = token();

function show_alarm(){

  $TOKEN.done(function (token_data) {

  	var ids = ["e48d1be0-1f80-11eb-baed-6de80ac85462","c2fd0990-1f80-11eb-baed-6de80ac85462", "096d6aa0-1f81-11eb-baed-6de80ac85462", "26ecafa0-1f81-11eb-baed-6de80ac85462", "3eaa6a10-1f81-11eb-baed-6de80ac85462","58a1c0d0-1f81-11eb-baed-6de80ac85462", "741d94b0-1f81-11eb-baed-6de80ac85462", "8b4cf1d0-1f81-11eb-baed-6de80ac85462", "a1ddec10-1f81-11eb-baed-6de80ac85462", "bd8cdde0-1f81-11eb-baed-6de80ac85462"];
  	
  	var urls = ids.map(item=>'http://localhost:8080/api/plugins/telemetry/DEVICE/'+item+'/values/timeseries'); 

  	$.each(urls, function(i,u){
  		$.ajax(u, {
  			headers: {
  				'Accept': 'application/json',
  				'X-Authorization': 'Bearer '+token_data.token},
        type: 'GET',
  			dataType: 'json',
  			success: function(data) {
  				var id = data['id'][0]['value'];
  				for (key in data){

  				 	if (key != 'id' && key != 'name'){
  				 			value = data[key][0]['value'];
  					}
  				}

  				if (value == '1'){
  					note({
  			    		content: 'Внимание! Пожар на контейнере #'+id,
  			    		type: 'error',
  			    		time: 9
  			  	});
  				}
  			}  
  		});
    });	
  });
}


$(document).ready(function(){
	show_alarm();  
  setInterval('show_alarm()',8000); 
  token();
  setInterval('token()',30000);
});

