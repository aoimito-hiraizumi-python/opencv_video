import cv2

# cap = cv2.VideoCapture("images/kuma.mp4")
cap = cv2.VideoCapture(0) # (0) にするとpcのカメラが起動する カメラ付の端末きならできる

# 保存するカメラの設定
fps = int(cap.get(cv2.CAP_PROP_FPS))                        # カメラのFPSを取得
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))                  # カメラの横幅を取得
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))                 # カメラの縦幅を取得
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')         # 動画保存時のfourcc設定（mp4用）
video = cv2.VideoWriter('video.mp4', fourcc, fps, (w, h))   # 動画の仕様（ファイル名、fourcc, FPS, サイズ）

while True:
    ret, frame = cap.read() # 読み込んだ最初の画像
    # print(ret, frame)
    if ret is False:
        break
    cv2.imshow("Image", frame) # 表示
    video.write(frame)
    # cv2.waitKey(1) # ()待って、表示
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
