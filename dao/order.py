from db import Order


class OrderDAO:
    def __init__(self, session):
        self.session = session

    def get_order(self, chat_id):
        return self.session.query(Order).filter(Order.chat_id == chat_id).one()

    def create_order(self, data):
        order = Order(**data)

        self.session.add(order)
        self.session.commit()
        return order

    def update_order(self, order):

        self.session.add(order)
        self.session.commit()
