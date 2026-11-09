# Machine Learning

F.CSM308 — Машин сургалтын лаборатори, бие даалт, туршилтууд.

Local кодоо Mac дээр засаж, GitHub-д хадгална. GPU шаардлагатай сургалтыг Colab дээр ажиллуулна.

## Notebook-ууд

| Лаб | Агуулга | Runtime | Хугацаа | Colab |
|---|---|---|---|---|
| **Lab 1** | Орчны шалгалт (Apple Silicon / MPS) | — | — | — |
| **Lab 2** | Perceptron, average perceptron, Pegasos | CPU | ~1 мин | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/Lab2/CS308_lab2_B231910012.ipynb) |
| **Lab 3** | Hinge loss, logistic regression, gradient descent | CPU | ~2 мин | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/Lab3/CS308_lab3_B231910012.ipynb) |
| **Lab 2–3** | Илгээсэн нэгтгэсэн хувилбар | CPU | ~2 мин | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/Ilgeeh_lab23/CS308_lab23_B231910012.ipynb) |
| **Lab 4** | SVM: max-margin, OvR, deskew + Virtual SV → **99.29%** | CPU | ~35 мин | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/Lab4/svm_lab4_2324.ipynb) |
| **Lab 5–6** | Мэдрэлийн сүлжээ эхнээс: NumPy → CuPy → PyTorch → **0.98** | **T4 GPU** | ~5 мин | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/Lab5-6/CS308_lab5_6_B231910012.ipynb) |
| **Lab 6–7** | Hyperparameter tuning, 6-fold CV, ROC/AUC, confusion matrix | **T4 GPU** | ~20 мин | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/Lab6-7/CS308_lab6_7_B231910012.ipynb) |
| **Lab 8** | Ensemble: stacking, out-of-fold, bagging / boosting | CPU | ~1 мин | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/Lab8/CS308_lab8_B231910012.ipynb) |
| **Lab 9–10** | Knowledge distillation + **FitNets** (завсрын давхарга) | **T4 GPU** | ~25 мин | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/Lab9-10/CS308_lab9_10_B231910012.ipynb) |
| **Lab 10** | Transformers: монгол мэдээ ангилал (Eduge, BERT) | **T4 GPU** | ~15 мин | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrbuus/Machine-Learning/blob/main/Lab/Lab10/CS308_lab10_B231910012.ipynb) |

> **GPU сонгох:** Colab-д notebook нээгээд `Runtime` → `Change runtime type` → **T4 GPU**.
> Lab 4 ба Lab 8-ийн sklearn нь зөвхөн CPU дээр ажилладаг тул GPU сонгох нь тэднийг хурдасгахгүй.

### Нэмэлт тайлбар

| Файл | Агуулга |
|---|---|
| [CS308_tailbar.html](CS308_tailbar.html) | Лаб 1–4 — функц функцээр, үндэслэлтэй |
| [CS308_lab5_10_tailbar.html](CS308_lab5_10_tailbar.html) | **Лаб 5–10** — функц функцээр, «яагаад» товчтой, графикийн хэлбэрийн тайлбартай |
| [CS308_lecture5_tailbar.html](CS308_lecture5_tailbar.html) | Лекц 5 — мэдрэлийн сүлжээ, backpropagation |
| [Lecture/Lecture5_Neural_Networks_daalgavar.tex](Lecture/Lecture5_Neural_Networks_daalgavar.tex) | Лекц 5-ийн бодлогууд LaTeX дээр |

> HTML файлуудыг GitHub дээр шууд үзэх боломжгүй (код харагдана).
> Татаж аваад браузераар нээнэ, эсвэл [htmlpreview](https://htmlpreview.github.io/) ашиглана.

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

## Урт сургалтын явцыг хадгалах, үргэлжлүүлэх

Их хэмжээний өгөгдөл эсвэл удаан ажиллах загварыг сургахдаа Colab-ийн ашиглалтын хязгаар, runtime тасрах боломжийг тооцож, сургалтын коддоо **checkpoint тогтмол хадгалах болон түүнээс үргэлжлүүлэх** ажиллагааг оруулна. Ингэснээр сургалт тасарсан үед эхнээс нь дахин сургахгүй, хамгийн сүүлд амжилттай хадгалсан төлөвөөс үргэлжлүүлнэ.

Хадгалах давтамжийг сургалтын хурд болон алдаж болох ажлын хэмжээнд тохируулна. Жишээлбэл, богино epoch-той сургалтад **10 epoch тутам**, харин нэг epoch удаан үргэлжилдэг бол тодорхой тооны batch/step тутам эсвэл **10–15 минут тутам** хадгалж болно. Эдгээр нь жишээ давтамж бөгөөд Colab-ийн тогтсон лимит биш. Runtime тасрахаас өмнө заавал анхааруулна гэж найдалгүй, хадгалалтыг сургалтын явцад автоматаар хийнэ.

- Checkpoint-д загварын жин, optimizer-ийн төлөв, дууссан epoch/step, сургалтын тохиргоо болон үнэлгээний үзүүлэлтүүдийг хадгална. Scheduler, mixed precision эсвэл санамсаргүй түүвэрлэлт ашигласан бол үргэлжлүүлэхэд шаардлагатай тэдгээрийн төлөвийг мөн хадгална.
- **Сүүлийн checkpoint**-ийг сургалтаа үргэлжлүүлэхэд, **validation дээр хамгийн сайн checkpoint**-ийг эцсийн загвараа сонгоход тусад нь ашиглана.
- Checkpoint болон loss/accuracy-ийн түүхийг Google Drive зэрэг runtime-аас тусдаа, тогтвортой хадгалалтад бичнэ. Зөвхөн `/content` дотор хадгалах эсвэл notebook-оо GitHub-д хадгалах нь загварын төлөвийг хамгаалахгүй.
- Урт сургалт эхлүүлэхээс өмнө богино туршилтаар checkpoint хадгалах → ачаалах → үргэлжлүүлэх ажиллагааг шалгана. Шинэ checkpoint бүрэн бичигдтэл өмнөх амжилттай файлыг үлдээнэ.

Энэ ажиллагаа нь сургалтын явц дундаас үргэлжлүүлэхийг дэмждэг алгоритмд хамаарна. `sklearn.svm.SVC` болон `LinearSVC`-ийн `fit()` нь дундаас нь checkpoint-оор үргэлжлүүлэх боломжгүй тул тухайн алгоритмын дэмжлэгийг эхлээд шалгана.

## Өгөгдөл, үр дүн

- Жижиг өгөгдөл, код, тайлан: GitHub.
- Том dataset, checkpoint: Google Drive эсвэл local; repo-д оруулахгүй.
- Colab runtime-ийн файлууд түр зуурынх. Чухал checkpoint-оо Drive-д хадгална.
- Сурах бичиг, багшийн PDF, ZIP архивууд local дээр үлдэнэ.

## Холбоос

- [Colab + GitHub](https://github.com/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb)
- [Colab FAQ](https://research.google.com/colaboratory/faq.html)
