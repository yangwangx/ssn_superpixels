from init_caffe import *
from create_net import load_ssn_net

models = [
    './models/ssn_bsds_model.caffemodel',
    # './models/ssn_cityscapes_model.caffemodel',
    # './models/ssn_sintel_model.caffemodel',
    # './models/ssn_voc_model.caffemodel',
]

for caffe_model in models:
    net = load_ssn_net(201, 201, 100, 1.0, 1.0, 10, 10, 5)
    net.copy_from(caffe_model)

    layers = sorted(net.params.keys())
    # conv layers
    conv_params = []
    for layer in layers:
        if 'Convolution' in layer:
            print(layer)
            conv_params.append(net.params[layer][0].data)
            conv_params.append(net.params[layer][1].data)

    # bn layers
    bn_params = []
    for layer in layers:
        if 'BatchNorm' in layer:
            print(layer)
            scale_factor = net.params[layer][2].data
            bn_params.append(net.params[layer][0].data / scale_factor)
            bn_params.append(net.params[layer][1].data / scale_factor)
    
    import numpy as np
    np.savez(caffe_model+'.npz', conv_params, bn_params)
