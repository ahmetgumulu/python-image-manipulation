import cv2
img = cv2.imread("lenna.png")
print("resim boyutu :",img.shape)
cv2.imshow("orijinal resim",img)

imgResized = cv2.resize(img,(800,800))
print("yapılandırılmış boyut :",imgResized.shape)
cv2.imshow("yapılandırılmış resim",imgResized)

imgCropped = img[:200,:300]
cv2.imshow("lırpılmış resim",imgCropped)

if cv2.waitKey(0) & 0xFF == ord("q"): 
    cv2.destroyAllWindows()

