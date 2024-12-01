from app.models.models import Sale, Product
from app import db

class SaleRepository:
    @staticmethod
    def get_all_sales():
        return Sale.query.all()

    @staticmethod
    def create_sale(data):
        product = Product.query.get(data['product_id'])
        if product and product.stock >= data['quantity']:
            product.stock -= data['quantity']
            sale = Sale(
                product_id=product.id,
                quantity=data['quantity'],
                total_price=data['quantity'] * product.price,
                date=data['date']
            )
            db.session.add(sale)
            db.session.commit()
            return sale
        return None
