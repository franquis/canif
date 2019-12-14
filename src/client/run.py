import can

can_interface = 'can0'
bus = can.interface.Bus(can_interface, bustype='socketcan')
message = bus.recv()