var SCYTALE = {};
Reveal.addEventListener('fragmentshown', function(event) {
    function zeroPadInteger( num ) {
        var str = "00" + parseInt( num );
        return str.substring( str.length - 2 );
    }
    if (event.fragment.className.indexOf("timer") !== -1) {
        var start = new Date(),
            minutesEl = document.querySelectorAll( '.timer .minutes' ),
            secondsEl = document.querySelectorAll( '.timer .seconds' );
        SCYTALE.timer = setInterval(function() {
            var diff, minutes, seconds,
                now = new Date();
            diff = 15 * 60 * 1000 + 1000 - now.getTime() + start.getTime();
            if (diff < 0) {
                diff = 0;
            }
            minutes = Math.floor( ( diff / ( 1000 * 60 ) ) % 60 );
            seconds = Math.floor( ( diff / 1000 ) % 60 );
            minutesEl[0].innerHTML = minutes;
            secondsEl[0].innerHTML = ":" + zeroPadInteger(seconds);
        }, 1000);
    }
});
Reveal.addEventListener('fragmenthidden', function(event) {
    if (event.fragment.className.indexOf("timer") !== -1) {
        clearInterval(SCYTALE.timer);
        document.querySelectorAll( '.timer .minutes' )[0].innerHTML = "15";
        document.querySelectorAll( '.timer .seconds' )[0].innerHTML = ":00";
    }
});