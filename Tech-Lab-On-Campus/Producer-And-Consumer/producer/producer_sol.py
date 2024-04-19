from producer_interface import mqProducerInterface


class mqProducer(mqProducerInterface):
    def __init__(self,routing_key: str, exchange_name: str)-> None:

        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection()





