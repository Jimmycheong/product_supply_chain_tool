var express = require('express')
var morgan = require('morgan')

var app = express()

app.use(morgan('dev'))
app.use(express.static('public'))

app.get('/home', function(req, res) {
	console.log("dir name: " + __dirname)
	res.sendFile(__dirname + "/" + "index.html")
})


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

var server = app.listen(8081, function() {
	var host = server.address().address
	var port = server.address().port

	console.log("Example app listening at http://%s:%s", host, port)
})
