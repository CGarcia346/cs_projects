
initialize();

function initialize() {

    var url = new URL(window.location.href);
    var searchText = url.searchParams.get('name');
    var searchname = document.getElementById('search');
    var url = getBaseURL() + '/cards?name=' + searchText;

    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(function(cards){

    var head = '<th>' + 'Set' + '</th>'
    head += '<th>' + 'Card Name' + '</th>'
    head += '<th>' + 'Artist' + '</th>'
    head += '<th>' + 'Text' + '</th>'
    head += '<th>' + 'Flavor Text' + '</th>'
    var tableBody = ""
    var subBody = ""
	var priority = ""
    for( var i = 0; i < cards.length; i++){
        var setid = cards[i]['set_id']
        var name = cards[i]['name']
        var artist = cards[i]['artist']
        var text = cards[i]['text']
        var flavor = cards[i]['flavor']
        var link = '<a href= /set/' +setid + '>' + setid + '</a>'
        var nameLink = '<a href=/card?name=' + name + '&set_id=' + setid + '>' + name + '</a>'
        var artistLink = '<a href=/artist/' + artist + '>' + artist + '</a>'

                if(searchText == name){
					tableBody += '<tr>'
                    tableBody += '<td>' + link + '</td>'
					tableBody += '<td>' + nameLink + '</td>'
                    tableBody += '<td>' + artistLink + '</td>'
                    tableBody += '<td>' + text + '</td>'
                    tableBody += '<td>' + flavor + '</td>'
					tableBody += '</tr>'
                }
                else{
                    
                    if(cards[i]['name'].startsWith(searchText)){
                        priority += '<tr>'
                        priority += '<td>' + link + '</td>'
                        priority += '<td>' + nameLink + '</td>'
                        priority += '<td>' + artistLink + '</td>'
                        priority += '<td>' + text + '</td>'
                        priority += '<td>' + flavor + '</tf>'
                        priority += '</tr>'
                    }
                    else{
                        subBody += '<tr>'
                        subBody += '<td>' + link +'</td>'
                        subBody += '<td>' + nameLink +'</td>'
                        subBody += '<td>' + artistLink + '</td>'
                        subBody += '<td>' + text + '</td>'
                        subBody += '<td>' + flavor + '</td>'
                        subBody += '</tr>'
                    }
                }
			}
        tableBody = head + tableBody + priority + subBody

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
