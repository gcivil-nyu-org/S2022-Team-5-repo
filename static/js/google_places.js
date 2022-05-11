
$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initAutoComplete)
})

let autocomplete;

function initAutoComplete(){
   autocomplete = new google.maps.places.Autocomplete(
       document.getElementById('id-google-address'),
       {
           types: ['address'],
           componentRestrictions: {'country': [base_country.toLowerCase()]},
       })

   autocomplete.addListener('place_changed', onPlaceChanged);
}


function onPlaceChanged (){

    var place = autocomplete.getPlace();

    var geocoder = new google.maps.Geocoder()
    var address = document.getElementById('id-google-address').value

    geocoder.geocode( { 'address': address}, function(results, status) {

        if (status == google.maps.GeocoderStatus.OK) {
            var latitude = results[0].geometry.location.lat();
            var longitude = results[0].geometry.location.lng();

            document.getElementById('longitude').value = longitude
            document.getElementById('latitude').value = latitude
        } 
    }); 

    if (!place.geometry){
        document.getElementById('id-google-address').placeholder = "*Begin typing address";
    }
    else{
        var borough = ""
        for (var i = 0; i < place.address_components.length; i++) {
            for (var j = 0; j < place.address_components[i].types.length; j++) {

                if (place.address_components[i].types[j] == "street_number") {
                    var num = place.address_components[i].long_name  
                }
                if (place.address_components[i].types[j] == "route") {
                    var addy = place.address_components[i].long_name
                }
                if (place.address_components[i].types[j] == "sublocality") {
                    borough = place.address_components[i].long_name
                    
                }
                if (place.address_components[i].types[j] == "postal_code") {   
                    document.getElementById('zipcode').value = place.address_components[i].long_name
                }
            }
        }
        document.getElementById('address1').value = num + " " + addy
        if (borough !== ""){
            document.getElementById('borough').value = borough
        }


        //find all hidden inputs & ignore csrf token
        var x = $( "input:hidden" );
        for (let i = 0; i < x.length; i++){
            if (x[i].name != "csrfmiddlewaretoken")  
            x[i].type = "text"; 
            x.eq(x).attr("class", 'hidden-el')  
        }

        //fade in the completed form
        $('.hidden-el').fadeIn()
    }
}