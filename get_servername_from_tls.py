import os
import argparse
from scapy.all import rdpcap,load_layer,sniff




def retrieve_servername(packet):
    try:
        if packet.haslayer('TLS') and packet['TLS'].type == 22 and packet['TLS'].msg[0].msgtype == 1:
            msg = packet['IP'].src +' ==> ' +packet['IP'].dst +' : '+ (packet['TLS']['TLS_Ext_ServerName'].servernames[0].servername).decode("utf-8")
            print(msg)
            if output_file_name:
                f.write(msg +'\n') 
            
    except:
        pass

        
if __name__ == '__main__':
        
    # Construct the argument parser
    ap = argparse.ArgumentParser()

    # Add the arguments to the parser
    ap.add_argument("-f", "--filename", required=True,
    help="Input file name")

    ap.add_argument("-o", "--output-file", required=False,
    help="Output file name")
    args = vars(ap.parse_args())
    if args['output_file'] :
        global output_file_name 
        output_file_name = args['output_file']
        global f
        f = open(output_file_name, "a")
    filename = args['filename']
    load_layer("tls")
    a =' '
    sniff(offline=filename,prn=retrieve_servername,store=0)
    
    




    

