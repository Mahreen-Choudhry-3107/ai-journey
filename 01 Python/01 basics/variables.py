# PYTHON VARIABLES 

# 1. VARIABLES & DATA TYPES

model_name = "ResNet50"       # str
epochs = 10                   # int
learning_rate = 0.001         # float
is_trained = False            # bool

print(model_name, type(model_name))
print(epochs, type(epochs))
print(learning_rate, type(learning_rate))
print(is_trained, type(is_trained))



# 2. INTEGER VS FLOAT

x = 5
y = 5.0

print(type(x))   # int
print(type(y))   # float

# 3. SWAPPING VARIABLES


train_acc = 0.91
val_acc = 0.87

train_acc, val_acc = val_acc, train_acc

print(train_acc)
print(val_acc)


# 4. = VS ==


threshold = 0.5

# =  means assignment
threshold = 0.5

# == means comparison
print(threshold == 0.5)   # True



# 5. VALID VARIABLE NAMES


model_2 = "CNN"          # Valid
_hidden_layer = 128      # Valid
batch_size = 32          # Valid

# 2nd_model = "CNN"      # Invalid: cannot start with number
# class = "CNN"          # Invalid: Python keyword
# learning-rate = 0.01   # Invalid: '-' is subtraction



# 6. LOCAL VARIABLE

def train_model():
    loss = 0.5
    print(loss)

train_model()

# loss cannot normally be accessed outside the function.



# 7. DYNAMIC TYPING


num_samples = 1000
print(type(num_samples))

num_samples = "1000"
print(type(num_samples))

# Python is dynamically typed.



# 8. MUTABLE LIST


weights = [0.2, 0.4, 0.6]

weights[0] = 0.9

print(weights)

# Lists are mutable.



# 9. MUTABLE VS IMMUTABLE


a = [1, 2, 3]
b = a

b.append(4)

print(a)
# [1, 2, 3, 4]

# a and b reference the same list.


a = 5
b = a

b += 1

print(a)
# 5

# Integers are immutable.



# 10. id()

x = [1, 2, 3]
y = x

print(id(x))
print(id(y))

print(x is y)   # True


# 11. ML HYPERPARAMETERS

learning_rate = 0.001
batch_size = 32
epochs = 20
optimizer = "Adam"

config = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 20,
    "optimizer": "Adam"
}

print(config["learning_rate"])
print(config["batch_size"])
print(config["epochs"])
print(config["optimizer"])


# 12. FORMAT ACCURACY

accuracy = 0.9423567

print(f"Accuracy: {accuracy:.2%}")
# Accuracy: 94.24%


# 13. MULTIPLE ASSIGNMENT


metrics = (0.85, 0.12, 0.91)

precision, loss, recall = metrics

print(precision)
print(loss)
print(recall)



# 14. STAR UNPACKING


layer_sizes = [128, 64, 32, 10]

first, *hidden, last = layer_sizes

print(first)    # 128
print(hidden)   # [64, 32]
print(last)     # 10


# 15. MUTABLE DEFAULT ARGUMENT — IMPORTANT


def train(data, results=None):
    if results is None:
        results = []

    results.append(data)
    return results

print(train("batch1"))
print(train("batch2"))

# Using None prevents the same list from being reused.


# 16. is VS ==


a = 256
b = 256

print(a == b)   # True
print(a is b)   # Identity check — implementation dependent

# Use == when comparing values.
# Use is when checking object identity.
