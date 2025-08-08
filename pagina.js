function achocolatado(marca, quantidade, valorvenda, preco){
    this.marca = marca;
    this.quantidade = quantidade;
    this.valorvenda = valorvenda;
    this.preco = preco;
}
    let todi = new achocolatado("todi", 100, 10, 7);
let produtos = [];

function onload(){
    let todi = new achocolatado("todi", 100, 10, 7);
produtos.push(todi)
}

function test(){
for (prop in todi){
    let  text = document.createElement("span");
text.innerText =" " + todi[prop];
document.body.appendChild(text);

    
}

}