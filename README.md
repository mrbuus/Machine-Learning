# Machine Learning

F.CSM308 — Машин сургалтын лаборатори, бие даалт, туршилтууд.

Local кодоо Mac дээр засаж, GitHub-д хадгална. GPU шаардлагатай сургалтыг Colab дээр ажиллуулна.

## Notebook-ууд

| Notebook | Colab |
|---|---|
| [Lab/CS308_lab_23_udirdamj.ipynb](Lab/CS308_lab_23_udirdamj.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/CS308_lab_23_udirdamj.ipynb) |
| [Lab/Ilgeeh_lab23/CS308_lab23_B231910012.ipynb](Lab/Ilgeeh_lab23/CS308_lab23_B231910012.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/Ilgeeh_lab23/CS308_lab23_B231910012.ipynb) |
| [Lab/Lab2/CS308_lab2_B231910012.ipynb](Lab/Lab2/CS308_lab2_B231910012.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/Lab2/CS308_lab2_B231910012.ipynb) |
| [Lab/Lab3/CS308_lab3_B231910012.ipynb](Lab/Lab3/CS308_lab3_B231910012.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/Lab3/CS308_lab3_B231910012.ipynb) |
| [svm_lab4_2324.ipynb](svm_lab4_2324.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/svm_lab4_2324.ipynb) |

## Өдөр тутмын ажил

1. Mac дээр ажил эхлэхдээ GitHub Desktop → Fetch origin → Pull origin.
2. VS Code/Jupyter дээр кодоо засаж, жижиг өгөгдлөөр шалгана.
3. GitHub Desktop дээр өөрчлөлтөө шалгаж, тайлбартай Commit → Push origin.
4. Дээрх Open in Colab товчоор notebook нээнэ. GPU хэрэгтэй бол Runtime → Change runtime type → GPU.
5. Colab дээр код/үр дүн өөрчилсөн бол File → Save a copy to GitHub. Ижил branch, notebook-ийн замыг сонгоно.
6. Mac дээр үргэлжлүүлэхээс өмнө дахин Pull хийнэ. Нэг notebook-ийг хоёр газар зэрэг өөрчлөхөөс зайлсхий.

Colab-аас GitHub-д автоматаар синк хийхгүй. Зөвхөн ажиллуулсан бол хадгалах шаардлагагүй; хадгалах код/үр дүн байгаа үед GitHub руу хадгална.

### Терминалын богино командууд

```bash
make status
make pull
make save MSG="Implement multiclass SVM"
make push
make check
```

`make save` нь ignore-д ороогүй бүх өөрчлөлтийг commit хийнэ. Эхлээд `make status` болон өөрчлөлтөө шалгана. `make pull` нь merge шаардлагатай бол зогсоно.

## Mac орчин

Одоо байгаа Anaconda kernel: `/opt/anaconda3/bin/python`.
Шинэ тусдаа орчин хэрэгтэй бол:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

`requirements.txt` нь шаардлагатай сангуудын жагсаалт; бүх платформд яг ижил хувилбар тогтоосон lock файл биш.

## Colab дээр нэмэлт файлууд хэрэгтэй үед

Notebook-ийг GitHub-аас нээхэд repo-ийн бусад файлууд автоматаар татагдахгүй. `Data/toy_data.tsv` зэрэг файл хэрэгтэй бол эхэнд нь:

```python
from pathlib import Path
import subprocess

repo = Path("/content/Machine-Learning")
if not repo.exists():
    subprocess.run(["git", "clone", "https://github.com/mrbuus/Machine-Learning.git", str(repo)], check=True)
%cd /content/Machine-Learning
```

Энэ clone нь GitHub-д байгаа кодыг татна; Colab editor дахь хадгалаагүй өөрчлөлтийг оруулахгүй. Дахин нээсэн runtime-д clone хуучирсан бол ажлаа хадгалаад шинэ runtime эхлүүлнэ.

## PyTorch төхөөрөмж

```python
import torch
device = torch.device("cuda" if torch.cuda.is_available() else
                      "mps" if torch.backends.mps.is_available() else "cpu")
model = model.to(device)
# Сургалтын batch бүрийг мөн .to(device) хийнэ.
```

sklearn-ийн энгийн SVM нь CPU ашиглана. GPU runtime сонгох нь sklearn кодыг автоматаар CUDA болгохгүй.

## Өгөгдөл, үр дүн

- Жижиг өгөгдөл, код, тайлан: GitHub.
- Том dataset, checkpoint: Google Drive эсвэл local; repo-д оруулахгүй.
- Colab runtime-ийн файлууд түр зуурынх. Чухал checkpoint-оо Drive-д хадгална.
- Сурах бичиг, багшийн PDF, ZIP архивууд local дээр үлдэнэ.

## Холбоос

- [Colab + GitHub](https://github.com/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb)
- [Colab FAQ](https://research.google.com/colaboratory/faq.html)
