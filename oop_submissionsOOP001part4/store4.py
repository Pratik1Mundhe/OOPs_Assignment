class Item:
    def __init__(self,name,price, category):
        if price <=0:
            raise ValueError(f"ValueError: Invalid value for price, got {price}")
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f'{self.name}@{self.price}-{self.category}'
    


class Query:
    def __init__(self, field, operation, value):
        self.field = field
        self.operation = operation
        self.value = value

    def __str__(self):
        return f'{self.field} {self.operation} {self.value}'
    


class Store:
    res = []
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def filter(self, query):
        result = []
        for item in self.items:
            itemAttr = getattr(item, query.field)
            if query.operation == 'EQ':
                if itemAttr == query.value:
                    result.append(item)
            elif query.operation == 'GT':
                if itemAttr > query.value:
                    result.append(item)
            elif query.operation == 'GTE':
                if itemAttr >= query.value:
                    result.append(item)
            elif query.operation == 'LT':
                if itemAttr < query.value:
                    result.append(item)
            elif query.operation == 'LTE':
                if itemAttr <= query.value:
                    result.append(item)
            elif query.operation == 'IN':
                for  i in query.value:
                    if itemAttr == i:
                        result.append(item)
            elif query.operation == 'CONTAINS':
                if query.value in itemAttr:
                    result.append(item)
            elif query.operation == 'ENDS_WITH':
                if itemAttr.endswith(query.value):
                    result.append(item)
            elif query.operation == 'STARTS_WITH':
                if itemAttr.startswith(query.value):
                    result.append(item)

        self.res = result
        return result

    def exclude(self,query):
        self.filter(query)
        res1 = []
        for item in self.items:
            if item not in self.res:
                res1.append(item)
        
        return res1
            