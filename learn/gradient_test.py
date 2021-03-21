#!/home/justin/.venv/learn/bin/python
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def f(t):
    return t**2


t = tf.linspace(-5.0, 5.0, 1001)

with tf.GradientTape() as tape:
    tape.watch(t)
    y = f(t)
    gradient = tape.gradient(y, t)
    plt.plot(t, y)
    plt.plot(t, gradient)
    plt.show()
