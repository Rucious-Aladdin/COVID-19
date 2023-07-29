import torch
import torch.nn as nn
import torch.optim as optim

def make_batch(): #입력을 한단위로 묶어줌.
    input_batch = []
    target_batch = []

    for sen in sentences:
        word = sen.split() #스페이스 단위로 쪼개서 리스트로 저장
        input = [word_dict[n] for n in word[:-1]] #[:-1] 마지막것을 제외한걸 말함
        # 단어를 숫자로 변환
        target = word_dict[word[-1]]
        #정답 -> 마지막하나를 숫자로 바꾼것
        input_batch.append(input)
        target_batch.append(target)

    return input_batch, target_batch

class NNLM(nn.Module): #nn.Module을 반드시 상속
    #위 뉴럴네트워크의 구조형태를 잘 파악하지 못하겠습니다.
    def __init__(self): #init, forward를 반드시 정의해 주어야 함.
        super(NNLM, self).__init__() #부모클래스의 init를 맨처음 실행
        self.C = nn.Embedding(n_class, m) #1번단어, 2번단어, .. 의 input에 대해서 어떤 벡터로 바꾸어주는 역할을 함.
        #단어 벡터를 학습을 통해 어떤 벡터값으로 변환
        self.H = nn.Linear(n_step * m, n_hidden, bias=False)
        #선형 레이어, dense레이어, 벡터에 행렬곱을 함 (입력벡터 차원, 출력 벡터 차원, bias=False)
        self.d = nn.Parameter(torch.ones(n_hidden))
        #파라미터 -> 학습을 시켜야 함.
        #별도의 학습할 파라미터로 지정함.
        self.U = nn.Linear(n_hidden, n_class, bias=False)
        self.W = nn.Linear(n_step * m, n_class, bias=False)
        self.b = nn.Parameter(torch.ones(n_class))

    def forward(self, X): #위 레이어들의 사용방식을 정의
        X = self.C(X) # X -> 입력, C(임베딩 메트릭스)에 X를 넣어줌.
        X = X.view(-1, n_step * m) #view함수의 기능이 무엇인지 잘 모르겠습니다.
        #형태는 그대로 두나, 3차원 배열이 2차원 배열로 바뀜(차원을 축소(?)) -1은 임의의 개수라는 의미임.
        tanh = torch.tanh(self.d + self.H(X))
        #매트릭스 곱과 파라미터를 더해줌 -> 거기에 하이퍼볼릭 tanh가 곱해짐.
        output = self.b + self.W(X) + self.U(tanh)
        #최종 output결과
        #W(X)가 스킵 커넥션이 있음.
        return output

if __name__ == '__main__': #가장 처음 실행되는 부분
    n_step = 2 #단어가 3개이니 앞에 2개를 보고 3번째것을 예측하기 때문에 2임.
    n_hidden = 2 #하이퍼 파라미터, 학습을 시작하기위해 정해주는 값들을 의미
    m = 2

    sentences = ["I like dog", "I like coffee", "i hate milk"]

    word_list = " ".join(sentences).split()
    word_list = list(set(word_list))
    word_dict = {w : i for i, w in enumerate(word_list)} #for문을 돌린결과를 딕셔너리로 반환
    #enumerate는 인덱스를 함께 튜플로 리턴해주는 특징이 있음.
    print(word_dict)

    number_dict = {i: w for i, w in enumerate(word_list)}
    n_class = len(word_dict)
    print(number_dict)

    model = NNLM()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    #잘 모르면 adam을 쓴다. -> lr을 자동으로 조정하는 기능이 있음.

    input_batch, target_batch = make_batch()
    input_batch = torch.LongTensor(input_batch)
    #파이토치 전용 자료형으로 변환
    target_batch = torch.LongTensor(target_batch)

    for epoch in range(5000):
        optimizer.zero_grad() #gradient를 0으로 초기화
        output = model(input_batch)

        loss = criterion(output, target_batch)
        if (epoch + 1) % 1000 == 0:
            print("Epoch:", "%04d" % (epoch + 1), "cost = ", "{:.6f}".format(loss))

        loss.backward()
        optimizer.step()

    predict = model(input_batch).data.max(1, keepdim=True)[1]
    #model(input_batch)를하면 어떤 함수가 실행되는 것인가요?
    # -> 내부적을 forward가 실행되게 되어있음.

    print([sen.split()[:2] for sen in sentences], '->', [number_dict[n.item()] for n in predict.squeeze()])
    #predict.squeeze()의 의미를 잘 모르겠습니다.