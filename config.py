class Config:
    seed = 116
    device = 'cuda'

    n_epoch = 3
    #batch_size = 64   ### 「CUDA out of memory. Tried to allocate…」となり
    batch_size = 48    ### batch_size を32に落として、その後48でもクリア！

    max_len = 22
    lr = 1e-3
    betas = (0.9, 0.98)

    vocab_size = 32000
    num_head = 8
    d_model = 768
    num_layer = 6
    d_ff = 2048
    drop_rate = 0.1
    max_grad_norm = 1.0

    smoothing = 0.1
    factor = 2
    warmup = 4000

    # FIXME: Change path of training data.
    data_dir = './data'
    train_data_path = f'{data_dir}/train_data.txt'
    #pickle_path = f'{data_dir}/train_data.pkl'
    pickle_path = f'{data_dir}/train_data_Xsmall.pkl'  ### ← これで、既存のTrainデータを利用
    fn = 'ckpt'

    load = False
    # FIXME: if you use original data, change flag of this
    use_pickle = True

    model_name = 'cl-tohoku/bert-base-japanese-whole-word-masking'
