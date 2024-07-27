import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn

# Load Data
# torch.utils.data.Dataset()
# torch.utils.data.DataLoader()


class MyDataset(Dataset):
    # read data and preprocess
    def __init__(self, file):
        # read data
        # preprocess
        self.data = file

    # return one sample at a time
    def __getitem__(self, index):
        return self.data[index]

    #  return the size of the dataset
    def __len__(self):
        return len(self.data)


# file = None
# dataset = MyDataset(file)
# # 5组数据合并成一个[mini_]batch
# dataloader = DataLoader(dataset, batch_size=5, shuffle=False)

# Define Neural Network
# torch.nn.Linear()
# nn.Sigmoid()
# nn.ReLU()


class MyModel(nn.Module):
    # Initialize you model
    def __init__(self):
        super(MyModel, self).__init__()
        # define layers
        self.net = nn.Sequential(
            nn.Linear(10, 32),
            nn.Sigmoid(),
            nn.Linear(32, 1)
        )

    # Compute output of your NN
    def forward(self, x):
        return self.net(x)


# Entire Procedure
# Neural Network Training Setup

# S_1
file = None
dataset = MyDataset(file)

# S_2
# 5组数据合并成一个[mini_]batch
dataloader = DataLoader(dataset, batch_size=5, shuffle=False)

# S_3
model = MyModel().to()  # device

# S_4
# Loss Function
model_output = None
expected_value = None
criterion = nn.CrossEntropyLoss()  # nn.MSELoss()
loss = criterion(model_output, expected_value)  # ======================

# S_5
# Optimization Algorithm
optimizer = torch.optim.SGD("")  # (model.parameters(), lr, momentum=0)
optimizer.zero_grad()
loss.backward()
optimizer.step()

# Neural Network Training Loop
n_epochs = 1000
for epoch in range(n_epochs):
    # set model to train model
    model.train()
    tr_set = []
    for x, y in tr_set:  # iterate through the dataloader
        optimizer.zero_grad()
        x, y = x.to(), y.to()
        pred = model(x)
        loss = criterion(pred, y)
        loss.backward()
        optimizer.step()

# Neural Network Validation Loop
# set model to test model
model.eval()
total_loss = 0
dv_set = []
for x, y in dv_set:  # iterate through the dataloader
    x, y = x.to(), y.to()  # move data to device (cpu / cuda)
    with torch.no_grad():  # disable gradient calculation  # 1 提升速度 2 防止模型参数修正
        pred = model(x)
        loss = criterion(pred, y)
    total_loss += loss.cpu().item() * len(x)
    # avg_loss = total_loss / len(dv_set.dataset)
