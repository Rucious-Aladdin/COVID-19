import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("TkAgg")


def make_batch():
    input_batch = [np.eye(n_class)[[word_dict[n] for n in sentences[0].split()]]]
    output_batch = [np.eye(n_class)[[word_dict[n] for n in sentences[1].split()]]]
    target_batch = [[word_dict[n] for n in sentences[2].split()]]

    return torch.FloatTensor(input_batch), torch.FloatTensor(output_batch), torch.LongTensor(target_batch)

class Attention(nn.Module):
    def __init__(self):
        super(Attention, self).__init__()
        self.enc_cell = nn.RNN(input_size=n_class, hidden_size=n_hidden, dropout=0.5)
        self.dec_cell = nn.RNN(input_size=n_class, hidden_size=n_hidden, dropout=0.5)

        self.attn = nn.Linear(n_hidden, n_hidden) # 어텐션 레이어 추가, 인코더 아웃풋도 사용함.
        self.out = nn.Linear(n_hidden * 2, n_class)

    def forward(self, enc_inputs, hidden, dec_inputs):
        enc_inputs = enc_inputs.transpose(0, 1)
        dec_inputs = dec_inputs.transpose(0, 1)

        enc_outputs, enc_hidden = self.enc_cell(enc_inputs, hidden)

        trained_attn = []
        hidden = enc_hidden
        n_step = len(dec_inputs)
        model = torch.empty([n_step, 1, n_class])

        for i in range(n_step):
            dec_output, hidden = self.dec_cell(dec_inputs[i].unsqueeze(0), hidden)
            # dec_inputs의 i번째 인풋을 넣어줌.
            attn_weights = self.get_att_weight(dec_output, enc_outputs)
            trained_attn.append(attn_weights.squeeze().data.numpy())

            context = attn_weights.bmm(enc_outputs.transpose(0, 1))
            # 행렬곱 처리.
            dec_output = dec_output.squeeze(0)
            context = context.squeeze(1)
            model[i] = self.out(torch.cat((dec_output, context), 1))

        return model.transpose(0, 1).squeeze(0), trained_attn
    # 모델의 정확성이 높아지나 연산량이 늘어남. 어텐션을 쓰지 않는 메커니즘에 비해서 리니어 레이어의 차원이 2배임.

    def get_att_weight(self, dec_output, enc_outputs):
        n_step = len(enc_outputs)
        attn_scores = torch.zeros(n_step)

        for i in range(n_step):
            attn_scores[i] = self.get_att_score(dec_output, enc_outputs[i])

        return F.softmax(attn_scores).view(1, 1, -1)

    def get_att_score(self, dec_output, enc_output):
        score = self.attn(enc_output)
        return torch.dot(dec_output.view(-1), score.view(-1))

if __name__ == "__main__":
    n_step = 5
    n_hidden = 128

    sentences = ["ich mochte ein bier P", "S i want a beer", "i want a beer E"]

    word_list = " ".join(sentences).split()
    word_list = list(set(word_list))
    word_dict = {w: i for i, w in enumerate(word_list)}
    number_dict = {i: w for i, w in enumerate(word_list)}
    n_class = len(word_dict)

    hidden = torch.zeros(1, 1, n_hidden)

    model = Attention()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    input_batch, output_batch, target_batch = make_batch()

    for epoch in range(2000):
        optimizer.zero_grad()
        output, _ = model(input_batch, hidden, output_batch)

        loss = criterion(output, target_batch.squeeze(0))
        if (epoch + 1) % 400 == 0:
            print("Epoch: ", "%04d" % (epoch + 1), "cost =", "{:.6f}".format(loss))

        loss.backward()
        optimizer.step()

    test_batch = [np.eye(n_class)[[word_dict[n] for n in "SPPPP"]]]
    test_batch = torch.FloatTensor(test_batch)
    predict, trained_attn = model(input_batch, hidden, test_batch)
    predict = predict.data.max(1, keepdim=True)[1]
    print(sentences[0], "->", [number_dict[n.item()] for n in predict.squeeze()])

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1, 1, 1)
    ax.matshow(trained_attn, cmap="viridis")
    ax.set_xticklabels([" "] + sentences[0].split(), fontdict={"fontsize" : 14})
    ax.set_yticklabels([" "] + sentences[2].split(), fontdict={"fontsize" : 14})
    plt.show()