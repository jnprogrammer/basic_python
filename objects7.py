class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = '' #Doctype doesn't have an end tag

class Head(Tag):

    def __init__(self):
        super().__init__('head', '')

class Body(Tag):

    def __init__(self):
        super(Body, self).__init__('body', '')
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None ):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)

class HtmlDoc(object):

    def __init__(self, doc_type, head, body):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=None)
        print('<html>', file=None)
        self._head.display(file=None)
        self._body.display(file=None)
        print('</html>', file=None)


# if __name__ == '__main__':
#     my_page = HtmlDoc()
#     my_page.add_tag('h1', 'Main TITLE')
#     my_page.add_tag('h2', 'sub title')
#     my_page.add_tag('p', "This was made using composition one of the multiple examples of Polymorphism")
#
#     with open('test.html', 'w') as test_doc:
#         my_page.display(file=test_doc)


    # new_body=Body()
    # new_body.add_tag('h1', "Aggregation")
    # new_body.add_tag('p', "Unlike <strong>Composition</strong>, aggregation uses existing instances"
    #                  "of objects to build up another object")
    # new_body.add_tag('p', "The composed object doesn't actually own the objects that it's composed of"
    #                  "- if it's destroyed, those objects continue to exit.")
    #
    # new_docType = DocType()
    # #new_header = Head(new_docType, new_header, new_body)
    # my_page = HtmlDoc()
    #
    # with open('test2.html', 'w') as test_doc:
    #          my_page.display(file=test_doc)