from app.models.models import Supplier
from app import db

class SupplierRepository:
    @staticmethod
    def get_all_suppliers():
        return Supplier.query.all()

    @staticmethod
    def create_supplier(data):
        new_supplier = Supplier(
            name=data['name'],
            contact_info=data.get('contact_info')
        )
        db.session.add(new_supplier)
        db.session.commit()
        return new_supplier
