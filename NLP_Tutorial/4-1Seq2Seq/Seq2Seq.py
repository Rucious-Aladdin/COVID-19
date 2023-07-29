#seq2seq 구조 -> 문장으로 들어와서 문장으로 나가는 형태

import numpy as np
import torch
import torch.nn as nn

def make_batch():
    input_batch, output_batch, target_batch = [], [], []

    for seq in seq_data:
        for i in range(2):
            seq[i] = seq[i] + 'P' * (n_step - len(seq[i]))

        input = [num_dic[n] for n in seq[0]] #
        output = [num_dic[n] for n in ('S' + seq[1])] #S : start, E: end
        target = [num_dic[n] for n in (seq[1] + "E")]
        #teacher forcing -> 정답을 한꺼번에 일괄적으로 넣어서 처리. / 학습능률 향상.

        input_batch.append(np.eye(n_class)[input])
        output_batch.append(np.eye(n_class)[output])
        target_batch.append(target) # 정답은 정수로 처리

    return torch.FloatTensor(input_batch), torch.FloatTensor(output_batch), torch.LongTensor(target_batch)
    #앞의 둘은 내부적으로 처리하는 벡터라 float, 결과는 Long으로 출력됨

def make_testbatch(input_word):
    input_batch, output_batch = [], []

    input_w = input_word + "P" * (n_step - len(input_word))
    input = [num_dic[n] for n in input_w]
    output = [num_dic[n] for n in "S" + "P" * n_step]

    input_batch = np.eye(n_class)[input]
    output_batch = np.eye(n_class)[output]

    return torch.FloatTensor(input_batch).unsqueeze(0), torch.FloatTensor(output_batch).unsqueeze(0)

class Seq2Seq(nn.Module): #모델먼저
    def __init__(self):
        super(Seq2Seq, self).__init__()

        self.enc_cell = nn.RNN(input_size=n_class, hidden_size=n_hidden, dropout=0.5)
        self.dec_cell = nn.RNN(input_size=n_class, hidden_size=n_hidden, dropout=0.5)
        self.fc = nn.Linear(n_hidden, n_class)
        #2개의 RNN, 한개의 FC레이어.

    def forward(self, enc_input, enc_hidden, dec_input): #입력이 시퀀스, 출력또한 시퀀스로 들어감.
        enc_input = enc_input.transpose(0, 1) # 시간축을 앞으로 당긴것
        dec_input = dec_input.transpose(0, 1)

        _, enc_states = self.enc_cell(enc_input, enc_hidden) #
        outputs, _ = self.dec_cell(dec_input, enc_states)

        model = self.fc(outputs) # 마지막에 선형레이어에 넣어서 확률(relative)로 변함
        return model

if __name__ == "__main__":
    n_step = 5
    n_hidden = 128

    char_arr = [c for c in "SEPabcdefghijklmnopqrstuvwxyz"]
    num_dic = {n:i for i, n in enumerate(char_arr)}
    seq_data = [["man", "women"], ["black", "white"], ["king", "queen"], ["girl", "boy"], ["up", "down"], ["high", "low"]]

    n_class = len(num_dic)
    batch_size = len(seq_data)

    model = Seq2Seq()

    criterion = nn.CrossEntropyLoss() # logits의 처리를 위한 것.
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3) #

    input_batch, output_batch, target_batch = make_batch()

    for epoch in range(5000):
        hidden = torch.zeros(1, batch_size, n_hidden)

        optimizer.zero_grad()
        output = model(input_batch, hidden, output_batch)
        output = output.transpose(0, 1)
        loss = 0

        for i in range(0, len(target_batch)):
            loss += criterion(output[i], target_batch[i])
        if(epoch + 1) % 1000 == 0:
            print("Epoch: ", "%04d" % (epoch + 1), "cost= ", "{:.6f}".format(loss))

        loss.backward()
        optimizer.step()

    def translate(word):
        input_batch, output_batch = make_testbatch(word)

        hidden = torch.zeros(1, 1, n_hidden)
        output = model(input_batch, hidden, output_batch)

        predict = output.data.max(2, keepdim=True)[1]
        decoded = [char_arr[i] for i in predict]
        end = decoded.index("E")
        translated = ''.join(decoded[:end])

        return translated.replace("P", '')

    print("test")
    print("man ->", translate("man"))
    print("mans ->", translate("mans"))
    print("king ->", translate("king"))
    print("black ->", translate("black"))
    print("upp ->", translate("upp"))