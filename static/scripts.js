var cityInputs = document.querySelector('.cityInputs');

// Dynamically builds the input boxes for the user to input cities
function buildCityInputForm(numberOfCities) {
    var html = `<form autocomplete="off"  action="/city_info" method="POST" >` + `<ol>`
    for (var i = 0; i < numberOfCities; i++) {
        html += `<li>` +
            `<p>` +
            `<input type="text" class="userInput ui-autocomplete-input" name="${i}" id="${i}"  placeholder="city, state" onfocus="showSuggestion()" autofocus autocomplete="off">` +
            `</p>` +
            `</li>`
    }
    html += `</ol>` + `<input type="submit"  value="submit" id="submitCities">` + '</form>' + '</div>';
    cityInputs.innerHTML = html;  //injects the html into the div
}

//TODO add ability to hit return??
// Responds to click event and checks validates input
document.getElementById("createCityInputs").onclick = function () {
    numberOfCities = document.getElementById("numberOfCities").value
    if (numberOfCities > 0 && numberOfCities < 21 && Number.isInteger(Number(numberOfCities))) {
        buildCityInputForm(document.getElementById("numberOfCities").value)
    } else {
        alert("Please enter a whole number from 1 to 20")
    }
}


// autosuggestion  for top ~1000 cities by population (in availableTags) provided by https://simplemaps.com/data/us-cities
// https://api.jqueryui.com/autocomplete/  for function -match beginning, 
// function (request, response) {
//     var matcher = new RegExp("^" + $.ui.autocomplete.escapeRegex(request.term), "i");
//     response($.grep(availableTags, function (item) {
//         return matcher.test(item);
//     }));

function showSuggestion() {
    var availableTags = ["Abilene, Texas", "Akron, Ohio", "Alafaya, Florida", "Alameda, California", "Albany, Georgia", "Albany, New York", "Albany, Oregon", "Albuquerque, New Mexico", "Alexandria, Louisiana", "Alexandria, Virginia", "Alhambra, California", "Aliso Viejo, California", "Allen, Texas", "Allentown, Pennsylvania", "Aloha, Oregon", "Alpharetta, Georgia", "Alton, Illinois", "Altoona, Pennsylvania", "Amarillo, Texas", "Ames, Iowa", "Anaheim, California", "Anchorage, Alaska", "Anderson, Indiana", "Anderson, South Carolina", "Ankeny, Iowa", "Ann Arbor, Michigan", "Anniston, Alabama", "Antioch, California", "Apex, North Carolina", "Apopka, Florida", "Apple Valley, California", "Apple Valley, Minnesota", "Appleton, Wisconsin", "Arcadia, California", "Arden-Arcade, California", "Arlington Heights, Illinois", "Arlington, Texas", "Arlington, Virginia", "Arroyo Grande, California", "Arvada, Colorado", "Ashburn, Virginia", "Asheville, North Carolina", "Aspen Hill, Maryland", "Atascocita, Texas", "Athens, Georgia", "Atlanta, Georgia", "Atlantic City, New Jersey", "Auburn, Alabama", "Auburn, Washington", "Augusta, Georgia", "Aurora, Colorado", "Aurora, Illinois", "Austin, Texas", "Avondale, Arizona", "Bakersfield, California", "Baldwin Park, California", "Baltimore, Maryland", "Bangor, Maine", "Barnstable Town, Massachusetts", "Bartlett, Tennessee", "Baton Rouge, Louisiana", "Battle Creek, Michigan", "Bay City, Michigan", "Bayamon, Puerto Rico", "Bayonne, New Jersey", "Baytown, Texas", "Beaufort, South Carolina", "Beaumont, California", "Beaumont, Texas", "Beaverton, Oregon", "Beckley, West Virginia", "Bellevue, Nebraska", "Bellevue, Washington", "Bellflower, California", "Bellingham, Washington", "Beloit, Wisconsin", "Bend, Oregon", "Benton Harbor, Michigan", "Bentonville, Arkansas", "Berkeley, California", "Berwyn, Illinois", "Bethesda, Maryland", "Bethlehem, Pennsylvania", "Billings, Montana", "Binghamton, New York", "Birmingham, Alabama", "Bismarck, North Dakota", "Blacksburg, Virginia", "Blaine, Minnesota", "Bloomington, Illinois", "Bloomington, Indiana", "Bloomington, Minnesota", "Blue Springs, Missouri", "Boca Raton, Florida", "Boise, Idaho", "Bolingbrook, Illinois", "Bonita Springs, Florida", "Bossier City, Louisiana", "Boston, Massachusetts", "Boulder, Colorado", "Bowie, Maryland", "Bowling Green, Kentucky", "Boynton Beach, Florida", "Bozeman, Montana", "Bradenton, Florida", "Brandon, Florida", "Bremerton, Washington", "Brentwood, California", "Brentwood, New York", "Bridgeport, Connecticut", "Bristol, Connecticut", "Bristol, Tennessee", "Brockton, Massachusetts", "Broken Arrow, Oklahoma", "Bronx, New York", "Brookhaven, Georgia", "Brookline, Massachusetts", "Brooklyn Park, Minnesota", "Brooklyn, New York", "Broomfield, Colorado", "Brownsville, Texas", "Brunswick, Georgia", "Bryan, Texas", "Buckeye, Arizona", "Buena Park, California", "Buffalo, New York", "Bullhead City, Arizona", "Burbank, California", "Burien, Washington", "Burlington, North Carolina", "Burlington, Vermont", "Burnsville, Minnesota", "Caguas, Puerto Rico", "Caldwell, Idaho", "Camarillo, California", "Cambridge, Massachusetts", "Camden, New Jersey", "Canton, Ohio", "Cape Coral, Florida", "Cape Girardeau, Missouri", "Carbondale, Illinois", "Carlsbad, California", "Carmel, Indiana", "Carmichael, California", "Carolina, Puerto Rico", "Carrollton, Texas", "Carson City, Nevada", "Carson, California", "Cartersville, Georgia", "Cary, North Carolina", "Casa Grande, Arizona", "Casas Adobes, Arizona", "Casper, Wyoming", "Castle Rock, Colorado", "Castro Valley, California", "Catalina Foothills, Arizona", "Cathedral City, California", "Cedar Park, Texas", "Cedar Rapids, Iowa", "Centennial, Colorado", "Centreville, Virginia", "Chambersburg, Pennsylvania", "Champaign, Illinois", "Chandler, Arizona", "Chapel Hill, North Carolina", "Charleston, South Carolina", "Charleston, West Virginia", "Charlotte, North Carolina", "Charlottesville, Virginia", "Chattanooga, Tennessee", "Cheektowaga, New York", "Chesapeake, Virginia", "Cheyenne, Wyoming", "Chicago, Illinois", "Chico, California", "Chicopee, Massachusetts", "Chino Hills, California", "Chino, California", "Chula Vista, California", "Cicero, Illinois", "Cincinnati, Ohio", "Citrus Heights, California", "Clarksville, Tennessee", "Clearwater, Florida", "Cleveland, Ohio", "Cleveland, Tennessee", "Clifton, New Jersey", "Clovis, California", "Coconut Creek, Florida", "Coeur d'Alene, Idaho", "College Station, Texas", "Collierville, Tennessee", "Colorado Springs, Colorado", "Colton, California", "Columbia, Maryland", "Columbia, Missouri", "Columbia, South Carolina", "Columbus, Georgia", "Columbus, Indiana", "Columbus, Ohio", "Commerce City, Colorado", "Compton, California", "Concord, California", "Concord, North Carolina", "Conroe, Texas", "Conway, Arkansas", "Cookeville, Tennessee", "Coon Rapids, Minnesota", "Coral Springs, Florida", "Corona, California", "Corpus Christi, Texas", "Corvallis, Oregon", "Costa Mesa, California", "Council Bluffs, Iowa", "Cranston, Rhode Island", "Cupertino, California", "Dale City, Virginia", "Dallas, Texas", "Dalton, Georgia", "Daly City, California", "Danbury, Connecticut", "Daphne, Alabama", "Davenport, Iowa", "Davie, Florida", "Davis, California", "Dayton, Ohio", "Daytona Beach, Florida", "Dearborn Heights, Michigan", "Dearborn, Michigan", "Decatur, Alabama", "Decatur, Illinois", "Deerfield Beach, Florida", "DeKalb, Illinois", "Delano, California", "Delray Beach, Florida", "Deltona, Florida", "Denton, Texas", "Denver, Colorado", "Des Moines, Iowa", "Des Plaines, Illinois", "DeSoto, Texas", "Detroit, Michigan", "Diamond Bar, California", "Doral, Florida", "Dothan, Alabama", "Dover, Delaware", "Dover, New Hampshire", "Downey, California", "Dublin, California", "Dubuque, Iowa", "Duluth, Minnesota", "Dundalk, Maryland", "Durham, North Carolina", "Eagan, Minnesota", "Eagle Pass, Texas", "East Hartford, Connecticut", "East Los Angeles, California", "East Orange, New Jersey", "East Stroudsburg, Pennsylvania", "Eastvale, California", "Eau Claire, Wisconsin", "Eden Prairie, Minnesota", "Edina, Minnesota", "Edinburg, Texas", "Edmond, Oklahoma", "El Cajon, California", "El Centro, California", "El Monte, California", "El Paso de Robles, California", "El Paso, Texas", "Elgin, Illinois", "Elizabeth, New Jersey", "Elizabethtown, Kentucky", "Elk Grove, California", "Elkhart, Indiana", "Ellicott City, Maryland", "Elmira, New York", "Elyria, Ohio", "Encinitas, California", "Enterprise, Nevada", "Erie, Pennsylvania", "Escondido, California", "Eugene, Oregon", "Euless, Texas", "Evanston, Illinois", "Evansville, Indiana", "Everett, Washington", "Fairbanks, Alaska", "Fairfield, California", "Fall River, Massachusetts", "Fargo, North Dakota", "Farmington Hills, Michigan", "Farmington, New Mexico", "Fayetteville, Arkansas", "Fayetteville, North Carolina", "Federal Way, Washington", "Fishers, Indiana", "Flagstaff, Arizona", "Flint, Michigan", "Florence, Alabama", "Florence, South Carolina", "Florence-Graham, California", "Florissant, Missouri", "Flower Mound, Texas", "Folsom, California", "Fond du Lac, Wisconsin", "Fontana, California", "Fort Collins, Colorado", "Fort Lauderdale, Florida", "Fort Myers, Florida", "Fort Smith, Arkansas", "Fort Wayne, Indiana", "Fort Worth, Texas", "Fountain Valley, California", "Fountainebleau, Florida", "Framingham, Massachusetts", "Franklin, Tennessee", "Frederick, Maryland", "Fredericksburg, Virginia", "Fremont, California", "Fresno, California", "Frisco, Texas", "Fullerton, California", "Gadsden, Alabama", "Gainesville, Florida", "Gainesville, Georgia", "Gaithersburg, Maryland", "Garden Grove, California", "Gardena, California", "Garland, Texas", "Gary, Indiana", "Gastonia, North Carolina", "Georgetown, Texas", "Germantown, Maryland", "Gilbert, Arizona", "Gilroy, California", "Glen Burnie, Maryland", "Glendale, Arizona", "Glendale, California", "Glendora, California", "Glens Falls, New York", "Goldsboro, North Carolina", "Goodyear, Arizona", "Grand Forks, North Dakota", "Grand Island, Nebraska", "Grand Junction, Colorado", "Grand Prairie, Texas", "Grand Rapids, Michigan", "Grants Pass, Oregon", "Grapevine, Texas", "Great Falls, Montana", "Greeley, Colorado", "Green Bay, Wisconsin", "Greensboro, North Carolina", "Greenville, North Carolina", "Greenville, South Carolina", "Greenwood, Indiana", "Gresham, Oregon", "Guaynabo, Puerto Rico", "Gulfport, Mississippi", "Hacienda Heights, California", "Hagerstown, Maryland", "Hamilton, Ohio", "Hammond, Indiana", "Hammond, Louisiana", "Hampton, Virginia", "Hanford, California", "Hanover, Pennsylvania", "Harlingen, Texas", "Harrisburg, Pennsylvania", "Harrisonburg, Virginia", "Hartford, Connecticut", "Hattiesburg, Mississippi", "Haverhill, Massachusetts", "Hawthorne, California", "Hayward, California", "Hazleton, Pennsylvania", "Helena, Montana", "Hemet, California", "Hempstead, New York", "Henderson, Nevada", "Hendersonville, Tennessee", "Herriman, Utah", "Hesperia, California", "Hialeah, Florida", "Hickory, North Carolina", "High Point, North Carolina", "Highland, California", "Highlands Ranch, Colorado", "Hillsboro, Oregon", "Hilton Head Island, South Carolina", "Hinesville, Georgia", "Hoboken, New Jersey", "Hoffman Estates, Illinois", "Holland, Michigan", "Hollywood, Florida", "Homestead, Florida", "Honolulu, Hawaii", "Hoover, Alabama", "Hot Springs, Arkansas", "Houma, Louisiana", "Houston, Texas", "Huntersville, North Carolina", "Huntington Beach, California", "Huntington Park, California", "Huntington, West Virginia", "Huntsville, Alabama", "Idaho Falls, Idaho", "Independence, Missouri", "Indianapolis, Indiana", "Indio, California", "Inglewood, California", "Iowa City, Iowa", "Irondequoit, New York", "Irvine, California", "Irving, Texas", "Ithaca, New York", "Jackson, Michigan", "Jackson, Mississippi", "Jackson, Tennessee", "Jacksonville, Florida", "Jacksonville, North Carolina", "Janesville, Wisconsin", "Jefferson City, Missouri", "Jersey City, New Jersey", "Johns Creek, Georgia", "Johnson City, Tennessee", "Johnstown, Pennsylvania", "Joliet, Illinois", "Jonesboro, Arkansas", "Joplin, Missouri", "Jupiter, Florida", "Jurupa Valley, California", "Kalamazoo, Michigan", "Kankakee, Illinois", "Kannapolis, North Carolina", "Kansas City, Kansas", "Kansas City, Missouri", "Kendale Lakes, Florida", "Kendall, Florida", "Kenner, Louisiana", "Kennewick, Washington", "Kenosha, Wisconsin", "Kent, Washington", "Kentwood, Michigan", "Kettering, Ohio", "Killeen, Texas", "Kingsport, Tennessee", "Kingston, New York", "Kirkland, Washington", "Kissimmee, Florida", "Knoxville, Tennessee", "Kokomo, Indiana", "La Crosse, Wisconsin", "La Habra, California", "La Mesa, California", "Lacey, Washington", "Lafayette, Colorado", "Lafayette, Indiana", "Lafayette, Louisiana", "Laguna Niguel, California", "Lake Charles, Louisiana", "Lake Elsinore, California", "Lake Forest, California", "Lake Havasu City, Arizona", "Lake Jackson, Texas", "Lakeland, Florida", "Lakeville, Minnesota", "Lakewood, California", "Lakewood, Colorado", "Lakewood, New Jersey", "Lakewood, Washington", "Lancaster, California", "Lancaster, Pennsylvania", "Lansing, Michigan", "Laredo, Texas", "Largo, Florida", "Las Cruces, New Mexico", "Las Vegas, Nevada", "Lauderhill, Florida", "Lawrence, Kansas", "Lawrence, Massachusetts", "Lawton, Oklahoma", "Layton, Utah", "League City, Texas", "Leander, Texas", "Lebanon, Pennsylvania", "Lee's Summit, Missouri", "Leesburg, Florida", "Leesburg, Virginia", "Lehi, Utah", "Lehigh Acres, Florida", "Lenexa, Kansas", "Leominster, Massachusetts", "Levittown, New York", "Levittown, Pennsylvania", "Lewiston, Idaho", "Lewiston, Maine", "Lewisville, Texas", "Lexington, Kentucky", "Lima, Ohio", "Lincoln, Nebraska", "Little Elm, Texas", "Little Rock, Arkansas", "Livermore, California", "Livonia, Michigan", "Lodi, California", "Logan, Utah", "Lompoc, California", "Long Beach, California", "Longmont, Colorado", "Longview, Texas", "Longview, Washington", "Lorain, Ohio", "Los Angeles, California", "Los Lunas, New Mexico", "Louisville, Kentucky", "Loveland, Colorado", "Lowell, Massachusetts", "Lubbock, Texas", "Lynchburg, Virginia", "Lynn, Massachusetts", "Lynwood, California", "Macon, Georgia", "Madera, California", "Madison, Alabama", "Madison, Wisconsin", "Malden, Massachusetts", "Manchester, New Hampshire", "Mandeville, Louisiana", "Manhattan, Kansas", "Manhattan, New York", "Mankato, Minnesota", "Mansfield, Ohio", "Mansfield, Texas", "Manteca, California", "Maple Grove, Minnesota", "Margate, Florida", "Maricopa, Arizona", "Marietta, Georgia", "Marysville, Washington", "Mauldin, South Carolina", "Mayaguez, Puerto Rico", "McAllen, Texas", "McKinney, Texas", "Medford, Massachusetts", "Medford, Oregon", "Melbourne, Florida", "Memphis, Tennessee", "Menifee, California", "Merced, California", "Meriden, Connecticut", "Meridian, Idaho", "Mesa, Arizona", "Mesquite, Texas", "Metairie, Louisiana", "Methuen Town, Massachusetts", "Miami Beach, Florida", "Miami Gardens, Florida", "Miami, Florida", "Michigan City, Indiana", "Middletown, New York", "Middletown, Ohio", "Midland, Michigan", "Midland, Texas", "Midwest City, Oklahoma", "Milford city , Connecticut", "Millcreek, Utah", "Milpitas, California", "Milwaukee, Wisconsin", "Minneapolis, Minnesota", "Minnetonka, Minnesota", "Miramar, Florida", "Mishawaka, Indiana", "Mission Viejo, California", "Mission, Texas", "Missoula, Montana", "Missouri City, Texas", "Mobile, Alabama", "Modesto, California", "Monessen, Pennsylvania", "Monroe, Louisiana", "Montebello, California", "Monterey Park, California", "Montgomery, Alabama", "Moore, Oklahoma", "Moreno Valley, California", "Morgantown, West Virginia", "Morristown, Tennessee", "Mount Pleasant, South Carolina", "Mount Prospect, Illinois", "Mount Vernon, New York", "Mount Vernon, Washington", "Mountain View, California", "Muncie, Indiana", "Murfreesboro, Tennessee", "Murrieta, California", "Muskegon, Michigan", "Myrtle Beach, South Carolina", "Nampa, Idaho", "Napa, California", "Naperville, Illinois", "Nashua, New Hampshire", "Nashville, Tennessee", "National City, California", "New Bedford, Massachusetts", "New Bern, North Carolina", "New Braunfels, Texas", "New Britain, Connecticut", "New Brunswick, New Jersey", "New Haven, Connecticut", "New Orleans, Louisiana", "New Rochelle, New York", "New York, New York", "Newark, New Jersey", "Newark, Ohio", "Newport Beach, California", "Newport News, Virginia", "Newton, Massachusetts", "Noblesville, Indiana", "Norfolk, Virginia", "Normal, Illinois", "Norman, Oklahoma", "North Bethesda, Maryland", "North Charleston, South Carolina", "North Las Vegas, Nevada", "North Little Rock, Arkansas", "North Miami, Florida", "North Port, Florida", "North Richland Hills, Texas", "Norwalk, California", "Norwalk, Connecticut", "Norwich, Connecticut", "Novato, California", "Novi, Michigan", "Oak Lawn, Illinois", "Oak Park, Illinois", "Oakland, California", "Ocala, Florida", "Oceanside, California", "Odessa, Texas", "O'Fallon, Missouri", "Ogden, Utah", "Oklahoma City, Oklahoma", "Olathe, Kansas", "Olympia, Washington", "Omaha, Nebraska", "Ontario, California", "Orange, California", "Orem, Utah", "Orland Park, Illinois", "Orlando, Florida", "Oshkosh, Wisconsin", "Overland Park, Kansas", "Owensboro, Kentucky", "Oxnard, California", "Palatine, Illinois", "Palm Bay, Florida", "Palm Beach Gardens, Florida", "Palm Coast, Florida", "Palm Desert, California", "Palm Harbor, Florida", "Palmdale, California", "Palo Alto, California", "Panama City, Florida", "Paradise, Nevada", "Paramount, California", "Parker, Colorado", "Parkersburg, West Virginia", "Parma, Ohio", "Pasadena, California", "Pasadena, Texas", "Pasco, Washington", "Passaic, New Jersey", "Paterson, New Jersey", "Pawtucket, Rhode Island", "Peabody, Massachusetts", "Pearland, Texas", "Pembroke Pines, Florida", "Pensacola, Florida", "Peoria, Arizona", "Peoria, Illinois", "Perris, California", "Perth Amboy, New Jersey", "Petaluma, California", "Pflugerville, Texas", "Pharr, Texas", "Philadelphia, Pennsylvania", "Phoenix, Arizona", "Pico Rivera, California", "Pine Hills, Florida", "Pinellas Park, Florida", "Pittsburg, California", "Pittsburgh, Pennsylvania", "Pittsfield, Massachusetts", "Placentia, California", "Plainfield, New Jersey", "Plano, Texas", "Plantation, Florida", "Pleasanton, California", "Plymouth, Minnesota", "Pocatello, Idaho", "Poinciana, Florida", "Pomona, California", "Pompano Beach, Florida", "Ponce, Puerto Rico", "Pontiac, Michigan", "Port Arthur, Texas", "Port Charlotte, Florida", "Port Huron, Michigan", "Port Orange, Florida", "Port St. Lucie, Florida", "Porterville, California", "Portland, Maine", "Portland, Oregon", "Portsmouth, New Hampshire", "Portsmouth, Virginia", "Pottstown, Pennsylvania", "Poughkeepsie, New York", "Prescott Valley, Arizona", "Providence, Rhode Island", "Provo, Utah", "Pueblo, Colorado", "Queen Creek, Arizona", "Queens, New York", "Quincy, Massachusetts", "Racine, Wisconsin", "Raleigh, North Carolina", "Rancho Cordova, California", "Rancho Cucamonga, California", "Rapid City, South Dakota", "Reading, Pennsylvania", "Redding, California", "Redlands, California", "Redmond, Washington", "Redondo Beach, California", "Redwood City, California", "Reno, Nevada", "Renton, Washington", "Reston, Virginia", "Revere, Massachusetts", "Rialto, California", "Richardson, Texas", "Richland, Washington", "Richmond, California", "Richmond, Virginia", "Rio Rancho, New Mexico", "Riverside, California", "Riverview, Florida", "Roanoke, Virginia", "Rochester Hills, Michigan", "Rochester, Minnesota", "Rochester, New York", "Rock Hill, South Carolina", "Rockford, Illinois", "Rocklin, California", "Rockville, Maryland", "Rocky Mount, North Carolina", "Rogers, Arkansas", "Rome, Georgia", "Rosemead, California", "Roseville, California", "Roswell, Georgia", "Round Lake Beach, Illinois", "Round Rock, Texas", "Rowland Heights, California", "Rowlett, Texas", "Royal Oak, Michigan", "Sacramento, California", "Saginaw, Michigan", "Sahuarita, Arizona", "Salem, Oregon", "Salinas, California", "Salisbury, Maryland", "Salt Lake City, Utah", "Sammamish, Washington", "San Angelo, Texas", "San Antonio, Texas", "San Bernardino, California", "San Buenaventura, California", "San Clemente, California", "San Diego, California", "San Francisco, California", "San Jose, California", "San Juan, Puerto Rico", "San Leandro, California", "San Luis Obispo, California", "San Marcos, California", "San Marcos, Texas", "San Mateo, California", "San Rafael, California", "San Ramon, California", "San Tan Valley, Arizona", "Sandy Springs, Georgia", "Sandy, Utah", "Sanford, Florida", "Santa Ana, California", "Santa Barbara, California", "Santa Clara, California", "Santa Clarita, California", "Santa Cruz, California", "Santa Fe, New Mexico", "Santa Maria, California", "Santa Monica, California", "Santa Rosa, California", "Santee, California", "Sarasota, Florida", "Saratoga Springs, New York", "Savannah, Georgia", "Schaumburg, Illinois", "Schenectady, New York", "Scottsdale, Arizona", "Scranton, Pennsylvania", "Seaside, California", "Seattle, Washington", "Sebring, Florida", "Shawnee, Kansas", "Sheboygan, Wisconsin", "Sherman, Texas", "Shoreline, Washington", "Shreveport, Louisiana", "Sierra Vista, Arizona", "Silver Spring, Maryland", "Simi Valley, California", "Sioux City, Iowa", "Sioux Falls, South Dakota", "Skokie, Illinois", "Slidell, Louisiana", "Smyrna, Georgia", "Smyrna, Tennessee", "Somerville, Massachusetts", "South Bend, Indiana", "South Fulton, Georgia", "South Gate, California", "South Hill, Washington", "South Jordan, Utah", "South Lyon, Michigan", "South San Francisco, California", "South Whittier, California", "Southaven, Mississippi", "Southfield, Michigan", "Sparks, Nevada", "Spartanburg, South Carolina", "Spokane Valley, Washington", "Spokane, Washington", "Spring Hill, Florida", "Spring Valley, Nevada", "Spring, Texas", "Springdale, Arkansas", "Springfield, Illinois", "Springfield, Massachusetts", "Springfield, Missouri", "Springfield, Ohio", "Springfield, Oregon", "St. Augustine, Florida", "St. Charles, Missouri", "St. Clair Shores, Michigan", "St. Cloud, Florida", "St. Cloud, Minnesota", "St. George, Utah", "St. Joseph, Missouri", "St. Louis, Missouri", "St. Paul, Minnesota", "St. Peters, Missouri", "St. Petersburg, Florida", "Stamford, Connecticut", "State College, Pennsylvania", "Staten Island, New York", "Staunton, Virginia", "Sterling Heights, Michigan", "Stockton, California", "Stonecrest, Georgia", "Suffolk, Virginia", "Sugar Land, Texas", "Summerville, South Carolina", "Sumter, South Carolina", "Sunnyvale, California", "Sunrise Manor, Nevada", "Sunrise, Florida", "Surprise, Arizona", "Syracuse, New York", "Tacoma, Washington", "Tallahassee, Florida", "Tamarac, Florida", "Tamiami, Florida", "Tampa, Florida", "Taunton, Massachusetts", "Taylor, Michigan", "Taylorsville, Utah", "Temecula, California", "Tempe, Arizona", "Temple, Texas", "Terre Haute, Indiana", "Texarkana, Texas", "Texas City, Texas", "The Hammocks, Florida", "The Villages, Florida", "The Woodlands, Texas", "Thornton, Colorado", "Thousand Oaks, California", "Tigard, Oregon", "Tinley Park, Illinois", "Titusville, Florida", "Toledo, Ohio", "Toms River, New Jersey", "Topeka, Kansas", "Torrance, California", "Town 'n' Country, Florida", "Towson, Maryland", "Tracy, California", "Traverse City, Michigan", "Trenton, New Jersey", "Troy, Michigan", "Tucson, Arizona", "Tulare, California", "Tulsa, Oklahoma", "Turlock, California", "Tuscaloosa, Alabama", "Tustin, California", "Twin Falls, Idaho", "Tyler, Texas", "Union City, California", "Union City, New Jersey", "Upland, California", "Utica, New York", "Vacaville, California", "Valdosta, Georgia", "Vallejo, California", "Vancouver, Washington", "Victoria, Texas", "Victorville, California", "Vineland, New Jersey", "Virginia Beach, Virginia", "Visalia, California", "Vista, California", "Waco, Texas", "Waldorf, Maryland", "Walla Walla, Washington", "Walnut Creek, California", "Waltham, Massachusetts", "Warner Robins, Georgia", "Warren, Michigan", "Warwick, Rhode Island", "Washington, District of Columbia", "Waterbury, Connecticut", "Waterloo, Iowa", "Watertown, New York", "Watsonville, California", "Waukegan, Illinois", "Waukesha, Wisconsin", "Wausau, Wisconsin", "Weirton, West Virginia", "Wellington, Florida", "Wenatchee, Washington", "Wesley Chapel, Florida", "West Allis, Wisconsin", "West Bend, Wisconsin", "West Covina, California", "West Des Moines, Iowa", "West Hartford, Connecticut", "West Haven, Connecticut", "West Jordan, Utah", "West Lafayette, Indiana", "West New York, New Jersey", "West Palm Beach, Florida", "West Sacramento, California", "West Valley City, Utah", "Westland, Michigan", "Westminster, California", "Westminster, Colorado", "Weston, Florida", "Weymouth Town, Massachusetts", "Wheaton, Illinois", "Wheaton, Maryland", "Wheeling, West Virginia", "White Plains, New York", "Whittier, California", "Wichita Falls, Texas", "Wichita, Kansas", "Williamsburg, Virginia", "Williamsport, Pennsylvania", "Wilmington, Delaware", "Wilmington, North Carolina", "Winchester, Virginia", "Winston-Salem, North Carolina", "Winter Haven, Florida", "Woodbury, Minnesota", "Woodland, California", "Worcester, Massachusetts", "Wylie, Texas", "Wyoming, Michigan", "Yakima, Washington", "Yonkers, New York", "Yorba Linda, California", "York, Pennsylvania", "Youngstown, Ohio", "Yuba City, California", "Yucaipa, California", "Yuma, Arizona", "Zephyrhills, Florida",];
    $(".userInput").autocomplete({
        source: function (request, response) {
            var matcher = new RegExp("^" + $.ui.autocomplete.escapeRegex(request.term), "i");
            response($.grep(availableTags, function (item) {
                return matcher.test(item);
            }));
        }
    });
};