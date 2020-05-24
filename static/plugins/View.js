import {Utils} from './Utils.js';


document.addEventListener("DOMContentLoaded", function(event) { 

	let commentPlace = document.getElementById('comments');
	Utils.makeRequest('GET', 'http://' + window.location.host + '/api' + window.location.pathname + '/comments', function(data) {
		let comment_key;

	    for (let key in data){
	    	comment_key = key;

	    	let comment_info = data[comment_key]

			let div = document.createElement('div')

			let h5 = document.createElement('h5')
			let user_name = document.createTextNode(comment_info.user.first_name + ' ' + comment_info.user.last_name);
	    	let comment_text = document.createTextNode(comment_info.text);

	    	h5.append(user_name)
			div.append(h5);
	    	div.append(comment_text);

			commentPlace.append(div);
	    }

	});
});
