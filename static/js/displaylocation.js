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

        latlng =


    //just for debugging
    console.log(`your current lat is: ${latitude}`);
    console.log(`your current lng is: ${longitude}`);
    console.log(`your current latlng is: ${latlng}`);

    geocoder.geocode({'location':latlng}, function(results, status){
        if (status == 'OK'){
        var address = "";
            if (result[0]){
                address = results[0].formatted_address;
                console.log(`your address is : ${address}`);
                //still need to display address to page. solve google referer issue
            }else { console.log(`Nothing was passed`)}
        }
        });
    }
    function error (err){
        console.warn(`ERROR(${err.code}): ${err.message}`);
    }
}

//latlng formatted function




