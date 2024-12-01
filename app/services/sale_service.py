from app.repositories.sale_repository import SaleRepository

class SaleService:
    @staticmethod
    def list_sales():
        sales = SaleRepository.get_all_sales()
        return [{'id': sale.id, 'product_id': sale.product_id, 'quantity': sale.quantity, 
                 'total_price': sale.total_price, 'date': sale.date} for sale in sales]

    @staticmethod
    def record_sale(data):
        return SaleRepository.create_sale(data)
