var cityInputs = document.querySelector('.cityInputs');

function buildCityInputForm(numberOfCities) {
    var html = "";
    html += `<form action="/city_info" method="POST" >` + `<ol>`
    for (var i = 0; i < numberOfCities; i++) {
            html += `<li>` +
            `<p>` +
            `<input type="text" name="${i}" id="${i}">` +
            `</p>` +
            `</li>` 
        }
    html += `</ol>`+ `<input type="submit"  value="submit" id="submitCities">` + '</form>' + '</div>';
    cityInputs.innerHTML = html;  //injects the html into the div section
    }

document.getElementById("createCityInputs").onclick = function () { 
    numberOfCities = document.getElementById("numberOfCities").value
    if (numberOfCities > 0 && numberOfCities< 21){
        buildCityInputForm(document.getElementById("numberOfCities").value)
    } else{
        alert("please enter a number from 1 to 20")
    }    
}


