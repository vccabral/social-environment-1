
    var map;
    var current_url = window.location.href;
    var arr = current_url.split("/");
    var base_url = arr[0] + "//" + arr[2];
    var api_call_count = 0;
    var marker_count = 0;
    var duplicate_marker_count = 0;
    var exists_markers = {"air": [], "toxic": [], "quality": []};
    var marker_universe = {"air": {}, "toxic": {}, "quality": {}};
    var cirlce;

    var quality_code = {
      '1' : '#66994e',
        '2': '#ffbe43',
        '3': '#ff651b',
        '4': '#850008',
        '5': '#5f0022',
        '6': '#2f001c',
        '7': '#000000'
    };

    var load_from_url = function (url, render_method) {
        $.ajax(url).done(render_method);
    };


    var air_quality_url_from_bounds = function (api_endpoint, bounds) {
        var lat = (bounds._southWest.lat + bounds._northEast.lat) / 2.0;
        var lng = (bounds._southWest.lng + bounds._northEast.lng) / 2.0;
        var url = base_url + api_endpoint +
                '?latitude=' + lat +
                '&longitude=' + lng +
                '&year=' + $("#year").val();
        return url;
    };

    var generic_url_from_bounds = function (api_endpoint, bounds) {
        var url = base_url + api_endpoint +
                '?min_latitude=' + bounds._southWest.lat + '&max_latitude=' + bounds._northEast.lat +
                '&min_longitude=' + bounds._southWest.lng + '&max_longitude=' + bounds._northEast.lng +
                "&year=" + $("#year").val();
        return url;
    }

    var get_generic_load_method = function (api_endpoint, render_method, get_url_from_bounds) {
        return function (bounds) {
            var url = get_url_from_bounds(api_endpoint, bounds);

            $.ajax(url)
                    .done(function (data) {
                        render_method(data);

                        if (data.next) {
                            load_from_url(data.next, render_method);
                        }
                    });
            $('#sharebutton').html('<fb:sharebutton class="fb-share-button"  href="' + window.location.href + '" style="position: absolute; z-index:1000;left: 30px; bottom:20px;" layout="button_count"/>');
            if (typeof FB !== 'undefined') {
                FB.XFBML.parse(document.getElementById('sharebutton'));
            }
        }
    };

    var get_marker = function (data_point) {
        var point = [
            parseFloat(data_point.latitude),
            parseFloat(data_point.longitude)
        ];

        var all_points = "";
        if ("grade" in data_point) {
            var content = "<div style='height:150px;'>" + data_point.title + "<div id='div2'></div></div>" + all_points;
            var popup = L.popup()
                    .setLatLng(map.getCenter())
                    .setContent(content)
                    .openOn(map);

            var div2 = d3.select(document.getElementById('div2'));
            var rp2 = radialProgress(document.getElementById('div2'))
                    .diameter(150)
                    .value(data_point.grade)
                    .render();

            $(".arc").css({'fill': quality_code[data_point.score]})
            marker = L.marker(
                    point,
                    {"title": data_point.title}
            ).bindPopup(popup).openPopup();

            return marker;
        } else {
            var content = data_point.title;
            var popup = L.popup()
                    .setLatLng(map.getCenter())
                    .setContent(content);
            marker = L.marker(
                    point,
                    {"title": data_point.title}
            ).bindPopup(popup);

            return marker;
        }

    };

    var generate_render_method = function (historical_markers) {
        return function (data) {
            var year = $("#year").val();
            var local_markers = [];
            for (var lcv = 0; lcv < data.results.length; lcv++) {
                var pk = data.results[lcv].id
                if (!(pk in historical_markers)) {
                    historical_markers[pk] = true;
                    var marker = get_marker(data.results[lcv]);
                    local_markers.push(marker);
                }
            }
            if (data.results.length > 0) {
                marker_universe[data.results[0].universe][year].addLayers(local_markers);
            }
        }
    }

    var load_toxic_to_map = get_generic_load_method(
            '/api/v1/toxic/',
            generate_render_method(
                    exists_markers['toxic']
            ),
            generic_url_from_bounds
    );

    var load_air_quality_to_map = get_generic_load_method(
            '/api/v1/airquality/',
            generate_render_method(
                    exists_markers['air']
            ),
            generic_url_from_bounds
    );

    var load_generic_quality_to_map = get_generic_load_method(
            '/api/v1/map_score/',
            function (data) {
                var year = $("#year").val();
                marker_universe[data.results[0].universe][year].clearLayers();
                var marker = get_marker(data.results[0]);
                marker_universe[data.results[0].universe][year].addLayer(marker);

                $('#score').html(Math.round(data.results[0].grade*100)/100.0 + ' ' + data.results[0].score_title);
                $('#lat_long').html('Latitude: ' + data.results[0].latitude + ' / Longitude: ' + data.results[0].longitude);
                $('#quality_bar').css('background-color',quality_code[data.results[0].score]);

            },
            air_quality_url_from_bounds
    );

    var all_load_methods = [
        // load_toxic_to_map,
        load_air_quality_to_map,
        load_generic_quality_to_map
    ];

    var set_refresh_url = function () {
        var center = map.getCenter();
        location.hash = center.lat + "/" + center.lng + "/" + map.getZoom() + "/" + $("#year").val();
    };

    //function should take a factory to draw icons.

    var create_universe = function (universe_name, year) {
        if (!(year in marker_universe[universe_name])) {
            marker_universe[universe_name][year] = L.markerClusterGroup({
                spiderfyOnMaxZoom: false,
                showCoverageOnHover: true,
                zoomToBoundsOnClick: false
            });

            marker_universe[universe_name][year].addTo(map);
        }
    };

    var load_markers_to_bounds = function (e) {
        set_refresh_url();

        var year = $("#year").val();
        var bounds = map.getBounds();

        create_universe("air", year);
        create_universe("toxic", year);
        create_universe("quality", year);

        circle.setLatLng(map.getCenter());

        for (var i in all_load_methods) {
            all_load_methods[i](bounds);
        }
    };

    var initializeMap = function (position) {
        var center = [position.coords.latitude, position.coords.longitude]
        var zoom = position.zoom || 13;
        map = L.map('map').setView(center, zoom);

        L.tileLayer('https://api.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoidmNjYWJyYWwiLCJhIjoiY2lpNWZpMXV3MDFnaXR3a2Z4cWhtOHIzdCJ9.VrZvhWnHZmXBxdJf1XWitQ', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            minZoom: 1,
            maxZoom: 20,
            id: '28903289137890890',
            accessToken: 'pk.eyJ1IjoidmNjYWJyYWwiLCJhIjoiY2lpNWZpMXV3MDFnaXR3a2Z4cWhtOHIzdCJ9.VrZvhWnHZmXBxdJf1XWitQ'
        }).addTo(map);

        L.mapbox.accessToken = 'pk.eyJ1IjoidmNjYWJyYWwiLCJhIjoiY2lpNWZpMXV3MDFnaXR3a2Z4cWhtOHIzdCJ9.VrZvhWnHZmXBxdJf1XWitQ';

        var geocoder = L.mapbox.geocoderControl('mapbox.places', {
            autocomplete: true,
            keepOpen: false
        });

        map.addControl(geocoder);
        geocoder.on('select', function (event) {
            $(".leaflet-control-mapbox-geocoder-form").find("input").val(event.feature.place_name);
            load_markers_to_bounds();
        });


        circle = L.circle(center, 3218.69); // two miles
        circle.addTo(map);

        map.on('dragend', load_markers_to_bounds);
        load_markers_to_bounds();
    }

    $("#year").change(function (event) {
        var cur_year = $("#year").val();
        for (var universe in marker_universe) {
            for (var year in marker_universe[universe]) {
                if (cur_year != year) {
                    if (year in marker_universe[universe]) {
                        map.removeLayer(marker_universe[universe][year]);
                    }
                }
                if (cur_year == year) {
                    if (year in marker_universe[universe]) {
                        marker_universe[universe][year].addTo(map);
                    }
                }
            }
        }
        load_markers_to_bounds();
    });

    var initialPosition = {
        "coords": {
            "latitude": 38.902590,
            "longitude": -77.050175,
        },
        "zoom": 13
    };

    if (location.hash.length > 1) {
        initialPosition.coords.latitude = location.hash.split("/")[0].substring(1);
        initialPosition.coords.longitude = location.hash.split("/")[1];
        initialPosition.zoom = location.hash.split("/")[2];
        $("#year").val(location.hash.split("/")[3])
        initializeMap(initialPosition);
    }
    else if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
                initializeMap,
                function () {
                    console.log("fallback");
                    initializeMap(initialPosition);
                }, {timeout: 2500});
    } else {
        initializeMap(initialPosition);
    }
