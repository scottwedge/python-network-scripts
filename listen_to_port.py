from argparse import ArgumentParser, SUPPRESS
import socket

def main():
    # Command Line Parser
    parser = ArgumentParser(add_help=False,description="Listen to a port on the current network")
    requiredArgs = parser.add_argument_group("required arguments")
    optionalArgs = parser.add_argument_group("optional arguments")
    # Adding All Command Line Arguments
    requiredArgs.add_argument("-p","--port",required=True,help="port to listen on")
    optionalArgs.add_argument("-h","--help",action="help",default=SUPPRESS,help="show this help message and exit")
    # Getting All Arugments
    args = vars(parser.parse_args())

    port = int(args["port"])

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'Sodcket successfully created')

        s.bind((socket.gethostname(), port))
        print(f'Socket binded to {port}')

        s.listen(5)
        print(f'Socket is listening')

        while True:
            clientsocket, address = s.accept()
            print(f"Connection from {address} has been established.")
            print(f"Sent a message to that address.")
            clientsocket.send(bytes("Hello!","utf-8"))
            clientsocket.close()

    except socket.error as err:
        print(f'Socket creation failed with error {err}')
    except:
        print(f'Unknown error has occured with Socket')


if __name__ == '__main__':
    main()
