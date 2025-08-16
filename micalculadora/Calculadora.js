function probarCalculadora() {
    let deseaOtraOperacion = true;

    while (deseaOtraOperacion == true) {
        num1 = parseInt(prompt("Ingrese el primer número"));
        num2 = parseInt(prompt("Ingrese el segundo número"));
        operacion = (prompt("Ingrese una operación: suma, resta, multiplicacion, division"));
        resultado = realizarOperacion(num1, num2, operacion);
        alert("El resultado es: " + resultado);
        deseaOtraOperacion = confirm("¿Desea realizar otra operacion?");
    }
}

// funciones matematicas
function suma(num1, num2) {
    return num1 + num2;
}

function resta(num1, num2) {
    return num1 - num2;
}

function multiplicacion(num1, num2) {
    return num1 * num2;
}

function division(num1, num2) {
    return num2 != 0 ? num1 / num2 : "No se puede dividir entre 0";
}

function realizarOperacion(num1, num2, operacion) {
    if (operacion == "suma") {
        return resultado = suma(num1, num2);
    } else if (operacion == "resta") {
        return resultado = resta(num1, num2);
    } else if (operacion == "multiplicacion") {
        return resultado = multiplicacion(num1, num2);
    } else if (operacion == "division") {
        return resultado = division(num1, num2);
    } else {
        alert("Operación no valida");
    }
}