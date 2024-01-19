const express = require('express');
const nodemailer = require('nodemailer');
const app = express();
app.use(express.json());
function enviaremail(){
        app.post('/enviaremail', (req, res) => {
            const mensagemdacaixadetexto = req.body.mensagem;

            let transporter = nodemailer.createTransport({
            service: 'gmail',
            port: 587,
            auth: {
                user: 'caiokotan@gmail.com',
                pass: 'ujln yahk ocpz kzeo'
            }
        });

        let mailOptions = {
            from: '"Caio" <caiokotan@gmail.com>',
            to: 'caiokotan@gmail.com',
            subject: 'Olá!',
            text: mensagemdacaixadetexto,
            html: '<b>Olá!</b>'
        };

        transporter.sendMail(mailOptions, (error, info) => {
            if (error) {
                console.log(error);
                res.status(500).send(error);
            } else {
                console.log('E-mail enviado: ' + info.response);
                res.status(200).send('E-mail enviado');
            }
        });
    });

    app.listen(3000, () => console.log('Servidor da web local escutando na porta 3000'));
}