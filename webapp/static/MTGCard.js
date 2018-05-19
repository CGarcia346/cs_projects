
initialize();

function initialize() {

    var url = new URL(window.location.href);
    var searchText = url.searchParams.get('name');
    var searchname = document.getElementById('search');
    var url = getBaseURL() + '/cards?name=' + searchText;
    var setName = getBaseURL() + '/sets'
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(cards){

    fetch(setName, {method: 'get'})
    var setList() = .then((response) => response.json())

    var tableBody = '<th>' + 'Set' + '</th>'
    tableBody += '<th>' + 'Card Name' + '</th>'
    tableBody += '<th>' + 'Artist' + '</th>'


				for( var i = 0; i < cards.length; i++){
						var tableBody += '<tr>';
						var setID = cards[i]['set_id']
            setName = setList[setID]
            tableBody += '<td>' + setName + '</td>';
						tableBody += '<td>' +cards[i]['name'] + '</td>';
            tableBody += '<td>' +cards[i]['Artist'] + '</td>';
						tableBody += '</tr>';
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
