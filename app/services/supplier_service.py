from app.repositories.supplier_repository import SupplierRepository

class SupplierService:
    @staticmethod
    def list_suppliers():
        suppliers = SupplierRepository.get_all_suppliers()
        return [{'id': supplier.id, 'name': supplier.name, 'contact_info': supplier.contact_info} for supplier in suppliers]

    @staticmethod
    def add_supplier(data):
        return SupplierRepository.create_supplier(data)
