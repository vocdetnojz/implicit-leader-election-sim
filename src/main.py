from src.controller import Controller
import argparse
import sys

# T has no meaning in the code, since we don't have to wait for local calculations,
# latency is 0 and the nodes are 100% synchronized


if __name__ == '__main__':
    x = input('Choose simulation type: \n  1: the default 4-regular 2 level graph\n  2: graph given by you\n')
    try:
        x = int(x)
    except:
        sys.exit('Invalid input choice!')
    if x == 1:
        print('Simulation started...')
        b = input('Do you want to render the graph? (Y/N) ') in ('y', 'Y')
        ctrl = Controller(render=b, network_size=-1, connectivity=0, c1=3, c2=6)
        ctrl.run()
        pass
    elif x == 2:
        n = input('Please specify the number of nodes in your graph: ')
        c = input('Please specify the possibility of edge existence between two random nodes (0.0 to 1.0): ')
        b = input('Do you want to render the graph? (Y/N) ') in ('y', 'Y')
        c1 = input('Please specify constant c1: ')
        c2 = input('Please specify constant c2: ')
        try:
            n = int(n)
            c = float(c)
            c1 = float(c1)
            c2 = float(c2)
        except Exception as e:
            sys.exit('Invalid inputs: \n' + e)
        res = []
        if n < 1:
            res.append('Invalid graph size!')
        if c < 0.0 or c > 1.0:
            res.append('Invalid connection percentage!')
        if res:
            sys.exit('\n'.join(res))
        print('Simulation started...')
        ctrl = Controller(render=b, network_size=n, connectivity=c)
        ctrl.run()
    else:
        sys.exit('Invalid choice value!')

    pass
