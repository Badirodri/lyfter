# 1. Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#     1. Si el precio es menor a 100, el descuento es del 2%.
#     2. Si el precio es mayor o igual a 100, el descuento es del 10%.
#     3. *Ejemplos*:
#         1. 120 → 108
#         2. 40 → 39.2

precio_del_producto = int(input("Digite el precio del producto: "))
descuento = 0
precio_final = 0

if (precio_del_producto > 100):
    descuento= precio_del_producto * 0.1
    precio_final =  precio_del_producto - descuento
else:
    descuento= precio_del_producto * 0.02
    precio_final =  precio_del_producto - descuento

print(f"El precio final es de {precio_final}")