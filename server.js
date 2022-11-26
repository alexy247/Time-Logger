const express = require('express');
const fs = require('fs');

const app = express();

/* Testing DATA */
app.get('/', function (req, res) {
    fs.readFile('./data/parsed/data.json', function(err, data) {
        if (err){
            throw err;
        }
        res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' , 'Access-Control-Allow-Headers': '*'});
        res.end(data);
        return;
    });
})

app.get('/day_stat', function (req, res) {
    fs.readFile('./data/stat/day_stat.json', function(err, data) {
        if (err){
            throw err;
        }
        res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' , 'Access-Control-Allow-Headers': '*'});
        res.end(data);
        return;
    });
})

app.listen(3000);