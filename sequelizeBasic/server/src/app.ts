import express from 'express'
import { Model, Sequelize, DataTypes } from 'sequelize';
import People from '../models/friend'
import * as DB from '../models/index'
import bodyParser from 'body-parser'


const mysql: Sequelize = DB.init();
const app = express();
app.use(bodyParser.json())

app.get('/users', async (req, res)=>{
    const temp = await People.findAll({
        attributes : ['name', 'hobby'],
        raw : true
    }).then(function(){
        console.log(arguments)
        res.json(temp);
    }).catch(function(e){
        res.status(400).send(e.message)
    })
})

app.get('/user/:id', async (req, res)=>{

})

app.post('/user', async (req, res)=>{
    const body = req.body;
    const newPeople = await People.create({
        name : body.name,
        hobby : body.hobby
    }).then(function(){
        console.log(arguments)
        res.json({ok:true})
    }).catch(function(e){
        res.status(400).send(e.message)
    })
})

app.delete('/user/:id', async (req, res)=>{
    await People.destroy({where : {id:req.params.id}})
    .then(function(){
        console.log(arguments)
        res.json({ok:true})
    })
    .catch(function(e){
        res.status(400).send(e.message)
    })
})

app.listen(7878, function(){
    console.log('The server has started on port 7878');
});

