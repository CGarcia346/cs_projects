
initialize();

function initialize() {

    var url = window.location.href;
    var path = url.substring(url.indexOf('?'));
    url = getBaseURL() + '/cards' + path;

    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(cards){

	    var tableBody = '<tr><td>Name</td><td>' + cards[0]['name'] + '</td></tr>';
        tableBody += '<tr><td>Set</td><td>' + cards[0]['set_id'] + '</td></tr>';
        tableBody += '<tr><td>Colors</td><td>' + cards[0]['colors'] + '</td></tr>';
        tableBody += '<tr><td>Color Identity</td><td>' + cards[0]['colorIdentity'] + '</td></tr>';
        tableBody += '<tr><td>Manacost</td><td>' + cards[0]['manaCost'] + '</td></tr>';
        tableBody += '<tr><td>CMC</td><td>' + cards[0]['cmc'] + '</td></tr>';
        tableBody += '<tr><td>Type</td><td>' + cards[0]['type'] + '</td></tr>';
        tableBody += '<tr><td>Types</td><td>' + cards[0]['types'] + '</td></tr>';
        tableBody += '<tr><td>Subtypes</td><td>' + cards[0]['subtypes'] + '</td></tr>';
        tableBody += '<tr><td>Text</td><td>' + cards[0]['text'] + '</td></tr>';
        tableBody += '<tr><td>Power</td><td>' + cards[0]['power'] + '</td></tr>';
        tableBody += '<tr><td>Toughness</td><td>' + cards[0]['toughness'] + '</td></tr>';
        tableBody += '<tr><td>Flavor Text</td><td>' + cards[0]['flavor'] + '</td></tr>';
    	tableBody += '<tr><td>Artist</td><td>' + cards[0]['artist'] + '</td></tr>';

        var cardTable = document.getElementById('card_table')
        if(cardTable){
            cardTable.innerHTML = tableBody
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
