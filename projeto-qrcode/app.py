import cv2
import threading
from flask import Flask, jsonify, render_template

app = Flask(__name__)

ultimo_qr = {"data": None}
lock = threading.Lock()

url = "http://172.20.32.35:8080/video"  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/qr", methods=["GET"])
def get_qr():
    with lock:
        return jsonify({"qr": ultimo_qr["data"]})

def camera_loop():
    cap = cv2.VideoCapture(url)
    detector = cv2.QRCodeDetector()

    if not cap.isOpened():
        print("Erro ao abrir a câmera")
        return

    print("Scanner iniciado.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Erro ao capturar frame")
            break

        data, bbox, _ = detector.detectAndDecode(frame)

        if bbox is not None:
            pontos = bbox[0].astype(int)
            n = len(pontos)
            for i in range(n):
                pt1 = tuple(pontos[i])
                pt2 = tuple(pontos[(i + 1) % n])
                cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

            if data:
                with lock:
                    ultimo_qr["data"] = data
                x, y = pontos[0]
                cv2.putText(frame, data, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                print("QR Code detectado:", data)

        cv2.imshow("Scanner QR - Raspberry", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    t = threading.Thread(target=camera_loop, daemon=True)
    t.start()

    app.run(host="0.0.0.0", port=5000)
