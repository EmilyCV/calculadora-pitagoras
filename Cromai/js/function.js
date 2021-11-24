//Armazenando "name" no localStorage
function setName() {
    var name = document.getElementById('name').value
    window.localStorage.setItem("name",name)
    getName();
}
//Pegando o nome armazenado no localStorage
function getName(){
    var name = window.localStorage.getItem("name");
    //Passando o nome armazenado assim que abrimos a pag calculator.html
    document.getElementById("name").innerHTML = `Bem vinde, ${name}`;
    console.log(document.getElementById("name"));
}

//Concatenando as funções e suas respectivas chamadas
function funcoes() {
    var catOp = document.getElementById('catOp').value;
    var catAd = document.getElementById('catAd').value;
    var pitagoras = Math.pow((Math.pow(catOp, 2) + Math.pow(catAd, 2)), (1 / 2));
    //Validação para saber se os valores passados no input correspondem a de um triângulo retângulo
    if (Math.pow(pitagoras, 2) != ((Math.pow(catOp, 2) + Math.pow(catAd, 2)))) {
        error();
    }
    //Iniciando a função que armazena todos os valores passados no input
    else {
        historico();

    }
}
let listaHist = []
function historico() {
    //Os dois campos são obrigatórios, essa função valida se eles foram preenchidos corretamente
    if ((document.getElementById('catOp').value == "") & (document.getElementById('catAd').value == "")) {
        camposError = "Os dois campos são obrigatórios";
        document.getElementById("campos-Error").innerHTML = camposError;
    //Caso os dois campos forem preenchidos é possivel armazená-los em lista para que sejam printados na tela do usuário
    } else if (!(document.getElementById('catOp').value == "") & !(document.getElementById('catAd').value == "")){
        let obj = {}
        obj.catOp = document.getElementById('catOp').value;
        obj.catAd = document.getElementById('catAd').value;
        listaHist.push(obj)


        var hist = "Cateto Oposto: " + obj.catOp + " Cateto Adjacente: " + obj.catAd;
        document.getElementById("resultado").innerHTML += `Cateto Oposto: ${obj.catOp} </br> Cateto Adjacente: ${obj.catAd} </br></br>`;
        //Chamada da função que vai realizar o calculo da hipotenusa
        calculo();
    }
}
function calculo() {
    var catOp = document.getElementById('catOp').value;
    var catAd = document.getElementById('catAd').value;
    var pitagoras = Math.pow((Math.pow(catOp, 2) + Math.pow(catAd, 2)), (1 / 2));
    document.getElementById("pitagoras").innerHTML = pitagoras;
    document.getElementById("oposto").innerHTML = catOp;
    document.getElementById("adjacente").innerHTML = catAd;
}
//Função que retorna uma alert para valores inválidos referente a um triângulo retângulo
function error() {
    alert("Não é pitagorico");
}