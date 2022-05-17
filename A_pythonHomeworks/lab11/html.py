
from abc import ABC,abstractmethod,abstractproperty
from typing import List



class Node(ABC):
    def __init__(self, attributes, content):
        self.__children=[]
        self.__attributes=attributes
        self.__content=content

    @property
    def content(self):
        return self.__content

    @property
    def children(self):
        return self.__children

    @property
    def attributes(self):
        return self.__attributes

    @abstractmethod
    def html(self):
        pass

class Html(Node):
    def html(self):
        str= '<Html>'
        str +=self.__content
        for k,v in self.attributes.items():
            str +=''+k+ '="'+v+'"'
            str +='>'

        str += '<Html>'

        return str

class Head(Node):
    def html(self):
        str= '<Head>'
        str +=self.__content
        for k,v in self.attributes.items():
            str +=''+k+ '="'+v+'"'
            str +='>'

        str += '<Head>'

        return str


class Body(Node):
    def html(self):
        str= '<Body>'
        str +=self.__content
        for k,v in self.attributes.items():
            str +=''+k+ '="'+v+'"'
            str +='>'

        str += '<Body>'

        return str


class Div(Node):
    def html(self):
        str= '<div>'
        str += self.__content
        for k,v in self.attributes.items():
            str +=''+k+ '="'+v+'"'
            str +='>'

        str += '<div>'

        return str

class Title(Node):
    def html(self):
        str= '<Title>'
        str +=self.__content
        for k,v in self.attributes.items():
            str +=''+k+ '="'+v+'"'
            str +='>'

        str += '<Title>'

        return str

class B(Node):
    def html(self):
        str= '<B>'
        str +=self.__content
        for k,v in self.attributes.items():
            str +=''+k+ '="'+v+'"'
            str +='>'

        str += '<B>'

        return str



class AbstractNodeFactory(ABC):
    @abstractmethod
    def makeNode(self,element, attr, content):
        pass


class StandardNodeFactory(AbstractNodeFactory):
    pass


class DebugNodeFactory(AbstractNodeFactory):
    pass



def main():
    divAtts = {}
    divAtts['id'] = 'first'
    divAtts['class'] = 'foo'
    divA = Div('This is a test A', divAtts)
    print(divA.html())

    divAtts = {}
    divAtts['id'] = 'second'
    divAtts['class'] = 'bar'
    divC = Div('This is a test B', divAtts)
    b = B()
    b.appendChild(divC)
    divAtts = {}
    divAtts['id'] = 'third'
    divAtts['class'] = 'dump'
    divC = Div('This is a test C', divAtts)

    body = Body()
    body.appendChild(divA)
    body.appendChild(b)
    body.appendChild(divC)
    title = Title('Example')
    head = Head()
    head.appendChild(title)
    html = Html()
    html.appendChild(head)
    html.appendChild(body)
    print(html.html())
if __name__ == "__main__":

    main()





