/*
@file week.js
@brief Code to control the client-side behavior of the week view
@author Stephen Wiss
@details
This file describes the logic, helper methods, and server interaction methods for
the week view.  It is used alongside the week.html template to implement the week view.
*/


/*
@fn Button_Handler_Views
@brief Button handler for views
@param [in] button The View change button which triggered this JQuery event
@param [out] return redirects to the link provided by the server, or prepares
					feedback for the user with the failMessage() method.
@details
The viewchange function is responsible for assembling a JSON for the server, indicating
a request to change to view to the view string stored in view change buttons in the HTML
above.  The function uses AJAX and assigns two callbacks to handle the server responses.
*/

$(function(){
	$('#viewChange').find('*').click(function(){
		console.log($(this).attr('id'));
		var payload = 'view=' + $(this).attr("id");
		$.ajax({
			url: 	 '/viewChange',
			data:    payload,
			type: 	 'POST',
			success: function(reply){
				// Once the server has confirmed a change, redirect
				// Parse the JSON into an object
				payload = JSON.parse(reply);
				if (payload.status == 'OK'){
					console.log("Changed view successfully");
					// redirect, cueing the server to display the updated view
					window.location.replace(payload.link);
					//window.location.replace("http://localhost:5000/");
				}
				else{
					console.log('Bad status:');
					console.log(payload);
				}
			}
		});// End ajax
	});
});

/*
@fn Button_Handler_Week_Days
@brief Button handler for days displayed in this month
@param [in] button The day button which triggered this JQuery event
@param [out] return redirects to the link provided by the server, or prepares
					feedback for the user with the failMessage() method.
@details
This function prepares a JSON request for an AJAX call to the server, indicating
that the view should be changed to the day described by the button that initiated the
JQuery event.  It sets up callbacks for successfull or failed communication, and uses
the failMessage function to communicate with the user if necessary.
*/

$(function(){
	$('#daysDiv').find('*').click(function(){
		var payload = serialize(['day', 'month','year'], [$(this).val(), (months.indexOf(month) + 1),year]); //'view=' + $(this).attr("id");
		$.ajax({
			url: 	 '/changeFocusDay',
			data:    payload,
			type: 	 'POST',
			success: function(reply){
				// Once the server has confirmed a change, redirect
				// Parse the JSON into an object
				payload = JSON.parse(reply);
				if (payload.status == 'OK'){
					console.log("Changed view successfully");
					// redirect, cueing the server to display the updated view
					window.location.replace(payload.link);
					//window.location.replace("http://localhost:5000/");
				}
				else{
					console.log('Bad status:');
					console.log(payload);
				}
			}
		});// End ajax
	});
});

function failMessage(msg){
	$('#comsField').css('color', 'red');
	$('#comsField').text(msg);
}

// This function was taken from a stackexchange post, which is kind of
// ridiculous considering JavaScript is a web language.  It should be built in..
// Retrieved September 2016
// http://stackoverflow.com/questions/16171320/remove-all-slashes-in-javascript#16171353
function sanitize(word){
	console.log(word);
	result = word.replace(/\\/g, '');
	result = result.replace(/\/\//g, '');
	result = result.replace(/\&/g, '');
	result = result.replace(/%/g, '');
	result = result.replace(/\$/g, '');
	result = result.replace(/#/g, '');
	console.log(result);
	return result;
}
/*
@fn serialize(word)
@brief Zips two lists together, JSON style
@param [in] names The list of String keys for the JSON
@param [in] vals The list of String values for the JSON
@param [out] result The modified string representing a JSON form
@details
This function is used to fake HTML form input because HTML forms are awful and we hate them.
*/
function serialize(names,vals){
	equals = '=';
	delimiter = '&';
	result = Array();
	for(var i = 0; i < vals.length; i++){
		result.push(names[i] + equals + vals[i])
	}
	return result.join(delimiter)
}
/*
@fn successMessage(msg)
@brief Displays a message to the user in a designated HTML element
@param [in] msg The string to be displayed
@details
This function is a means of providing feedback to the user through a HTML element.
It uses green text to indicate GOOD.
*/
function successMessage(msg){
	$('#comsField').css('color', 'green');
	$('#comsField').text(msg);
}
