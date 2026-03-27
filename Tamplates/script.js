
function alerta() {
    alert("Olá, você clicou no botão!");
}



async function getCode1() {
    const url = ""
    try {
        const response = await fetch(url)
        const data = await response
        return data
    } catch(err) {
        alert("Não foi possivel pegar os dados")
    }
}


const qrcode = new QRCode("qrcode1",{
    text: "1",
    width: 200,
    height: 200,
    colorDark : "#000000",
    colorLight : "#ffffff",
    correctLevel : QRCode.CorrectLevel.H
});

const qrcode2 = new QRCode("qrcode2",{
    text: "1",
    width: 200,
    height: 200,
    colorDark : "#000000",
    colorLight : "#ffffff",
    correctLevel : QRCode.CorrectLevel.H
});


async function criarCode() {
    //const dados = await getCode1()

    dados = "https://hogangnono.com"
    qrcode.criarCode(dados)

}

//criarCode()


//new QRCode(document.getElementById("qrcode1"), "http://jindo.dev.naver.com/collie");
