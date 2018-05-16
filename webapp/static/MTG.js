
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

