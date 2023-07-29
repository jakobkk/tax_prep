class W2:
    def __init__(self, **kwargs):
        self.b1 = kwargs['wage']
        self.b2 = kwargs['fed_withheld']
        self.b3 = kwargs['ss_wage']
        self.b4 = kwargs['ss_withheld']
        self.b5 = kwargs['medicare_wage']
        self.b6 = kwargs['medicare_withhyeld']
        for key,value in kwargs['box12'].items():
            self.b12[key] = value
        self.b15 = []
        self.b16 = []
        self.b17 = []
        for i in kwargs['state']:
            self.b15.append(i['name'])
            self.b16.append(i['wage'])
            self.b17.append(i['withheld'])
        self.b18 = []
        self.b19 = []
        self.b20 = []
        for i in kwargs['locality']:
            self.b18.append(i['wage'])
            self.b19.append(i['withheld'])
            self.b20.append(i['name'])
            