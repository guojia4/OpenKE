import config
import models
import numpy as np
import json
import os
os.environ['CUDA_VISIBLE_DEVICES']='6'
#(1) Set import files and OpenKE will automatically load models via torch.load().
con = config.Config()
con.set_in_path("./benchmarks/FB15K/")
#con.set_test_link_prediction(True)
#con.set_test_triple_classification(True)
con.set_work_threads(4)
con.set_dimension(100)
con.set_import_files("./res/transe.pt")
con.init()
con.set_model(models.TransE)
con.show_link_prediction(8,4)
con.show_triple_classification(8,9,4)
'''
#(2) Read model parameters from json files and manually load parameters. 
con = config.Config()
con.set_in_path("./benchmarks/FB15K/")
con.set_test_link_prediction(True)
con.set_test_triple_classification(True)
con.set_work_threads(4)
con.set_dimension(100)
con.init()
con.set_model(models.TransE)
f = open("./res/embedding.vec.json", "r")
content = json.loads(f.read())
f.close()
con.set_parameters(content)
con.test()
#(3) Manually load models via torch.load()
con = config.Config()
con.set_in_path("./benchmarks/FB15K/")
con.set_test_link_prediction(True)
con.set_test_triple_classification(True)
con.set_work_threads(4)
con.set_dimension(100)
con.init()
con.set_model(models.TransE)
con.import_variables("./res/transe.pt")
con.test()
'''
