import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  #隐藏提示警告
hello = tf.constant('pooooooooooooo')
sess = tf.Session()
print(sess.run(hello))

