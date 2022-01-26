# Dependency Inversion Principle
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def get_child_of(self, name):
        pass

class Relationships(RelationshipBrowser): # low level module
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def get_child_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r

class Research: # high level module
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'Jhon' and r[1] == Relationship.PARENT:
    #             print(f'Jhon is parent of {r[2].name}')
    def __init__(self, browser):
        for p in browser.get_child_of('Jhon'):
            print(f'Jhon is parent of {p[2].name}')

parent = Person('Jhon')
child1 = Person('Chris')
child2 = Person('Matt')
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)