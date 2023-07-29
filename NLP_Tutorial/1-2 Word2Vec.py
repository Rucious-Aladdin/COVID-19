import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("TkAgg")

def random_batch():
    random_inputs = []
    random_labels = []
    random_index = np.random.choice(range(len(skip_grams)), batch_size, replace=False)

    for i in random_index:
        random_inputs.append(np.eye(voc_size)[skip_grams[i][0]])
        #np.eye -> 항등행렬을 만듬
        random_labels.append(skip_grams[i][1])
        #한 행씩 뽑아쓸 수 있도록 함.

    return random_inputs, random_labels

class Word2Vec(nn.Module): #같은단어들 사이에 오는 벡터는 비슷하다는 가정을 바탕으로 설계 됨.
    def __init__(self):
        super(Word2Vec, self).__init__()
        self.W = nn.Linear(voc_size, embedding_size, bias=False)
        self.WT = nn.Linear(embedding_size, voc_size, bias=False)

    def forward(self, X):
        hidden_layer = self.W(X)
        output_layer = self.WT(hidden_layer) #output에 단어가 올 확률을 계산하게 됨.
        return output_layer

if __name__ == "__main__":
    batch_size = 2
    embedding_size = 2

    sentences = ["apple banana fruit", "banana orange fruit", "orange banana fruit",
                 "dog cat animal", "cat monkey animal", "monkey dog animal"]

    word_sequence = " ".join(sentences).split()
    print(word_sequence)
    word_list = " ".join(sentences).split()
    word_list = list(set(word_list))
    word_dict = {w: i for i, w in enumerate(word_list)}
    voc_size = len(word_list)

    #입력을 만드는 부분이 다름
    skip_grams = []
    for i in range(1, len(word_sequence) - 1): #가운데 있는 단어를 찾게됨.
        target = word_dict[word_sequence[i]]
        context = [word_dict[word_sequence[i-1]], word_dict[word_sequence[i+1]]]
        for w in context:
            skip_grams.append([target, w])

    print(skip_grams)

    model = Word2Vec()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(10000):
        input_batch, target_batch = random_batch()
        input_batch = torch.Tensor(input_batch)
        target_batch = torch.LongTensor(target_batch)

        optimizer.zero_grad()
        output = model(input_batch)

        loss = criterion(output, target_batch)
        if(epoch +1) % 1000 == 0:
            print("Epoch:", "%04d" % (epoch + 1), "cost = ", "{:.6f}".format(loss))

        loss.backward()
        optimizer.step()

    for i, label in enumerate(word_list):
        W, WT = model.parameters()
        x, y = W[0][i].item(), W[1][i].item()
        plt.scatter(x, y)
        plt.annotate(label, xy=(x, y), xytext=(5, 2), textcoords="offset points", ha="right", va="bottom")

    plt.show()