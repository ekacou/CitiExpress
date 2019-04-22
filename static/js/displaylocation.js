// create an instance of google goelocation
var geocoder = new google.maps.Geocoder();
var latlng;
if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition(success,error);
    function success(pos){
        //setting latitude coords
        var latitude = pos.coords.latitude;
        //set longitude coords
        var longitude = pos.coords.longitude;
        latlng = new google.maps.LatLng(latitude, longitude);
        geocoder.geocode( {'location':latlng}, function(results, status){
        if (status == 'OK'){
            if (result[0]){
                var address = results[0].formatted_address;
                console.log(`your address is : ${address}`);
                //still need to display address to page. solve google referer issue
            }
        }
    });
    //just for debugging
    console.log(`your current lat is: ${latitude}`);
    console.log(`your current lng is: ${longitude}`);
    console.log(`your current latlng is: ${latlng}`);
    }
    function error (err){
        console.warn(`ERROR(${err.code}): ${err.message}`);
    }

}