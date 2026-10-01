"""
F.CS308 Машин сургалт - Лаборатори №1
Орчин бэлтгэсний дараа шаардлагатай сангууд бүрэн суусан эсэхийг шалгах скрипт.

Ажиллуулах:  python3 check_env.py
"""

import platform
import sys
from importlib import import_module

# Лабораторийн удирдамжид заасан сангууд
REQUIRED = [
    ("numpy", "numpy"),
    ("pandas", "pandas"),
    ("matplotlib", "matplotlib"),
    ("scipy", "scipy"),
    ("sklearn", "scikit-learn"),
    ("cv2", "opencv-python"),
    ("torch", "torch"),
    ("torchvision", "torchvision"),
]


def version_of(module):
    """Сан бүр __version__-ээ өөр нэрээр хадгалдаг тул хамгаалалттай уншина."""
    return getattr(module, "__version__", "тодорхойгүй")


def main():
    print("=" * 58)
    print("СИСТЕМИЙН МЭДЭЭЛЭЛ")
    print("=" * 58)
    print(f"Үйлдлийн систем : {platform.system()} {platform.release()}")
    print(f"Архитектур      : {platform.machine()}")
    print(f"Python          : {sys.version.split()[0]}")
    print(f"Python зам      : {sys.executable}")

    print()
    print("=" * 58)
    print("САНГУУДЫН ШАЛГАЛТ")
    print("=" * 58)

    missing = []
    for import_name, pip_name in REQUIRED:
        try:
            mod = import_module(import_name)
        except ImportError:
            print(f"[ДУТУУ] {pip_name:<16} -> pip3 install {pip_name}")
            missing.append(pip_name)
        else:
            print(f"[ OK  ] {pip_name:<16} {version_of(mod)}")

    # PyTorch суусан бол GPU (CUDA/MPS) боломжтой эсэхийг нэмж шалгана
    try:
        import torch
    except ImportError:
        pass
    else:
        print()
        print("-" * 58)
        print("Хурдасгуур төхөөрөмж")
        print("-" * 58)
        print(f"CUDA боломжтой эсэх : {torch.cuda.is_available()}")
        # Apple Silicon дээр CUDA биш MPS ажилладаг
        mps = getattr(torch.backends, "mps", None)
        print(f"MPS боломжтой эсэх  : {bool(mps and mps.is_available())}")

    print()
    if missing:
        print(f"ДҮГНЭЛТ: {len(missing)} сан дутуу байна -> {', '.join(missing)}")
        return 1

    print("ДҮГНЭЛТ: Шаардлагатай бүх сан амжилттай суусан. Лаб 2-т бэлэн.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
