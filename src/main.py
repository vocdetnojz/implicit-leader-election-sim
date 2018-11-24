from src.controller import Controller


# T has no meaning in the code, since we don't have to wait for local calculations,
# latency is 0 and the nodes are 100% synchronized


if __name__ == '__main__':
    ctrl = Controller()
    ctrl.run()
    pass
