import numpy as np
import torch 
import torch.nn as nn 
import torch.optim as optim 

np.random.seed(12)
torch.manual_seed(12)

class HyperParameter(object):
    def __init__(self):
        #do not change vocab_size, embeded_size 
        self.vocab_size = 250 
        self.embedded_size = 50
        self.batch_size = 1 

        #########TODO###########
        
        self.hidden_size =  200
        self.epoch = 3
        self.learning_rate = 0.01
        self.data_path = "./data/input/"

        ########################

class LSTM(nn.Module):
    def __init__(self, param):
        super(LSTM, self).__init__()

        #########TODO###########
        
        self.embedding_layer = nn.Embedding(param.vocab_size,param.embedded_size)
        self.lstm_layer = nn.LSTM(param.embedded_size,param.hidden_size)
        self.output_layer = nn.Linear(param.hidden_size,param.vocab_size)
        
        #######################

        self.softmax_layer = nn.Softmax()

    def forward(self, x):

        ##########TODO###########
        
        x = self.embedding_layer(x)
        outputs = self.lstm_layer(embeds)

        ########################


        final_output = self.softmax_layer(self.output_layer(outputs[:, -1, :]))    
        return final_output



#convert branch address to int value 
def data_load(data_path):
    br_addr_a = [] #list of converted attack branch address 
    br_addr_n = [] #list of converted normal branch address
    
    ###TODO##################

    temp_arr_a = []
    temp_arr_n = []
    normal = open(data_path+"small.refined.normal",data="r",encoding="utf-8")
    attack = open(data_path+"small.refined.attack",data="r",encoding="utf-8")
    
    while True:
        normal_line = normal.readline().rstrip()
        attack_line = attack.readline().rstrip()
        
        if not normal_line or not attack_line :
            break
        
        int_n = -1
        int_a = -1
        
        for index,item in enumerate(temp_arr_n):
            if item == normal_line:
                int_n = index


        for index,item in enumerate(temp_arr_a):
            if item == attack_line:
                int_a = index
        
        if int_n == -1:
            int_n = len(temp_arr_n)
            temp_arr_n.append(normal_line)
                
        if int_a == -1:
            int_a = len(temp_arr_a)
            temp_arr_a.append(attack_line)
    
        br_addr_a.append(int_a)
        br_addr_n.append(int_n)


    ########################

    return torch.tensor(br_add_a, dtype=torch.long), torch.tensor(br_add_n, dtype=torch.long)


def to_one_hot(data, param):
    ###TODO###################
    zero = np.zeros(param. ,param. ,dtype=int)




    ##########################

    return one_hot



def train(model, device, train_input, train_output, optimizer, criterion, epoch):
    model.train()

    #####TODO#################
   


    #############################

    print('Train epoch: {}, Loss: {:.6f}'.format(epoch, loss.item()))



def test(model, device, test_input, test_output, criterion):
    model.eval()

    ####TODO#####################
    test_loss = 0
    correct = 0

    with torch.no_grad():
        for data,target in test

    

    ###############################
    print('Test Loss: {:.6f}'.format(loss.item()))



if __name__ == '__main__':
    param = HyperParameter()
    epochs = param.epoch
    lr = param.learning_rate 


    #########TODO###################
    data_a, data_n = data_load(param.data_path)
    

    train_input = 
    train_output = 

    test_input = 
    test_output = 

    device = torch.device('cpu')
    model = LSTM(param).to(device)
    optimizer = 
    criterion = nn.BCELoss()
    
    
    for epoch in range(0, epochs):
        train(model, device, train_input, train_output, optimizer, criterion, epoch)

    test(model, device, test_input, test_output, criterion)


    ##########################################
