from abc import ABC, abstractmethod
import enum


class AbstractParserFactory(ABC):
    @classmethod
    def factory_display(cls):
        factory = cls.get_parser_instance()

    @abstractmethod
    def get_parser_instance():
        print("-- get_parser_instance is not implemented")


class AmazonParserFactory(AbstractParserFactory):

    def get_parser_instance(self):
        return AmazonParserFactory()


class FlipkartParserFactory(AbstractParserFactory):

    def get_parser_instance(self):
        return FlipkartParserFactory()





class FactoryEnum(Enum):
    amazon = AmazonParserFactory
    flipkart = FlipkartParserFactory


if __name__ == "__main__":
    factory_list = ['amazon', 'flipkart']
