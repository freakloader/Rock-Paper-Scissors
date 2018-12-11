import numpy as np
from keras.models import load_model
from ImgPrepro import Valid,Train,Test
import matplotlib.pyplot as plt
from keras.preprocessing import image
import pandas as pd

model=load_model('ModelA.h5')#EModel20epoch,6convu6464finalconvu1024denseneurons,2310imgsrmspropsparselowdataugrescaleintrain.h5')


#train=Train()
#test=Test()
#print(Train.class_indices)
#fruit_indices=Train.class_indices


#test_image=image.load_img('Operation3/Good/live.jpg',target_size=(150,150),color_mode='grayscale')
#print(type(test_image))
#test_image=test_image.astype('float32')
#test_image=test_image/255
#print(test_image.shape)
##plt.imshow(test_image)
##plt.show()

def Prediction(playerimg):
    pred_image=image.load_img(playerimg,target_size=(150,150),color_mode='grayscale')
    plt.imshow(pred_image)
    plt.show()

    pred_image = image.img_to_array(pred_image)
    #print(pred_image.shape)
    pred_image = np.expand_dims(pred_image, axis=0)
    #print(test_image.shape)

    result = model.predict(pred_image)
    prediction=None
    if result[0][0] == 1:
        prediction = "Paper"
        return prediction
    elif result[0][1] == 1:
        prediction = "Scissors"
        return prediction
    elif result[0][2] == 1:
        prediction = "Stone"
        return prediction




##test_image=image.img_to_array(test_image)
##print(test_image.shape)
##test_image=np.expand_dims(test_image,axis =0)
##print(test_image.shape)
#test_image=np.expand_dims(test_image,axis =-1)
#print(test_image.shape)

#test_image=np.expand_dims(test_image,axis=0)

##result=model.predict(test_image)
##print(result)
#pred=model.predict_generator(test_image,verbose=1)
#predicted_indices=np.argmax(pred,axis=1)
#print(predicted_indices)

##model.summary()

##if result[0][0]==1:
##    prediction="Paper"
##elif result[0][1] == 1:
##    prediction = "Scissors"
##elif result[0][2]==1:
##    prediction="Stone"

##print(prediction)


'''
if result[0][0]>result[0][1] and result[0][0]>result[0][1]:
    prediction="Paper"
elif result[0][0]<result[0][1] and result[0][2]<result[0][1]:
    prediction="Scissors"
elif result[0][0]<result[0][2] and result[0][2]>result[0][1]:
    prediction="Stone"
'''


##valid=Valid()
##acc=model.evaluate_generator(generator=valid,pickle_safe=False)
##print("Accuracy:",acc)

#print(type(acc))

'''
train=Train()
test=Valid()

pred=model.predict_generator(test,verbose=1)
predicted_indices=np.argmax(pred,axis=1)
print(predicted_indices)

#predicted_class_indice=dict({0:'Paper' ,1:'Scissors',2:'Stone'})
labels=train.class_indices
#print(train.class_indices)
#print(labels)
labels=dict((v,k) for k,v in labels.items())
#print(labels)

predictions=[labels[k] for k in predicted_indices]
#print(predictions)
filenames=test.filenames
result=pd.DataFrame({"Filename":filenames,"Predictions":predictions})
result.to_csv("RESULT5thModel.csv",index=True)

'''







