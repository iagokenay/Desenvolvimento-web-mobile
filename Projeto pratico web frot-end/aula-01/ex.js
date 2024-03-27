document.getElementById('soma').addEventListener('click', function() {
    const n1 = parseFloat(document.getElementById("n1").value);
    const n2 = parseFloat(document.getElementById("n2").value);

    const result = n1+n2;

    document.getElementById('resultado').innerText = "resultado: " + result;
    document.getElementById('resultado').style.color = "white";
    document.getElementById('resultado').style.margin = "15px";

});












