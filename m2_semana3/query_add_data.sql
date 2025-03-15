-- QUERIES INSERT

-- INSERT INTO productos (codigo, nombre, precio, fecha_ingreso, marca)
-- 	VALUES ('ZZ3Y7JQ9', 'printer', 12325, '2024-09-27', 'sony');

-- INSERT INTO productos (codigo, nombre, precio, fecha_ingreso, marca)
-- 	VALUES ('ZZ3Y7JQ2', 'printer 2', 1230, '2024-09-27', 'sony');

-- INSERT INTO productos (codigo, nombre, precio, fecha_ingreso, marca)
-- 	VALUES ('ZZ3Y7J25', 'TV', 125000, '2024-09-28', 'test');

-- INSERT INTO productos (codigo, nombre, precio, fecha_ingreso)
-- 	VALUES ('ZZ3Y7215', 'TV smart', 225000, '2024-09-28');

-- INSERT INTO facturas (fecha_compra, correo_comprador, monto, telefono_comprador, codio_empleado)
-- 	VALUES ('2025-02-18', 'test@gmail.com', 351000, 24532020, 'Pedrito506');

-- INSERT INTO facturas (fecha_compra, correo_comprador, monto, telefono_comprador, codio_empleado)
-- 	VALUES ('2025-02-19', 'test@gmail.com', 51000, 24532020, 'Pedrito506');

-- INSERT INTO facturas (fecha_compra, correo_comprador, monto, telefono_comprador, codio_empleado)
-- 	VALUES ('2025-03-12', 'test2@gmail.com', 5000, 22532121, 'Maria506');

-- INSERT INTO carrito_compras (factura_id, cantidad)
-- 	VALUES (1,4);

-- INSERT INTO carrito_compras (factura_id, cantidad)
-- VALUES (2,3);

-- INSERT INTO detalle_facturas (factura_id, producto_id)
-- VALUES (1,2);

-- INSERT INTO detalle_facturas (factura_id, producto_id)
-- VALUES (2,4);


-- QUERIES SELECT
-- Obtenga todos los productos almacenados

SELECT *
FROM productos;

-- Obtenga todos los productos que tengan un precio mayor a 50000

SELECT *
FROM productos
WHERE precio > 5000;

-- Obtenga todas las compras de un mismo producto por id.

SELECT *
FROM productos
JOIN detalle_facturas ON productos.id = detalle_facturas.producto_id
JOIN facturas ON detalle_facturas.factura_id = facturas.id
WHERE producto_id in (1,2);

SELECT *
FROM productos
JOIN detalle_facturas ON productos.id = detalle_facturas.producto_id
JOIN facturas ON detalle_facturas.factura_id = facturas.id
WHERE producto_id = 1;



-- Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.

SELECT productos.nombre, facturas.monto
FROM productos
JOIN detalle_facturas ON productos.id = detalle_facturas.producto_id
JOIN facturas ON detalle_facturas.factura_id = facturas.id;

-- Obtenga todas las facturas realizadas por el mismo comprador

SELECT *
FROM facturas
WHERE correo_comprador='test@gmail.com';

-- Obtenga todas las facturas ordenadas por monto total de forma descendente

SELECT *
FROM facturas
ORDER BY monto DESC;

-- Obtenga una sola factura por número de factura.

SELECT *
FROM facturas
where id=1