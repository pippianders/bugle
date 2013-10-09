var Faye = require('faye');
var fs = require('fs');
var sys = require('sys');
var http = require('http');

var settings = JSON.parse(fs.readFileSync(process.argv[2] || './settings.json').toString());

var debug = function (s) {
    if (settings.debug) {
        sys.debug(s);
    }
};

var fayeServer = new Faye.NodeAdapter({
    mount:    '/faye',
    timeout:  45
});

var httpServer = http.createServer();
fayeServer.attach(httpServer);

debug("Starting Faye server on port "+settings.port);
httpServer.listen(settings.port);

