initialize();

function initialize() {
	var element = document.getElementById('sets_button');
	if (element) {
		element.onclick = onSetsButtonClicked;
	}
}

function getBaseURL() {
	var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
	return baseURL
}

function onSetsButtonClicked(){
	var url = getBaseURL() + '/sets/';

	fetch(url, {method, 'get'})

	.then((response) => response.json())
	
	
