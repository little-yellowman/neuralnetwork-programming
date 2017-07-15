import tensorflow as tf

batch_size=1
input_height = 3
input_width = 3
input_channels = 1


def main():
    sess = tf.InteractiveSession()
    layer_input = tf.constant([
            [
                [[1.0], [0.2], [2.0]],
                [[0.1], [1.2], [1.4]],
                [[1.1], [0.4], [0.4]]
            ]
        ])

    # The strides will look at the entire input by using the image_height and image_width
    kernel = [batch_size, input_height, input_width, input_channels]
    max_pool = tf.nn.max_pool(layer_input, kernel, [1, 1, 1, 1], "VALID")
    print(sess.run(max_pool))

if __name__ == '__main__':
  main()