import argparse
import os
import sys
import cv2
from ultralytics import YOLO
from datetime import datetime

MODEL_PATH = "model.pt"
OUTPUT_DIR = "outputs"


def main():
    parser = argparse.ArgumentParser(
        description="Dockerized Inference Pipeline for a Custom Fine-Tuned YOLO Mask Detection Model by Emre Uçar"
    )
    parser.add_argument("--input", required=True, help="Input image path")
    parser.add_argument(
        "--output",
        default=None,
        help="Only the output file name (example: output.jpg). Folder cannot be specified."
    )
    args = parser.parse_args()

    if not os.path.exists(MODEL_PATH):
        print(f"Model not found: {MODEL_PATH}", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(args.input):
        print(f"Input not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if args.output:
        if "/" in args.output or "\\" in args.output:
            print("You can only specify a file name. You cannot specify a folder.", file=sys.stderr)
            sys.exit(1)

        output_filename = args.output
    else:
        base_name = os.path.splitext(os.path.basename(args.input))[0]
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = f"{base_name}_{timestamp}.jpg"

    output_path = os.path.join(OUTPUT_DIR, output_filename)

    model = YOLO(MODEL_PATH)

    img = cv2.imread(args.input)
    if img is None:
        print("The image could not be read.", file=sys.stderr)
        sys.exit(1)

    results = model(img, verbose=False)

    annotated = results[0].plot()

    success = cv2.imwrite(output_path, annotated)
    if not success:
        print("The output file could not be written.", file=sys.stderr)
        sys.exit(1)

    print(f"Inference completed. File Path: {output_path}")


if __name__ == "__main__":
    main()