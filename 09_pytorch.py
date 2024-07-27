# PyTorch
import torch

# version = torch.__version__
# available = torch.cuda.is_available()  # GPU是否可用
# print(f"torch版本：{version}")
# print(f"CUDA是否可用：{available}")

# scalar 标量---a
scalar = torch.tensor(7)
print(f"标量值为：{scalar}，类型为：{type(scalar)}，维度为：{scalar.ndim}")

# 张量->Python整数
scalar_num = scalar.item()
print(f"scalar_num值为：{scalar_num}，类型为：{type(scalar_num)}")

# vector 向量---y
vector = torch.tensor([7, 7])
print(f"vector的维度：{vector.ndim}，vector的形状：{vector.shape}")  # 外面方括号 ([) 的数量来判断一个张量的维数

# MATRIX 矩阵---Q
MATRIX = torch.tensor([[7, 8],
                       [9, 10]])  # ([7, 7])
print(f"matrix的维度：{MATRIX.ndim}，matrix的形状：{MATRIX.shape}")

# TENSOR 张量---X
TENSOR = torch.tensor([[[1, 2, 3],
                        [3, 6, 9],
                        [2, 4, 5]]])
print(f"tensor的维度：{TENSOR.ndim}，tensor的形状：{TENSOR.shape}，类型为：{type(TENSOR)}")

# 随机张量
random_tensor = torch.rand(size=(224, 224, 3))
print(f"random_tensor为：{random_tensor}\nrandom_tensor的数据类型：{random_tensor.dtype}")

# zeros_like()
zero_ten = torch.zeros_like(TENSOR)
print(zero_ten)

# 数据类型
float_32_tensor = torch.tensor([3.0, 6.0, 9.0], dtype=None, device=None, requires_grad=False)
# ==========================================================存储设备（CPU/GPU）   是否记录张量执行的操作
print(f"tensor的shape：{float_32_tensor.shape}，dtype：{float_32_tensor.dtype}，device：{float_32_tensor.device}")

float_16_tensor = torch.tensor([3.0, 6.0, 9.0], dtype=torch.float16, device=None, requires_grad=False)  # 是否记录张量执行的操作
print(f"tensor1的shape：{float_16_tensor.shape}，dtype：{float_16_tensor.dtype}，device：{float_16_tensor.device}")

# 乘法辨析
tensor = torch.tensor([1, 2, 3])
print(f"按元素乘法tensor * tensor结果为：{tensor * tensor}")
print(f"矩阵乘法tensor * tensor结果为：{tensor.matmul(tensor)}或者{torch.matmul(tensor, tensor)}")

# torch.mean() 要求张量是 torch.float32 （最常见的）或其他特定数据类型，否则操作将失败

# range替代为arange
# type更改数据类型
tensor = torch.arange(1.0, 10.0, 1)
print(tensor.dtype)
new_tensor = tensor.type(torch.float16)
print(new_tensor.dtype)

# .stack()--- 张量叠加
x = torch.arange(1.0, 8.0)
x_stack = torch.stack([x, x, x, x], dim=1)
print(x, x_stack)

# torch.squeeze()  # ---移除维度为 1 的行或列  (1, 2, 3) -> (2, 3)

# torch.permute(input, dims) 重新排列每个维度的顺序， 其中 input 维度变为dims
# 新张量与原始张量共享相同的数据

# torch.from_numpy(ndarray) - NumPy 数组 -> PyTorch 张量
# torch.Tensor.numpy() - PyTorch 张量 -> NumPy 数组
# 张量返回给 CPU 并可用于 NumPy，可以使用Tensor.cpu()
# 张量返回给 GPU  # x = x.to('cuda')



