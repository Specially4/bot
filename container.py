from dao.order import OrderDAO
from db import session
from service.order import OrderService

order_dao = OrderDAO(session)
order_service = OrderService(order_dao)
