import {Utils} from './Utils.js';

$(".five li ul").hide(); // скрываем выпадающее меню
$(".five li:has('.submenu')").hover(
  function(){
  $(".five li ul").stop().fadeToggle(300);} /* отбираем элемент списка, который содержит элемент с классом .submenu и добавляем ему функцию при наведении, которая показывает и скрывает выпадающее меню */
);

document.addEventListener("DOMContentLoaded", function(event) {

	let placeComment = function() {

		let commentPlace = document.getElementById('comments');

		if (commentPlace) {
			Utils.makeRequest('GET', 'http://' + window.location.host + '/api' + window.location.pathname + '/comments', function (data) {
				let comment_key;

				for (let key in data) {
					comment_key = key;

					let comment_info = data[comment_key]

					let image = document.createElement('img')
					image.src = comment_info.user.image;
					image.height = 100;
					image.width = 100;

					let image_div = document.createElement('div')
					image_div.classList = 'comment_image'

					image_div.append(image)

					let div = document.createElement('div')
					div.classList = 'border rounded mb-2 p-3';

					let h5 = document.createElement('h5')

					let user_name = document.createTextNode(comment_info.user.first_name + ' ' + comment_info.user.last_name);
					let comment_text = document.createTextNode(comment_info.text);

					h5.append(user_name)
					div.append(image_div)
					div.append(h5);
					div.append(comment_text);

					commentPlace.append(div);
				}

			});
		}
	}

	placeComment();

	let placeSubMenu = function () {

		let subMenuPlace = document.getElementById('subMenu');

		if (subMenuPlace){
			Utils.makeRequest('GET', 'http://127.0.0.1:5000/api/categories/active_categories', function (data) {

				let subMenuKey;

				for (let key in data) {
					subMenuKey = key;

					let li = document.createElement('li');
					li.className = 'nav-item';
					let a =document.createElement('a');
					a.className = 'nav-link';
					a.href = data[subMenuKey]['url'];
					let span = document.createElement('span');
					span.className = 'nav-link-text';
					span.textContent = data[subMenuKey]['name'];

					a.append(span);
					li.append(a);
					subMenuPlace.append(li);

				}
		})}

	}

	placeSubMenu();

});
