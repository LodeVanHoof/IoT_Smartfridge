from fastapi import APIRouter
import database as db
import queries.queries as queries
from models.models import Content

router = APIRouter()

@router.post("/insert_content")
def create_product(new_content: Content):
    result = db.execute_sql_query(
        queries.insert_product_query,
        (new_content.name, new_content.expiration_date)
    )
    return result
@router.post("/remove_content")
def remove_product(product: Content):
    result = db.execute_sql_query(
        queries.remove_product_query,
        (product.name, product.expiration_date)
    )
    return result
@router.post("/warned_true")
def product_true(product: Content):
    result = db.execute_sql_query(
        queries.warned_query,
        (product.name, product.expiration_date)
    )
    return result