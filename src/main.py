from pathlib import Path

import cv2


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_IMAGE = PROJECT_ROOT / "images" / "input" / "input.jpg"
OUTPUT_DIR = PROJECT_ROOT / "images" / "output"
OUTPUT_IMAGE = OUTPUT_DIR / "face_detection_result.jpg"


def detect_faces(image):
    """Detecta faces usando o classificador Haar Cascade do OpenCV."""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_detector = cv2.CascadeClassifier(cascade_path)

    if face_detector.empty():
        raise RuntimeError("nao foi possivel carregar o haar cascade do opencv")

    return face_detector.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40),
    )


def draw_faces(image, faces):
    """Desenha bounding boxes e labels simulados nas faces detectadas."""
    result = image.copy()

    for index, (x, y, width, height) in enumerate(faces, start=1):
        label = f"pessoa_{index}"

        cv2.rectangle(
            result,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            2,
        )

        label_y = max(y - 10, 20)
        cv2.putText(
            result,
            label,
            (x, label_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

    return result


def main():
    if not INPUT_IMAGE.exists():
        print(f"imagem nao encontrada: {INPUT_IMAGE}")
        print("adicione uma imagem em images/input/input.jpg e execute novamente")
        return

    image = cv2.imread(str(INPUT_IMAGE))

    if image is None:
        print(f"nao foi possivel carregar a imagem: {INPUT_IMAGE}")
        return

    faces = detect_faces(image)
    result = draw_faces(image, faces)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(OUTPUT_IMAGE), result)

    print(f"faces detectadas: {len(faces)}")
    print(f"resultado salvo em: {OUTPUT_IMAGE}")


if __name__ == "__main__":
    main()
