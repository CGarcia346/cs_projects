
initialize();

function initialize() {
	var element = document.getElementById('sets_button');
	if (element) {
		element.onclick = onSetsButtonClicked;
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

        for (var k = 0; k < setsList.length; k++) {

            tableBody += '<tr>';
            tableBody += '<td>' +setsList[k]['id'];
            tableBody += '<td>' +setsList[k]['name'];
            tableBody += '<td>' +setsList[k]['releaseDate'];
            tableBody += '<td>' +setsList[k]['border'];
            tableBody += '</td>';
            tableBody += '</tr>';
        }

        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('results_table');
				var displayValue = table.style.display;

				if (displayValue == 'none') {
						table.style.display = 'block';
				} else{
						table.style.display = 'none';
				}

        //if (resultsTableElement) {
          //  resultsTableElement.innerHTML = tableBody;
        //}
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
        var tableBody = '<tr><th>' + setsList + '</th></tr>';
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
