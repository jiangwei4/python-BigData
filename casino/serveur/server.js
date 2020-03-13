const express = require('express')
const sync = require('./sync.js')
const app = express()
const bodyParser = require('body-parser')
const fs = require('fs')

const PORT = 8083


try {
	fs.statSync('./sync.json')
	sync.initSync('sync.json')
	if(sync.get('FILE') == undefined)
		sync.set('FILE',[])	
} 
catch(e){
	sync.initSync('sync.json')
	sync.set('FILE',[])	
}


app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE, OPTIONS");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Authorization");
    next();
})

app.use(bodyParser.json())

app.post('/',(request,response) => {
	let tmp2 = sync.get('FILE')
	tmp2.push({
		'niveau':request.body.niveau,
		'name':request.body.name,
		'essai':request.body.essai,
		'sold':request.body.sold,
		'mise':request.body.mise,
		'valeurJouer':request.body.valeurJouer,
		'randomOrdi':request.body.randomOrdi,
		'gain':request.body.gain
	})
	sync.set('FILE',tmp2)
	sync.write()
	response.send({'response':'ok'})
})

app.get('/',(request,response) => {
	let tmp1 = new Array()
	if(sync.get('FILE').length > 0)
		sync.get('FILE').forEach(element => {
			if(element.niveau = request.body.niveau)
				tmp1.push(element)
		})
	response.send({'response':tmp1})
})

app.listen(PORT,() => {
    console.log(`ok ${PORT}`)
})