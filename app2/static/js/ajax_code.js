var messagebox = document.getElementById("message_to_insert");
var xmlhttp;

function send_message_to_db(){
				// get message from text box
				var message = messagebox.value;
				
				dict_to_send = {"message_to_insert" : message}
				json_string = JSON.stringify(dict_to_send);
				// send to database

				if (window.XMLHttpRequest){
								xmlhttp = new XMLHttpRequest();
				} else {
								xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
				}
				
				xmlhttp.onreadystatechange=function(){
								console.log("state=="+xmlhttp.readyState+" , status=="+xmlhttp.status);
								if (xmlhttp.readyState==4 && xmlhttp.status==200){
												messagebox.value="";
												console.log("xmlhttp.response == "+xmlhttp.responseText)
								}
				}

				xmlhttp.open("POST", "/data", true);
				xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
				xmlhttp.send(json_string);
}

function get_messages(){
				if (window.XMLHttpRequest){
								xmlhttp = new XMLHttpRequest();
				} else {
								xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
				}
				
				xmlhttp.onreadystatechange=function(){
								console.log("state=="+xmlhttp.readyState+" , status=="+xmlhttp.status);
								if (xmlhttp.readyState==4 && xmlhttp.status==200){
												console.log("xmlhttp.response == "+xmlhttp.responseText)
												add_messages(xmlhttp.responseText)
								}
				}

				xmlhttp.open("POST", "/get_data", true);
				xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
				xmlhttp.send();
}

function add_messages(responseText){
				responseData = JSON.parse(responseText);
				messages = responseData['messages'];
				console.log(messages)
}
