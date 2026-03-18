pedidos = []
sabores = [ 'vainilla','chocolate','fresa' ]
estadistica_sabores = []

print("Bienvenido a la heladeria riwi!")
print('Por favor eliga un sabor para su helado')

for i,sabor in enumerate(sabores):
    print(f'{i} - {sabor}')

for i in range(5):
    pedido = int(input('¿De que sabor desea el helado? '))
    pedidos.append(pedido)

for i,sabor in enumerate(sabores):
    estadistica_sabores.append({
        'sabor': sabor,
        'cantidad': pedidos.count(i+1)
    })
    
for s in estadistica_sabores:
    print(s)


