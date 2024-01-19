var operacao="2"
function calcular() {
  var texto = document.getElementById("txt").value;
  var i=texto.indexOf("+");
  var i2=texto.indexOf("-");
  var i3=texto.indexOf("*");
  var i4=texto.indexOf("/");
  if(i==1){
    operacao="+";
  }
  if(i2==1){
    operacao="-";
  }
  if(i3==1){
    operacao="*";
  }
  if(i4==1){
    operacao="/";
  }
  var numeros=texto.split(operacao)
  var numero1=numeros[0]
  var numero2=numeros[1]
  var resultado = 0;
  document.getElementById("n1").innerHTML = numero1;
  document.getElementById("n2").innerHTML = numero2;
  document.getElementById("op").innerHTML = operacao;
  switch (operacao) {
    case "+":
      resultado = parseFloat(numero1) + parseFloat(numero2);
      break;
    case "-":
      resultado = parseFloat(numero1) - parseFloat(numero2);
      break;
    case "*":
      resultado = parseFloat(numero1) * parseFloat(numero2);
      break;
    case "/":
      resultado = parseFloat(numero1) / parseFloat(numero2);
      break;
  }
  document.getElementById("resultado").innerHTML = resultado;  
}
setInterval(calcular, 1)
