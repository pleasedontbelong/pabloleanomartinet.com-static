var map;
jQuery(document).ready(function(){

    map = new GMaps({
        div: '#map',
        lat: 48.870077, 
        lng: 2.345325,
    });
    map.addMarker({
        lat: 48.870077,
        lng: 2.345325,
        title: 'Address',      
        infoWindow: {
            content: '<h5 class="title">Botify HQ</h5><p><span class="region">8 rue Saint Fiacre</span><br><span class="postal-code">75 002 Paris</span><br><span class="country-name">France</span></p>'
        }
        
    });

});