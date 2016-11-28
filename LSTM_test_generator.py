import keras
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
import sys
import os


def get_best_model():
    files = list(os.listdir('tmp'))
    if not files:
        return None
    best_epoch = 0
    best_file = files[0]
    for file_ in files:
        epoch_number = int(file_.split('-')[2])
        if epoch_number > best_epoch:
            best_epoch = epoch_number
            best_file = file_
    return best_file


filename = "zaratustra_clear.txt"
raw_text = open(filename).read()
for sym in '0123456789-"':
    raw_text = raw_text.replace(sym, '')
raw_text = raw_text.replace('?', '')
# create mapping of unique chars to integers
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
print(chars)

n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)

# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
    seq_in = raw_text[i:i + seq_length]
    seq_out = raw_text[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)

# reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
# normalize
X = X / float(n_vocab)
# one hot encode the output variable
y = np_utils.to_categorical(dataY)

# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

int_to_char = dict((i, c) for i, c in enumerate(chars))
# load the network weights
filename = get_best_model()
if filename:
    model.load_weights(os.path.join('tmp', filename))
model.compile(loss='categorical_crossentropy', optimizer='adam')


class Generate(keras.callbacks.Callback):
    def on_epoch_begin(self, epoch, logs={}):
        # pick a random seed
        start = numpy.random.randint(0, len(dataX) - 1)
        pattern = dataX[start]
        print("epoch: {} Seed: {}".format(epoch, ''.join([int_to_char[value] for value in pattern])))
        # generate characters
        for i in range(1000):
            x = numpy.reshape(pattern, (1, len(pattern), 1))
            x = x / float(n_vocab)
            prediction = model.predict(x, verbose=0)
            index = numpy.argmax(prediction)
            result = int_to_char[index]
            seq_in = [int_to_char[value] for value in pattern]
            sys.stdout.write(result)
            pattern.append(index)
            pattern = pattern[1:len(pattern)]
        print("\nDone.")


def train():
    # define the checkpoint
    file_path = "tmp/weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
    checkpoint = ModelCheckpoint(file_path, monitor='loss', verbose=1, save_best_only=True, mode='min')
    generate = Generate()
    callbacks_list = [checkpoint, generate]

    model.fit(X, y, nb_epoch=20, batch_size=128, callbacks=callbacks_list)


train()
