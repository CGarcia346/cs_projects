
initialize();

function initialize() {

    var url = window.location.href;
    var path = url.substring(url.indexOf('?'));
    url = getBaseURL() + '/artists' + path;
    console.log(url);
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(artist){

	    var tableBody = '<tr><td>Name</td><td>' + artist[0]['name'] + '</td></tr>';
        tableBody += '<tr><td>Sets</td><td>' + artist[0]['sets'] + '</td></tr>';
    	tableBody += '<tr><td>Cards</td><td>' + artist[0]['cards'] + '</td></tr>';

        var artistTable = document.getElementById('artist_table')
        if(artistTable){
            artistTable.innerHTML = tableBody
        }
    })
    .catch(function(error){
        console.log(error);
    });
}

function getBaseURL() {
	var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
	return baseURL;
}
