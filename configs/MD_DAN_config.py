#conding=utf-8

from munch import Munch

cfg = Munch()

# network
cfg.network = "resnet50"
cfg.pretrained = True
cfg.latent_domain_num = 3

# datasets
cfg.dataset = "office31"
cfg.data_root = "/home/sunh/WorkSpace/MD-MMD/data/" + cfg.dataset + "/"
cfg.src = ["sketch", "art_painting", "cartoon"]
cfg.tar = ["photo"]
cfg.num_class = 31


# learning
cfg.learning_rate = 1e-4
cfg.new_layer_learning_rate = 1e-3
cfg.momentum = 0.9 # SGD momentum
cfg.max_iter = 500

#loss
cfg.mmd_type = "mmd"
cfg.entropy_loss_weight = 1.0
cfg.inter_MMD_loss_weight = 2.0
cfg.cluster_loss_weight = 0.01
cfg.aux_entropy_loss_weight = 0.1
cfg.loss_factor_decay = 0


# dataloader
cfg.batch_size = 128
cfg.src_val_ratio = 0.8


