
function alerta() {
    alert("Olá, você clicou no botão!");
}


async function getCode1() {
    const url = ""
    try {
        fetch(url)
            .then(response => response.json)
    } catch(err) {
        alert("Não foi possivel pegar os dados")
    }
}

const qrcode = new QRCode("qrcode1")

function criarCode() {
    const elText = document.getElementById("text");


}


new QRCode(document.getElementById("qrcode1"), "http://jindo.dev.naver.com/collie");
