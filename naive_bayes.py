class NaiveBayes():

    def __init__(self, data):
        self.data = data
        self.ind_var = list(self.data.keys())[0]
        self.dep_vars = list(self.data.keys())[1:]
        self.ind_var_data = self.data[self.ind_var]
        self.classes = self.get_classes()

    def get_classes(self):
        classes = [data_point for i, data_point in enumerate(self.ind_var_data) if data_point not in self.ind_var_data[0:i]]
        return sorted(classes, key = lambda one_class: self.ind_var_data.count(one_class))

    def predict(self, test_data):
        predictions = []
        for test_data_index in range(len(list(test_data.values())[0])):
            test_data_point = {variable : test_data[variable][test_data_index] for variable in self.dep_vars}
            predictions.append(self.predict_data_point(test_data_point))
        return predictions
    
    def predict_data_point(self, test_data_point):
        
        p = {variable:{one_class:0 for one_class in self.classes} for variable in list(self.data.keys())}
        
        for one_class in self.classes:
            
            p[self.ind_var][one_class] = self.ind_var_data.count(one_class) / len(self.ind_var_data)
            
            for i, ind_var_data_point in enumerate(self.ind_var_data):
                if ind_var_data_point == one_class:
                    for variable in test_data_point:
                        if self.data[variable][i] == test_data_point[variable]:
                            p[variable][one_class] += (1 / self.ind_var_data.count(one_class))
            
            for count in p.values():
                p[self.ind_var][one_class] *= count[one_class]
            
            p[self.ind_var][one_class] = round(p[self.ind_var][one_class], 3)
        
        temp = [p[self.ind_var][one_class] for one_class in self.classes]
        
        for one_class in self.classes:
            if p[self.ind_var][one_class] == max(temp):
                return one_class