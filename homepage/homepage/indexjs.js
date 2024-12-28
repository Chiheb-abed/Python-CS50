function sendMail (){

    var parms = {
        name : document.getElementById("name").value,
        email : document.getElementById("email").value,
        message : document.getElementById("message").value,

    };



const serviceID = "service_avservice_3lblnuj";
const templateID = "template_x2f5qix";

emailjs.send(serviceID,templateID,parms)
.then(
    res => {
        document.getElementById("name").value ="",
        document.getElementById("email").value="",
        document.getElementById("message").value = "",
        console.log(res);
        alert ("your message send succefuly")
    })
.catch (err => console.log(err));

}