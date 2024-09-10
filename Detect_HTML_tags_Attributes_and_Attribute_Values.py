from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, att):
        print(tag)
        self.print_attributes(att)

    def print_attributes(self, att):
        for name, value in att:
            print(f'-> {name} > {value}')
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())