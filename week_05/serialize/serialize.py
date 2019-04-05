import json
import dicttoxml
class Jsonable:
    def to_json(self, indent = 4):
        dc = {'dict' : self.__dict__, 'type' : str(type(self).__name__)}
        return json.dumps(dc, indent = indent, sort_keys = True)


    @classmethod
    def from_json(cls, json_string):
        dc = json.loads(json_string)
        data = dc['dict']
        print(cls(**data))


class Xmlable:
    def to_xml(self):
        return dicttoxml.dicttoxml(self.__dict__)

    @classmethod
    def from_xml(cls, xml_string):
        pass

class Panda(Jsonable, Xmlable):
    def __init__(self, name):
        self.name = name

def main():
    p = Panda('ivo')
    js = p.to_json()
    print(Panda.from_json(js))
    print(p.to_xml())


if __name__ == '__main__':
    main()