from dao.order import OrderDAO


class OrderService:
    def __init__(self, dao: OrderDAO):
        self.dao = dao

    def get_order(self, chat_id):
        return self.dao.get_order(chat_id)

    def create_order(self, data: dict):
        return self.dao.create_order(data)

    def update_order(self, data: dict):
        cid = data['chat_id']
        order = self.get_order(cid)

        if 'path' in data:
            order.path = data['path']
        if 'url' in data:
            order.url = data['url']

        self.dao.update_order(order)
        return order
