from abc import ABC, abstractmethod

class DocumentHandler(ABC):

    @abstractmethod
    def get_info(self, file_path):
        pass
