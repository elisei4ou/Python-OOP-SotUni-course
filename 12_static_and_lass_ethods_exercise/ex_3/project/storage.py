from typing import List

from ex_4.project import Category
from ex_4.project import Document
from ex_4.project import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    @staticmethod
    def add_obj_to_list(obj, list_with_obj):
        if obj not in list_with_obj:
            list_with_obj.append(obj)

    @staticmethod
    def search_by_id(_id, list_with_obj):
        result = next(filter(lambda x: x.id == _id, list_with_obj))
        return result

    def add_category(self, category: Category):
        self.add_obj_to_list(category, self.categories)

    def add_topic(self, topic: Topic):
        self.add_obj_to_list(topic, self.topics)

    def add_document(self, document: Document):
        self.add_obj_to_list(document, self.documents)

    def edit_category(self, category_id: int, new_name: str):
        category = self.search_by_id(category_id, self.categories)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.search_by_id(topic_id, self.categories)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.search_by_id(document_id, self.categories)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.search_by_id(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.search_by_id(topic_id, self.categories)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.search_by_id(document_id, self.categories)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.search_by_id(document_id, self.categories)
        return document

    def __repr__(self):
        result = [repr(x) for x in self.documents]
        return '\n'.join(result)

