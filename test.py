import tensorflow as tf

a = tf.Variable(tf.random_normal([1, 2], stddev=111))

init_op = tf.global_variables_initializer()

with tf.Session() as sess:

    sess.run(init_op)

    print(sess.run(a))

