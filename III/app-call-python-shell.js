const express = require('express')
const multer = require('multer')
const app = express()
let { PythonShell } = require('python-shell')
app.set('view engine', 'ejs');
app.use(express.static('public'))

// set the storage engine
const storage = multer.diskStorage({
    destination: 'public/tmp_uploads/', //save path
    filename: function (req, file, cb){
        cb(null, file.originalname);
    }
});

//init upload
const upload = multer({storage: storage});//single image Key:myImage
const fs = require('fs')


app.listen(3000, () => {
    console.log('server start on port 3000')
})

app.get('/photo', (req, res) =>{
    res.render('home')
});

app.post('/photo', upload.single('spotUpload'),(req, res)=>{
    // if (err) console.log(err);
    // res.send({result:'success'});
    console.log(req.file);
    res.render('home',{
        result: true,
        uploadPic : '/tmp_uploads/' + req.file.filename,
        uploadPicPath : req.file.path
    })
})

app.get('/photo/python', pythonProcess)
app.get('/photo/photocategory', photocategory)
app.get('/photo/photodetect', photoDetect)



function pythonProcess(req, res) {
    let options = {
        args:
            [
                req.query.name,
                req.query.from
            ]
    }


    PythonShell.run('./process.py', options, (err, data) => {
        if (err) res.send(err)
        const parsedString = JSON.parse(data)
        console.log(data);
        console.log(parsedString);
        // console.log(`name: ${parsedString.Name}, from: ${parsedString.From}`)
        res.json(parsedString)

    })
}

//category photos!!!!!!!!!!!! 
function photocategory(req, res) {
    let options = {
        args:
            [
                req.query.name,
                req.query.from
            ]
    }


    PythonShell.run('./photocategory.py', options, (err, result) => {
        if (err) res.send(err)
        const parsedString = JSON.parse(result)
        // console.log(result);
        // console.log(parsedString);
        // console.log(`name: ${parsedString.Name}, from: ${parsedString.From}`)
        res.json(parsedString)

    })
}

function photoDetect(req, res) {
    // set photo path in options
    let options = {
        args:[req.query.uploadPicPath]
    }
    
    PythonShell.run('./photodetect.py', options, (err, result) => {
        if (err) res.send(err)
        const parsedString = JSON.parse(result)
        // console.log(result);
        // console.log(parsedString);
        // console.log(`name: ${parsedString.Name}, from: ${parsedString.From}`)
        res.json(parsedString)

    })
}