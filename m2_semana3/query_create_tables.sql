CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    codigo VARCHAR(25) NOT NULL,
    nombre VARCHAR(25) NOT NULL,
    precio INT NOT NULL,
    fecha_ingreso  TIMESTAMP NOT NULL,
    marca VARCHAR(25) DEFAULT 'sin marca'
);


CREATE TABLE facturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    fecha_compra  TIMESTAMP NOT NULL,
    correo_comprador VARCHAR(25) NOT NULL,
    monto INT DEFAULT 0
);

CREATE TABLE detalle_facturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    factura_id  SMALLINT REFERENCES facturas(id),
    producto_id SMALLINT REFERENCES productos(id)
);

CREATE TABLE carrito_compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    factura_id  SMALLINT REFERENCES facturas(id),
    cantidad SMALLINT DEFAULT 0
);

CREATE TABLE carrito_productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    producto_id  SMALLINT REFERENCES productos(id),
    carrito_compra_id REFERENCES carrito_compras(id)
);
