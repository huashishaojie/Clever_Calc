import tensorflow as tf
import numpy as np
from data.mydict import result

def recognize(imagelist):
    
    with tf.Graph().as_default():
        output_graph_def = tf.GraphDef()
    with open('frozen_model.pb', "rb") as f:
        output_graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(output_graph_def, name="")
    with tf.Session() as sess:
        output = sess.graph.get_tensor_by_name("out:0")
        input = sess.graph.get_tensor_by_name("x_input:0")
        for imgdict in imagelist:
            if(isinstance(imgdict, dict) and "image" in imgdict):
                image = imgdict["image"]
                if(isinstance(image, np.ndarray)):
                    img = np.reshape(image, [1, 32, 32, 1])
                    y = sess.run(output, feed_dict={input:img})
                    li = y.tolist()[0]
                    """n = []
                    for i in range(len(li)):
                        n.append({"key":i, "value":li[i]})
                    n.sort(key = lambda i:i["value"], reverse = True)
                    r = []
                    for i in n:
                        if(i["value"] > 0):
                            r.append(result[i["key"]])
                    """
                    ind = li.index(max(li))
                    imgdict["char"] = result[ind]["value"]
                    imgdict.pop("image")
        

    #print(imagelist)
    i = 0
    while(i < len(imagelist)):
        if(isinstance(imagelist[i], dict) and imagelist[i].get("index", False)):
            char = imagelist[i]["char"]
            if(char != "°"):
                imagelist[i]["char"] = '%s%s' % ("^(", char)
            i += 1
            while(i < len(imagelist) and isinstance(imagelist[i], dict) and imagelist[i].get("index", False)):
                i += 1
            char = imagelist[i-1]["char"]
            if(char != "°"):
                imagelist[i-1]["char"] = '%s%s' % (char, ")")
        i += 1
