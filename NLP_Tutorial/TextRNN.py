import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

def make_batch():
    input_batch = []
    target_batch = []

    for sen in sentences:
        word = sen.split()
        input = [word_dict[n] for n in word[:-1]]
        target = word_dict[word[-1]]

        input_batch.append(np.eye(n_class)[input])
        target_batch.append(target)

    return input_batch, target_batch

class TextRNN(nn.Module):
    def __init__(self):
        super(TextRNN, self).__init__()
        self.rnn = nn.RNN(input_size=n_class, hidden_size=n_hidden)
        self.W = nn.Linear(n_hidden, n_class, bias=False)
        self.b = nn.Parameter(torch.ones([n_class]))

    def forward(self, hidden, X):
        X = X.transpose(0, 1)
        outputs, hidden = self.rnn(X, hidden)
        outputs = outputs[-1]
        model = self.W(outputs) + self.b
        return model

if __name__ == "__main__":
    n_step = 2
    n_hidden = 5

    sentences = ["i like dog", "i love coffee", "i hate milk"]

    word_list = " ".join(sentences).split()
    word_list = list(set(word_list))
    word_dict = {w: i for i, w in enumerate(word_list)}
    number_dict = {i: w for i, w in enumerate(word_list)}
    n_class = len(word_dict)
    batch_size = len(sentences)

    model = TextRNN()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    input_batch, target_batch = make_batch()
    input_batch = torch.FloatTensor(input_batch)
    target_batch = torch.LongTensor(target_batch)

    for epoch in range(5000):
        optimizer.zero_grad()

        hidden = torch.zeros(1, batch_size, n_hidden)
        output = model(hidden, input_batch) #이 함수에 두변수를 주게되면 어떤 일이 일어나는지??
        #직접 쳐보면서 forward 밑에 return model 한줄을 빼먹었었는데 오류가 발생 제대로 실행되지 않았습니다.
        
        loss = criterion(output, target_batch)
        if (epoch + 1) % 1000 == 0:
            print("Epoch: ", "%04d" % (epoch + 1), "cost = ", "{:.6f}".format(loss))

        loss.backward()
        optimizer.step()

    input = [sen.split()[:2] for sen in sentences]

    hidden = torch.zeros(1, batch_size, n_hidden)
    predict = model(hidden, input_batch).data.max(1, keepdim=True)[1]
    print([sen.split()[:2] for sen in sentences], "->", [number_dict[n.item()] for n in predict.squeeze()])