class Context:
    def __init__(self):
        self.data = []
    
    def add_data(self, sentence):
        self.data.append(sentence)
    
    def get_data(self):
        return self.data
    
    def reset(self):
        self.data = []