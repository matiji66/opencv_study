from pyimagesearch.searcher import Searcher
import numpy as np
import argparse
import pickle
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-d",'--dataset',required=True,
        help="Path to the directory that contains the image we just indexed")
ap.add_argument("-i",'--index',required=True,
        help="Path to where we stored our index")
args=vars(ap.parse_args())
index=pickle.loads(open(args["index"],'rb').read())

searcher=Searcher(index)

for (query, queryFeatures) in index.items():
    results=searcher.search(queryFeatures)
    path=args['dataset']+"/%s" % (query)
    queryImage=cv2.imread(path)
    cv2.imshow("Query",queryImage)
    print("query: %s" % (query))

    montageA=np.zeros((166*5,400,3),dtype='uint8')
    montageB=np.zeros((166*5,400,3),dtype='uint8')

    for j in range(0,10):
        (score, imagename)=results[j]
        path=args["dataset"]+"/%s" % (imagename)
        result=cv2.imread(path)
        print("\t%d. %s : %.3f" % (j+1, path,score))
        if j<5:
            montageA[j*166:(j+1)*166,:]=result
        else:
            montageB[(j-5)*166:(j-5+1)*166,:]=result
    cv2.imshow("Result 1-5",montageA)
    cv2.imshow("Result 6-10",montageB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
