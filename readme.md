ENGLISH – US

YOLO Face Mask Detection – Dockerized CLI Tool (CUDA)

Dockerized inference tool for a custom fine-tuned YOLO mask detection model.

Pull image:
docker pull mremre06/yolo-facemask-detection-cuda:1.0.0

Prepare folders:
mkdir inputs outputs

Run:
docker run --rm -v "$(pwd)/inputs:/app/inputs" -v "$(pwd)/outputs:/app/outputs" mremre06/yolo-facemask-detection-cuda:1.0.0 --input /app/inputs/input.jpg

Output is saved inside the outputs folder.

CLI:
--input (required)
--output (optional, filename only)

UI Version => https://github.com/EMRUCR/Mask_Detection_with_UI
Docker Link => https://hub.docker.com/r/mremre06/yolo-facemask-detection-cuda

###################################

TURKISH – TR

YOLO Yüz Maskesi Tespiti – Dockerize Edilmiş CLI Aracı (CUDA)

Özel fine-tune edilmiş YOLO maske tespit modeli için Dockerize edilmiş inference aracıdır.

Image indirme:
docker pull mremre06/yolo-facemask-detection-cuda:1.0.0

Klasörleri hazırlama:
mkdir inputs outputs

Çalıştırma:
docker run --rm -v "$(pwd)/inputs:/app/inputs" -v "$(pwd)/outputs:/app/outputs" mremre06/yolo-facemask-detection-cuda:1.0.0 --input /app/inputs/input.jpg

Çıktı outputs klasörüne kaydedilir.

CLI:
--input (zorunlu)
--output (isteğe bağlı, sadece dosya adı)

UI Versiyonu => https://github.com/EMRUCR/Mask_Detection_with_UI
Docker Linki => https://hub.docker.com/r/mremre06/yolo-facemask-detection-cuda

