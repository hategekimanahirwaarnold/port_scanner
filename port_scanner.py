import socket
import common_ports

def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSock:
            clientSock.settimeout(2)
            try: 
                if not clientSock.connect_ex((target, port)):
                    open_ports.append(port)
            except:
                if not target[0:3].isdigit():
                    return "Error: Invalid hostname"
                else:
                    return "Error: Invalid IP address"
    if verbose:
        host = ""
        try:
            if not target[:3].isdigit():
                host = socket.gethostbyname(target)
            else:
                host = target
                target, _, _ = socket.gethostbyaddr(target)
        except:
            host = ""
        response = f"Open ports for {target}" 
        if host != "":
            response += f" ({host})" 
        response += "\nPORT     SERVICE"
        for port in open_ports:
            space = 5 - len(str(port))
            white = ""
            for add in range(space):
                white += " "
            response += ("\n" + str(port)+ f"{white}    " + common_ports.ports_and_services[port])
        return response
    return(open_ports)