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


function show(){

	$TOKEN.done(function (token_data) {

		var ids = ["1e4aa4f0-1f82-11eb-baed-6de80ac85462", "3d35d600-1f82-11eb-baed-6de80ac85462","60cf4ce0-1f82-11eb-baed-6de80ac85462", "7fe892d0-1f82-11eb-baed-6de80ac85462", "b8f69770-1f82-11eb-baed-6de80ac85462", "e7fc6720-1f82-11eb-baed-6de80ac85462", "03316e00-1f83-11eb-baed-6de80ac85462", "1b883420-1f83-11eb-baed-6de80ac85462", "32e07600-1f83-11eb-baed-6de80ac85462", "4973ba30-1f83-11eb-baed-6de80ac85462","7c8c5300-1f83-11eb-baed-6de80ac85462", "b9848a20-1f83-11eb-baed-6de80ac85462", "e8b93200-1f83-11eb-baed-6de80ac85462", "1248d800-1f84-11eb-baed-6de80ac85462", "33001680-1f84-11eb-baed-6de80ac85462", "506061d0-1f84-11eb-baed-6de80ac85462", "5cede210-1f84-11eb-baed-6de80ac85462","845ec6c0-1f84-11eb-baed-6de80ac85462", "9e3723d0-1f84-11eb-baed-6de80ac85462", "c0e30660-1f84-11eb-baed-6de80ac85462"];

		var urls = ids.map(item=>'http://localhost:8080/api/plugins/telemetry/DEVICE/'+item+'/values/timeseries');

		$.each(urls, function(i,u){
			$.ajax(u, {
				headers: {
					'Accept': 'application/json',
					'X-Authorization': 'Bearer '+token_data.token
				},
				type: 'GET',
				dataType: 'json',
				success: function(data){
				 	var id, name, value;

				 	id = data['id'][0]['value'];
				 	name = data['name'][0]['value'];
				 	// value = data[2][0]['value'];

				 	for (key in data){

					 	if (key != 'id' && key != 'name'){
					 			value = data[key][0]['value'];
						}
					}

				 	if (name == "Destination"){
				 		$('#'+id+'.dest').html(value);
				 	}

				 	if (name == "Cap"){
				 		if (value == '1'){
				 			$("td[id_num="+id+"]").html('Открыт').css({'text-weight':'bold', 'color':'green'});
				 		}else{
				 			$("td[id_num="+id+"]").html('Закрыт').css({'text-weight':'bold', 'color':'red'});
				 		}
				 	}
				}
			});
		});
	});
}

$(document).ready(function(){
	 show();  
	 token();
     setInterval('show()',8000); 
     setInterval('token()',30000); 
});