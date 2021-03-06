#conding=utf-8

from munch import Munch

cfg = Munch()

# network
cfg.network = "resnet50"
cfg.pretrained = True

# datasets
cfg.dataset = "office31"
cfg.data_root = "/home/sunh/WorkSpace/MD-MMD/data/office31/"
cfg.src = ["amazon"]
cfg.tar = ["webcam"]
cfg.num_class = 31


# learning
cfg.learning_rate = 1e-4
cfg.new_layer_learning_rate = 1e-3
cfg.momentum = 0.9 # SGD momentum
#cfg.max_epoch = 500
cfg.max_iter = 1000

#loss
cfg.mmd_type = "mmd"
cfg.entropy_loss_weight = 1.0
cfg.MMD_loss_weight = 1.0


# dataloader
cfg.batch_size = 64
cfg.src_val_ratio = 0.8


