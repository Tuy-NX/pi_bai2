import cv2
import qrcode
import csv
import RPi.GPIO as GPIO
import time

print("Nhập lựa chọn:\n 1: Tạo QR-Code. \n 2: Quét QR-Code bằng ảnh. \n 3: Quét QR-Code bằng camera.\n 4: Thoát.")
TT = input()
while(1):
    if TT == '1':
        print("Tạo QR Code.")
        print("Nhập data QR-Code.")
        data=input()
        print("Nhập tên QR-Code.")
        name=input()+'.png'
        img = qrcode.make(data)
        img.save(name)
        print("Tạo QR-Code thành công. ")
        print("Nhập lựa chọn:\n 1: Tạo QR-Code. \n 2: Quét QR-Code bằng ảnh. \n 3: Quét QR-Code bằng camera.\n 4: Thoát.")
        TT = input()

    if TT=='2':
        name=input()+'.png'
        img = cv2.imread(name)
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(img)
        if bbox is not None:
            print(f"QRCode data: {data}")
            n_lines = len(bbox)
            for i in range(n_lines):
                point1 = tuple(bbox[i][0])
                point2 = tuple(bbox[(i+1) % n_lines][0])

        cv2.imshow("QR_Code", img)
        while(1):
            if cv2.waitKey(0) == ord("q"):
                break
        cv2.destroyAllWindows()       
        print("Nhập lựa chọn:\n 1: Tạo QR-Code. \n 2: Quét QR-Code bằng ảnh. \n 3: Quét QR-Code bằng camera. \n 4: Thoát.")
        TT = input()

    if TT=='3':    
            GPIO.setup(17, GPIO.OUT) #đèn đỏ
            GPIO.setup(18, GPIO.OUT) #đèn xanh
            GPIO.setup(19, GPIO.OUT)  #còi           
            # set up camera object
            cap = cv2.VideoCapture(0)
            # QR code detection object
            detector = cv2.QRCodeDetector()
            
            print("Scan QR code using Raspberry Pi Camera")
            print("------------------------------")
            
            while True: #có qr
                # get the image
                _, img = cap.read()
                # get bounding box coords and data
                data, bbox, _ = detector.detectAndDecode(img) 
                if bbox is not None:
                        GPIO.output(18, 1) #có qr thì bật đèn xanh
                        GPIO.output(17, 0) #có qr thì tắt đèn đỏ
                        bb_pts = bbox.astype(int).reshape(-1, 2)
                        num_bb_pts = len(bb_pts)
                        for i in range(num_bb_pts):
                            cv2.line(img,
                                tuple(bb_pts[i]),
                                tuple(bb_pts[(i+1) % num_bb_pts]),
                                color=(255, 0, 255), thickness=2)
                            cv2.putText(img, data,
                                (bb_pts[0][0], bb_pts[0][1] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 255, 0), 2)
                else: #khong có qr
                    GPIO.output(18, 0) #có qr thì tắt đèn xanh
                    GPIO.output(17, 1) #có qr thì bật đèn đỏ

                if data: #so sánh database
                        print("data found: ", data)    
                        data = data.split(",")
                        print("ID: " + data[0])
                        print("NAME: " + data[1])
                        print("CLASS: " + data[2])
                        print()
                        #if the same QR code is detected, do not save the data  
                        userScanned = False
                        with open('Database.csv') as csvfile:
                            reader = csv.DictReader(csvfile)
                            for row in reader:
                                if row['ID'] == data[0]:
                                    userScanned = True
                        #write data to file Database.csv        
                        if userScanned == False:
                            with open('Database.csv', 'a') as csvfile:
                                fieldNames = ['ID', 'NAME', 'CLASS']
                                writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
                                writer.writerow({'ID': data[0], 'NAME': data[1], 'CLASS': data[2]})
                                GPIO.output(19, 1) #data chưa có trong database thì bật còi và kêu 2s
                                sleep(2)
                                GPIO.output(19, 0) #tắt còi
                # display the image preview            
                cv2.imshow("code detector", img)
                if cv2.waitKey(1) == ord("q"):
                    break
            # free camera object and exit
            cap.release()
            cv2.destroyAllWindows()

            print("Nhập lựa chọn:\n 1: Tạo QR-Code. \n 2: Quét QR-Code bằng ảnh. \n 3: Quét QR-Code bằng camera. \n 4: Thoát.")
            TT = input()

    if TT=='4':
        break
    else:
        print("Nhập lựa chọn:\n 1: Tạo QR-Code. \n 2: Quét QR-Code bằng ảnh. \n 3: Quét QR-Code bằng camera.\n 4: Thoát.")
        TT = input()


