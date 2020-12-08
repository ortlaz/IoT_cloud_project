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

// $TOKEN.done(function (data) {
//     console.log("Success!" + data);
// }).fail(function (e) {
//     console.log("Failure!" + e);      
// });



function show_warning(){

	$TOKEN.done(function (token_data) {

		var tokens = ["Yl5XT3RuokftknhlONoq", "cgRUEWTh08nLUUanC84B", "czYW66xyICSQMrnpIaz8", "7tPbHyDbbbYDeBHXKl17", "9Mk2rFyReqKRgpMVQPZi", "e9HsuZ7yW9gisUHnWBYD", "ZUFW8ejdwstFiHH9pkCU", "kLdSDTOYy8rkx7VHnXAz", "kViU0vw1kTdMPzTb4XU4", "zZXOBsmQM5AaAS342nHO"];
		
		var urls = tokens.map(item=>'http://localhost:8080/api/v1/'+item+'/attributes?clientKeys=clearTs&sharedKeys=id');

		$.each(urls, function(i,u){
			$.ajax(u, {
				headers: {
					'Accept': 'application/json',
					'X-Authorization':'Bearer '+token_data.token
				},
				type: 'GET',
				dataType: 'json',
				success: function(data){
				 	var id, value, clearTs;

				 	clearTs = data['client']['clearTs'];
				 	id = data['shared']['id'];

				 	if (clearTs != 0){
				 		$('#'+id+'.dest').css({'backgroundColor':'#73d964'});
				 	}else{
				 		$('#'+id+'.dest').css({'backgroundColor':'#ff7f50'});

				 	}

				},
			});
		});
	});

}

$(document).ready(function(){
	 show_warning();  
	 token();
     setInterval('show_warning()',8000);
     setInterval('token()',30000) 
});