from faunadb import query as q
from flask_restx import inputs, reqparse

list_products_args = reqparse.RequestParser()
list_products_args.add_argument(
    'name',  required=False, case_sensitive=True,
    help='Partial name of product', store_missing=False
)
list_products_args.add_argument(
    'category', required=False, store_missing=False,
    help='Category id to fetch products from'
)
list_products_args.add_argument(
    'sort_by', required=False,
    choices=['name_asc', 'price_asc', 'price_desc'], store_missing=False, 
    default='name_asc', help='Sort products by some values'
)
list_products_args.add_argument(
    'per_page', type=int, required=False,
    choices=[5, 10, 20, 30, 40, 50], store_missing=False, 
    default=5, help='Results per page {error_msg}'
)


create_product_args = reqparse.RequestParser()
create_product_args.add_argument('name', location="form", required=True)
create_product_args.add_argument('price', location="form", type=inputs.positive, required=True)
create_product_args.add_argument('quantity', location="form", type=inputs.positive, required=True)
create_product_args.add_argument('categories', location="form", action='append', required=True)


update_product_args = reqparse.RequestParser()
update_product_args.add_argument('name', location='form',store_missing=False)
update_product_args.add_argument('price', location='form', store_missing=False, type=inputs.positive)
update_product_args.add_argument('quantity', location='form', store_missing=False, type=inputs.positive)
update_product_args.add_argument("categories", location='form', store_missing=False, action="append")

