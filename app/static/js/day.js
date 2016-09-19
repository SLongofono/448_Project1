
/*
@file day.js
@brief Code to control the client-side behavior of the day view
@author Stephen Longofono
@details
This file describes the logic, helper methods, and server interaction methods for
the day view.  It is used alongside the day.html template to implement the day view.
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
					failMessage('We\'re experiencing difficulties processing your request.  Please try again later.');
					console.log('Bad status: ');
					console.log(payload);
				}
			}
		});// End ajax
	});
});


/*
@fn Button_Handler_Details
@brief Button handler for details
@param [in] button The detail button which triggered this JQuery event
@param [out] return void
@details
This function is responsible for identifying changes in a detail and its associated
set of buttons and reacting accordingly.  If the button pressed was the 'Edit'
button, the input field is displayed along with the 'Save' button.  If the 'Save'
button was pressed, the input is stored in the local copy of the day's details and
also sent to the server to be changed permenantly.  If the 'Delete' button was
pressed, the detail is deleted locally, and a message is sent to the server to remove
it permenantly.

This button handler is different from the other button handlers in that it
will be interacting with dynamically created DOM elements.  For some
arcane reason, dynamically created items will not be selectable unless
the 'on' function is used.  Hooray.
*/
$(function(){
	$("#detailWrapper").on('click', "[value]", function(){
		console.log('Clicked a button with number ' + $(this).attr("num"));
		var div_pattern = "#detailDiv" + $(this).attr("num")
		var delete_btn = $(div_pattern).find('#delete')
		var edit_btn = $(div_pattern).find('#edit')
		var save_btn = $(div_pattern).find('#save')
		var input_btn = $(div_pattern).find('#input')
		var orig_detail = $(div_pattern).find('li')

		// Case delete button
		// TODO verify that this is working correctly, or switch to delete fcn
		if($(this).attr("id") == "delete"){
			// Update the local day object
			modifyDetail(currentDay, $(this).attr("data"), "", true);

			// Send changes to server
			saveChanges(currentDay);

			// Delete the div and its contents completely
			$(div_pattern).remove()

			// Update global detail count
			detailCount -= 1;
		}

		//Case edit button
		else if($(this).attr("id") == "edit"){
			// Find the input field and save button for this and make visible
			input_btn.css('visibility', 'visible')
			save_btn.css('visibility', 'visible')
		}

		//Case Save button
		else if($(this).attr("id") == "save"){

			// Fetch new detail for this detail id number
			var newDetail = sanitize(input_btn.val());

			// Verify that there is in fact a new detail before making changes
			if (newDetail.length <= 0){
				failMessage('No valid detail text.  Use the delete button to remove a detail');
				input_btn.val($(this).attr("data"));
				return;
			}

			console.log("Saving new detail " + newDetail + " over old detail " + $(this).attr('data'));

			// Update the local day object
			modifyDetail(currentDay, $(this).attr("data"), newDetail, false);

			// Update all of this detail's buttons with the new detail text
			$(div_pattern).find('*').attr("data", newDetail);

			// Update original template value
			orig_detail.text(newDetail);

			// Hide the input and save button again
			input_btn.css('visibility', 'hidden')
			save_btn.css('visibility', 'hidden')

			// Send changes to server
			saveChanges(currentDay);
		}
		return;
	});
});


/*
@fn Button_Handler_Add_Detail
@brief Button handler for add detail
@param [in] button The 'Add Detail' button which triggered this JQuery event
@param [out] return void
@details
This function creates a new local detail with default values, and adds an
HTML element and buttons to display and interact with it.  The change is not
permanent unless the user edits the detail and saves it via the 'Edit' and 'Save'
buttons generated by this method
*/
$(function(){
	$('#addDetailSection').find('*').click(function(){
		var detailDiv = $('#detailWrapper');

		// The template engine counts starting at 1, which is not so great in
		// this context
		var idNum = detailCount + 1;

		// Build HTML buttons for a new detail
		var newDetailSetup = buildDetail(idNum);

		// Tack it onto the end of the detailDiv
		$('#detailWrapper').append(newDetailSetup);

		detailCount += 1;
		console.log(detailCount);
	});
});


/*
@fn buildDetail
@brief Assembles HTML for new detail fields and buttons
@param [in] num The number which will identify this detail uniquely wrt other details (ascending list of integers)
@param [out] return A string representing an detail in HTML, including Div, Button, and Input elements
@details
This is a super-dumb function which makes number sandwiches.
*/
function buildDetail(num){
	var p1  = '<div id="detailDiv'
	var p2  = '"><li>New</li><br><button class="btn" type="button" id="delete" num="'
	var p3  = '"data="New" value="Delete">Delete</button><button class="btn" type="button" id="edit"   num="'
	var p4  = '" data="New" value="Edit">Edit</button><input  type="text" style="visibility:hidden" id="input" num="'
	var p5  = '" data="New" value="New"></input><button class="btn" type="button" style="visibility:hidden" id="save" num="'
	var p6 = '" data="New" value="Save">Save</button></div>'

	return p1 + num + p2 + num + p3 + num + p4 + num + p5 + num + p6;
}

/*
@fn modifyDetail
@brief Modify existing details
@param [in] day The local day object to be modified
@param [in] oldDetail A string representing the old value for the detail to be modified
@param [in] newDetail A string representing the new value for the detail to be modified
@param [in] deleteFlag A boolean indicating whether or not the modification is a deletion
@param [out] return void
@details
This method is used to add, modify, or delete a detail string in the given day object.
This method assumes that the day's stats and labels lists are aligned with one another.
*/
function modifyDetail(day, oldDetail, newDetail, deleteFlag){
	console.log('Params: old detail: ' + oldDetail);
	console.log('New detail: ' + newDetail);
	if(day.stats.length > 4){
		var done = false;
		// Locate detail
		// start at index 4 so expected values are never changed
		for(var i = 4; i<day.stats.length; i++){
			// If the detail exists...
			if (day.stats[i] == oldDetail){
				console.log('Match:');
				console.log( newDetail + ' matches existing detail ' + day.stats[i]);
				if(deleteFlag){
					console.log('Removing detail: ' + oldDetail);
					// Remove the detail and the corresponding label
					console.log('Removing element ' + i + ', ' + day.stats[i]);
					console.log(day.stats);
					day.stats.splice(i,1);
					day.labels.splice(i,1);
					console.log('done');
					console.log(day.stats);
				}
				else{
					// Replace the value.  Leave the label unchanged.
					console.log("Changing detail");
					day.stats[i] = newDetail;
					console.log("Detail changed to " + newDetail);
					console.log(day.stats);
				}
				done = true;
				break;
			}
		} //end for
		if(!done){
			// This is a new detail
			// Get the number of the last detail
			lastDetail = day.labels[day.labels.length-1];
			newNum = lastDetail.charAt(lastDetail.length-1);
			newNum++;
			day.stats.push(newDetail);
			day.labels.push('detail' + newNum);
			console.log(day.stats);
		}
	} //end if
	else{
		// This is the first detail
		day.stats.push(newDetail);
		day.labels.push('detail0');
	}
	return;
};


/*
@fn parseDate
@brief Apply a regular expression to pull a date from a given string
@param [in] str The String to be parsed
@details
This function applies a regular expression to pull matches in the form mm/dd/yyyy

The regular expression was built with help from a 2016 tutorial by Jan Goyvaerts
Accessed September 2016
https://www.regular-expressions.info/dates.html
*/
function parseDate(str){
	// match 19** or 20**   			'^(19|20)\\d\\d'
	// match 0* or 10,11,12 			'^(0[1-9]|1[012])'
	// match 0* or 1* or 2* or 30,31 	'^(0[1-9]|[12][0-9]|3[01])'
	// match delimiters '-' or '/'		'[-/]'

	//line up with beginning of input, and find the patterns below
	var date = str.match('^(0[1-9]|1[012])[-/](0[1-9]|[12][0-9]|3[01])[-/](19|20)\\d\\d');
	if(date !== 'undefined' && date != null){
		result = Array();
		result.push(date[0].substring(3,5));
		result.push(date[0].substring(0,2));
		result.push(date[0].substring(6,10));
		console.log('Returning result: ');
		console.log(result);
		return result;
	}
	return date;
}


/*
@fn Button_Handler_Jump
@brief Button handler for jump to day
@param [in] button The 'jump' button which triggered this JQuery event
@param [out] return displays an error message on failure.  Otherwise, redirects
					to the link provided by the server.
@details
This function prepares a JSON request for an AJAX call to the server, indicating
that the view should be changed to the day described by the associated input field
'jumpInput'.  It sets up callbacks for successfull or failed communication, and uses
the failMessage function to communicate with the user if necessary.
*/
$(function(){
	$('#jump').click(function(){
		console.log($('#jumpInput').val());
		var date = parseDate($('#jumpInput').val());

		if(date !== 'undefined' && date != null){
			var data = serialize(['day','month','year'], date);
			console.log(data);
			$.ajax({
				url: 	 '/changeFocusDay',
				data:    data,
				type: 	 'POST',
				success: function(reply){
					// Once the server has confirmed a change, redirect
					// Parse the JSON into an object
					payload = JSON.parse(reply);
					if (payload.status == 'OK'){
						// redirect, cueing the server to display the updated day view
						window.location.replace(payload.link);
					}
					else{
						failMessage('We\'re experiencing difficulties processing your request.  Please check that your date is in the format mm/dd/yyyy and that it falls within the academic year.');
						console.log('Bad status: ');
						console.log(payload);
					}
				}
			});// End ajax
		} // end if defined
	});
});


/*
@fn saveChanges(currentDay)
@brief Sends new details to the server to be committed to the logfile/database
@param [in] currentDay the local day object for this view's day
@param [out] return void.  Displays an error message on failure or a success message on succecss.
@details
This function prepares a JSON request for an AJAX call to the server, indicating
that the details for the day described by currentDay are to be replaced with those in
the prepared JSON.  Callbacks are assigned to handle the server resonse and communicate
status to the user.
*/
function saveChanges(currentDay){
	// Send out an ajax call and assign callbacks to the reply
	console.log(serialize(currentDay.labels, currentDay.stats));
	$.ajax({
		url: 	 '/process',
		data:    serialize(currentDay.labels, currentDay.stats), // Faking a form
		type: 	 'POST',
		success: function(reply){
					payload = JSON.parse(reply)
					console.log(reply);
					if(reply.status == 'BAD'){
						failMessage('Failed to communicate with the server, please try again later.');
					}
					else{
						successMessage('Your changes were saved!');
						console.log('OK');
					}
				 },
		error: 	 function(reply){
					console.log(reply);
					failMessage('Failed to communicate with the server, please try again later.');
				 }
	});// End ajax
}; // End saveChanges


/*
@fn sanitize(word)
@brief Removes slashes, ampersands, percent signs, dollar signs, and hashtags from the given string
@param [in] word The string to be stripped of unwanted characters
@param [out] result The modified string
@details
This function strips out certain punctuation from strings provided by the user.  If this is already
built into Javascript, it isn't obvious or readily found on the internet.  We got it from
a StackExchange post by user 'Arun P Johny'.

Retrieved September 2016
http://stackoverflow.com/questions/16171320/remove-all-slashes-in-javascript#16171353
*/
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
};


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
	delimiter = '&';
	result = Array();
	for(var i = 0; i < vals.length; i++){
		result.push(names[i] + '=' + vals[i].replace(' ', '_'))
	}
	return result.join(delimiter)
};


/*
@fn failMessage(msg)
@brief Displays a message to the user in a designated HTML element
@param [in] msg The string to be displayed
@details
This function is a means of providing feedback to the user through a HTML element.
It uses red text to indicate BAD.
*/
function failMessage(msg){
	$('#comsField').css('color', 'red');
	$('#comsField').text(msg);
};


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
};
