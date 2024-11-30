from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.models.models import User, Role, Product, Category, Supplier, Sale
from app import db

bp = Blueprint('main', __name__)

@bp.route('/users', methods=['GET', 'POST'])
def manage_users():
    """
    Manage users.
    ---
    tags:
      - Users
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            email:
              type: string
            password:
              type: string
            role_id:
              type: integer
    responses:
      200:
        description: A list of users
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
              username:
                type: string
              email:
                type: string
      201:
        description: User created successfully
      400:
        description: Invalid input
    """
    if request.method == 'POST':
        data = request.json
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            role_id=data['role_id']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201

    users = User.query.all()
    users_data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify(users_data), 200


@bp.route('/products', methods=['GET', 'POST'])
def manage_products():
    """
    Manage products.
    ---
    tags:
      - Products
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            category_id:
              type: integer
            stock:
              type: integer
            price:
              type: number
    responses:
      200:
        description: A list of products
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
              name:
                type: string
              stock:
                type: integer
              price:
                type: number
      201:
        description: Product created successfully
      400:
        description: Invalid input
    """
    if request.method == 'POST':
        data = request.json
        new_product = Product(
            name=data['name'],
            category_id=data['category_id'],
            stock=data['stock'],
            price=data['price']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully'}), 201

    products = Product.query.all()
    products_data = [{'id': product.id, 'name': product.name, 'stock': product.stock, 'price': product.price} for product in products]
    return jsonify(products_data), 200


@bp.route('/suppliers', methods=['GET', 'POST'])
def manage_suppliers():
    """
    Manage suppliers.
    ---
    tags:
      - Suppliers
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            contact_info:
              type: string
    responses:
      200:
        description: A list of suppliers
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
              name:
                type: string
              contact_info:
                type: string
      201:
        description: Supplier created successfully
      400:
        description: Invalid input
    """
    if request.method == 'POST':
        data = request.json
        new_supplier = Supplier(
            name=data['name'],
            contact_info=data.get('contact_info')
        )
        db.session.add(new_supplier)
        db.session.commit()
        return jsonify({'message': 'Supplier created successfully'}), 201

    suppliers = Supplier.query.all()
    suppliers_data = [{'id': supplier.id, 'name': supplier.name, 'contact_info': supplier.contact_info} for supplier in suppliers]
    return jsonify(suppliers_data), 200


@bp.route('/sales', methods=['GET', 'POST'])
def manage_sales():
    """
    Manage sales.
    ---
    tags:
      - Sales
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            product_id:
              type: integer
            quantity:
              type: integer
            date:
              type: string
    responses:
      200:
        description: A list of sales records
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
              product_id:
                type: integer
              quantity:
                type: integer
              total_price:
                type: number
              date:
                type: string
      201:
        description: Sale recorded successfully
      400:
        description: Insufficient stock or invalid product
    """
    if request.method == 'POST':
        data = request.json
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
            return jsonify({'message': 'Sale recorded successfully'}), 201
        
        return jsonify({'error': 'Insufficient stock or invalid product'}), 400

    sales = Sale.query.all()
    sales_data = [{'id': sale.id, 'product_id': sale.product_id, 'quantity': sale.quantity, 
                   'total_price': sale.total_price, 'date': sale.date} for sale in sales]
    
    return jsonify(sales_data), 200


@bp.route('/', methods=['GET', 'POST'])
def holi():
    """
    Test route.
    ---
    tags:
      - Test
    responses:
      200:
        description: A simple greeting
      201:
        description: POST method received
    """
    if request.method == 'POST':
        return jsonify({'message': 'POST method received!'}), 201
    
    return "Hola desde Flask!", 200
