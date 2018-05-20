
initialize();

function initialize() {
	var element = document.getElementById('sets_button');
	if (element) {
		element.onclick = onSetsButtonClicked;
	}
    var element = document.getElementById('results_table');
    if(element) {
        getSets();
    }
    element = document.getElementById('artists_table');
    if (element) {
        getArtists();
    }
    element = document.getElementById('random_table');
    if (element){
        getRandom();
    }

}

function getBaseURL() {
	var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
	return baseURL;
}

function onSetsButtonClicked(){

    var url = getBaseURL() + '/sets';

	fetch(url, {method: 'get'})

	.then((response) => response.json())

	.then(function(setsList) {

        // Build the table body.
        var tableBody = '';

        tableBody = '<th> Name </th>';
        tableBody += '<th> Release Date </th>';
        tableBody += '<th> Border </th>';

        for (var k = 0; k < setsList.length; k++) {

            tableBody += '<tr>';

            tableBody += '<td>' +setsList[k]['name'];
            tableBody += '<td>' +setsList[k]['releaseDate'];
            tableBody += '<td>' +setsList[k]['border'];
            tableBody += '</td>';
            tableBody += '</tr>';
        }

        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('results_table');

        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }

        var displayValue = resultsTableElement.style.display;

    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function getSets() {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.
    var url = getBaseURL() + '/sets';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(setsList) {
        var tableBody = '<th> ID </th>';
        tableBody+= '<th> Name </th>';
        tableBody += '<th> Release Date </th>';
        tableBody += '<th> Border </th>';
        for (var k = 0; k < setsList.length; k++) {
            tableBody += '<tr>';
            tableBody += '<td>' + setsList[k]['id'] + '</td>';
            tableBody += '<td>' + setsList[k]['name'] + '</td>';
            tableBody += '<td>' + setsList[k]['releaseDate'] + '</td>';
			tableBody += '<td>' + setsList[k]['border'] + '</td>';
            tableBody += '</tr>';
        }
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

function getArtists() {

    var url = getBaseURL() + '/artists';
    fetch(url, {method: 'get'})
    .then((response) => response.json())

    .then(function(artistsList) {
        var tableBody = '<th> Artist ID </th>';
        tableBody += '<th> Name </th>';

        for(var i = 0; i < artistsList.length; i++) {
            tableBody += '<tr>';
            tableBody += '<td>' + artistsList[i]['artist_id'] + '</td>';
            tableBody += '<td>' + artistsList[i]['name'] + '</td>';
            tableBody += '</tr>';
        }
        var artistTable = document.getElementById('artists_table');
        if (artistTable) {
            artistTable.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}
function getRandom() {
    var url = getBaseURL() + '/random';
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(card){
        var tableBody = '<tr>' + '<td>' + 'Name' + '</td>' + '<td>' +card['name'] + '</td>' + '</tr>';
        tableBody += '<tr>' + '<td>' + 'Colors' + '</td>' + '<td>' + card['colors'] + '</td>' + '</tr>';
        tableBody += '<tr>' + '<td>' + 'Color Identity' + '</td>' + '<td>' + card['colorIdentity'] + '</td>' +  '</tr>';
        tableBody += '<tr>' + '<td>' + 'Manacost' + '</td>' + '<td>' +  card['manaCost'] + '</td>' + '</tr>';
        tableBody += '<tr>' + '<td>' + 'CMC' + '</td>' + '<td>' + card['cmc'] + '</td>' + '</tr>';
        tableBody += '<tr>' + '<td>' + 'Type' + '</td>' + '<td>' + card['type'] + '</td>' + '</tr>';
        tableBody += '<tr>' + '<td>' + 'Types' + '</td>' +'<td>'+ card['types'] + '</td>' + '</tr>';
        tableBody += '<tr>' + '<td>' + 'Subtypes' + '</td>' + '<td>' + card['subtypes'] + '</td>' + '</tr>';
        tableBody+= '<tr>' + '<td>' + 'Text' + '</td>' + '<td>' + card['text'] + '</td>' + '</tr>';
        tableBody+= '<tr>' + '<td>' + 'Power' + '</td>' + '<td>' + card['power'] + '</td>' + '</tr>';
        tableBody+= '<tr>' + '<td>' + 'Toughness' + '</td>' + '<td>' + card['toughness'] + '</td>' + '</tr>';
        tableBody+= '<tr>' + '<td>' + 'Flavor Text' + '</td>' + '<td>' + card['flavor'] + '</td>' + '</tr>';
        tableBody += '<tr>' + '<td>' + 'Artist' + '</td>' + '<td>' + card['artist'] + '</td>' + '</tr>';
        var randomTable = document.getElementById('random_table');
        if(randomTable){
            randomTable.innerHTML = tableBody;
        }
    })
    .catch(function(error){
        console.log(error);
    });
}

function getCard() {

    var searchname = document.getElementById('search');
    var x = searchname.elements[0].value;

    var url = getBaseURL() + '/cards?name=' + x;

    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(cards){

				for( var i = 0; i < cards.length; i++){
						if(x == cards[i]['name']){
						var tableBody = '<tr>' + '<td>' + 'Name' + '</td>' + '<td>' +cards[i]['name'] + '</td>' + '</tr>';
						tableBody += '<tr>' + '<td>' + 'Colors' + '</td>' + '<td>' + cards[i]['colors'] + '</td>' + '</tr>';
						tableBody += '<tr>' + '<td>' + 'Color Identity' + '</td>' + '<td>' + cards[i]['colorIdentity'] + '</td>' +  '</tr>';
						tableBody += '<tr>' + '<td>' + 'Manacost' + '</td>' + '<td>' +  cards[i]['manaCost'] + '</td>' + '</tr>';
						tableBody += '<tr>' + '<td>' + 'CMC' + '</td>' + '<td>' + cards[i]['cmc'] + '</td>' + '</tr>';
						tableBody += '<tr>' + '<td>' + 'Type' + '</td>' + '<td>' + cards[i]['type'] + '</td>' + '</tr>';
						tableBody += '<tr>' + '<td>' + 'Types' + '</td>' +'<td>'+ cards[i]['types'] + '</td>' + '</tr>';
						tableBody += '<tr>' + '<td>' + 'Subtypes' + '</td>' + '<td>' + cards[i]['subtypes'] + '</td>' + '</tr>';
						tableBody+= '<tr>' + '<td>' + 'Text' + '</td>' + '<td>' + cards[i]['text'] + '</td>' + '</tr>';
						tableBody+= '<tr>' + '<td>' + 'Power' + '</td>' + '<td>' + cards[i]['power'] + '</td>' + '</tr>';
						tableBody+= '<tr>' + '<td>' + 'Toughness' + '</td>' + '<td>' + cards[i]['toughness'] + '</td>' + '</tr>';
						tableBody+= '<tr>' + '<td>' + 'Flavor Text' + '</td>' + '<td>' + cards[i]['flavor'] + '</td>' + '</tr>';
						tableBody += '<tr>' + '<td>' + 'Artist' + '</td>' + '<td>' + cards[i]['artist'] + '</td>' + '</tr>';
					}
				}

        var cardTable = document.getElementById('card_table');
        if(cardTable){
            cardTable.innerHTML = tableBody;
        }
    })
    .catch(function(error){
        console.log(error);
    });
}

