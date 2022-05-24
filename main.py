import src.mnist_loader as mnist
import src.network as network

def print_header():
    print('---------------------------------------------')
    print('\tFeedForward Nerual Network')
    print('---------------------------------------------')
    print()

def print_footer():
    print()
    print('---------------------------------------------')
    print('\t\t GOOD BYE')
    print('---------------------------------------------')

def main():
    print_header()
    training_data, validation_data, test_data = mnist.load_data_wrapper()
    net = network.Network([784, 30, 10])
    net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
    print_footer()


if __name__ == '__main__':
    main()


