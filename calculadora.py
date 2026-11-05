def sumar(a, b):    
    return a + b
def restar(a, b):    
    return a - b
def multiplicar(a, b):    
    return a * b
def dividir(a, b):    
    if b == 0:        
        raise ValueError("No se puede dividir entre cero")    
    return a / b

if __name__ == "__main__":    
    print("CALCULADORA MATEMATICA")    
    print("Suma:", sumar(20, 10))    
    print("Resta:", restar(20, 10))    
    print("Multiplicacion:", multiplicar(20, 10))    
    print("Division:", dividir(20, 10))