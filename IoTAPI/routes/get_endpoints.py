from fastapi import APIRouter
import database as db
import queries.queries as queries

router = APIRouter()

@router.get("/get_content")
def get_content():
    result = db.execute_sql_query(queries.get_all_products_query)
    return result