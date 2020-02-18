import numpy as np

true_w = np.array([1,2,3,4,5])
d = len(true_w)

sample = []
sample_num = 10
s = np.random.randn(5)
for i in range(sample_num):
    x = np.random.rand(d)
    sample.append((x, true_w.dot(x) + np.random.rand()))

def F(w, data):
    return sum(w.dot(x) - y for x,y in data)/len(data)

def dF(w, data):
    return sum(2*(w.dot(x) - y) * x for x,y in data)/len(data)

def gradient_discent(true_w,data,w):
    eta = 0.01
    for i in range(10000):
        w -= eta * dF(w,sample)
        if i%100==0:
            print(i,w)

w = np.random.randn(d)
#gradient_discent(true_w,sample,w)

def sF(w,data):
    x,y = data
    return w.dot(x) - y
def sdF(w,data):
    x,y = data
    return w*(w.dot(x)-y)*x
def stochastic_gradient_discent(true_w,data,w):
    eta = 0.03
    for i in range(10000):
        for x, y in data:
            w -= eta*sdF(w,(x,y))
        if i%100==0:
            print(i,w)

w2 = np.random.rand(d)
#stochastic_gradient_discent(true_w,sample,w2)

class GD:
    def __init__(self):
        self.true_w = np.array([1,2,3,4,5])
        self.d = len(self.true_w)
    def make_sample(self):
        self.sample = []
        for i in range(10000):
            x = np.random.randn(d)
            self.sample.append((x, self.true_w.dot(x) + np.random.rand()))
    def train(self, w, eta, iter):
        def dF(w,data):
            return sum(2*(w.dot(x)-y)*x for x,y in data)/len(data)
        
        for i in range(iter):
            w -= eta*dF(w,self.sample)
        return w

gd = GD()
gd.make_sample()
w3 = np.random.randn(5)
#print(gd.train(w3,0.01,1000))


class SGD:
    def __init__(self):
        self.true_w = np.array([1,2,3,4,5])
        self.d = len(self.true_w)
    def make_sample(self):
        self.sample = []
        for i in range(10000):
            x = np.random.randn(d)
            self.sample.append((x, self.true_w.dot(x) + np.random.rand()))
    def train(self, w, eta, iter):
        def sdF(w,data):
            x,y=data
            return 2*(w.dot(x)-y)*x
        
        for i in range(iter):
            for data in self.sample:
                w -= eta*sdF(w,data)
        return w
sgd = SGD()
sgd.make_sample()
w4 = np.random.randn(5)
print(sgd.train(w4,0.03,10))