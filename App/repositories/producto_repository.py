from entities.producto import Producto as ProductoEntity
from models import db

class ProductoRepository:
    @staticmethod
    def listar_productos():
        return ProductoEntity.query.all()

    @staticmethod
    def buscar_producto_codigo(codigo):
        return ProductoEntity.query.filter_by(codigo=codigo).first()

    @staticmethod
    def eliminar(id_producto):
        producto = ProductoEntity.query.get(id_producto)
        if producto:
            coincidencia_ventas = db.session.query(db.exists().where(db.text(f"detalle_venta.producto = {id_producto}"))).scalar()
            if not coincidencia_ventas:
                db.session.delete(producto)
                db.session.commit()
                return True
        return False

    @staticmethod
    def modificar(producto: ProductoEntity):
        producto_to_update = ProductoEntity.query.get(producto.id_producto)
        if producto_to_update:
            producto_to_update.nombre = producto.nombre
            producto_to_update.descripcion = producto.descripcion
            producto_to_update.categoria = producto.categoria
            producto_to_update.precio_venta = producto.precio_venta
            producto_to_update.precio_compra = producto.precio_compra
            producto_to_update.codigo = producto.codigo
            producto_to_update.estado = producto.estado
            producto_to_update.stock = producto.stock
            producto_to_update.mayoreo = producto.mayoreo
            producto_to_update.precio_mayoreo = producto.precio_mayoreo
            producto_to_update.pieza_mayoreo = producto.pieza_mayoreo
            db.session.commit()
            return True
        return False

    @staticmethod
    def control_stock(id_producto, cantidad):
        product_to_update = ProductoEntity.query.get(id_producto)
        if product_to_update:
            product_to_update.stock += cantidad
            db.session.commit()
            return True
        return False

    @staticmethod
    def control_stock_cajas(id_producto, cantidad):
        product_to_update = ProductoEntity.query.get(id_producto)
        if product_to_update and product_to_update.mayoreo:
            product_to_update.stock += (cantidad * product_to_update.pieza_mayoreo)
            db.session.commit()
            return True
        return False

    @staticmethod
    def agregar(producto: ProductoEntity):
        db.session.add(producto)
        db.session.commit()
        return True

    @staticmethod
    def obtener_productos_totales_registrados():
        return ProductoEntity.query.count()

    @staticmethod
    def obtener_stock_completo():
        return db.session.query(db.func.sum(ProductoEntity.stock)).scalar() or 0

    @staticmethod
    def contar_productos_categoria(idcat):
        return ProductoEntity.query.filter_by(categoria=idcat).count()
