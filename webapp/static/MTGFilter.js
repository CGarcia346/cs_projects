
initialize();

function initialize() {

    var url = new URL(window.location.href);
    var searchText = url.searchParams.get('name');
    var searchname = document.getElementById('search');
    var url = getBaseURL() + '/cards?name=' + searchText;

    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(cards){

				for( var i = 0; i < cards.length; i++){
						if(searchText == cards[i]['name']){
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

function getBaseURL() {
	var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
	return baseURL;
}
