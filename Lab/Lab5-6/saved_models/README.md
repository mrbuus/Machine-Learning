# Lab 5-6: хадгалсан загварууд

`lab5_6_best_models.pt` - Colab (T4) дээрх гүйлтийн дараа хадгалсан 3 загвар:

| Түлхүүр | Параметр | Тестийн нарийвчлал | Сувгууд |
|---|---|---|---|
| `tiny_cnn_8450` | 8 450 | 0.9960 | [8, 16, 16, 16, 16] |
| `pruned_section7` | 4 828 | 0.9942 | [6, 12, 12, 12, 12] |
| `pruned_l1_section8` | 3 395 | 0.9926 | [5, 10, 10, 10, 10] |

Ачаалах (notebook-ийн `SlimCNN` класс хэрэгтэй):

```python
d = torch.load("saved_models/lab5_6_best_models.pt", weights_only=True)
m = SlimCNN(d["tiny_cnn_8450"]["widths"])
m.load_state_dict(d["tiny_cnn_8450"]["state_dict"])
m.eval()
```

9-р хэсгийн 3 seed-ийн загварууд (жишээ нь L1 + WD, 3 395 параметр, 0.9931 ± 0.0005) санах ойд хадгалагдаагүй тул
энд ороогүй.
