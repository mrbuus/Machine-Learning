---
name: shorten-notebook
description: Shorten a course lab or exam notebook in this repo so it only answers what the assignment asks, keeps one correctness check, runs cleanly on the local .venv, and leaves the commit to the user. Use when asked to shorten, trim, simplify or "make smaller" a Lab, midterm or Bie daalt notebook.
argument-hint: <notebook path> [assignment text]
---

# Shorten a notebook

Target: $ARGUMENTS

If no assignment text was given and the notebook does not contain it, ask for it before doing anything.
Work on one notebook at a time.

## Goal

Turn the notebook into small, readable code that answers exactly what the assignment asks.
It must still run without errors and produce correct results.

## 1. Read and plan first. Do not edit yet.

- Split the assignment text into its individual requirements
  (for example "write forward and backward functions", "print the test results").
- Go through the notebook cell by cell and mark which requirement each cell serves and which cells can go.
- Show this plan to the user and wait for an OK before touching the file.

## 2. Shortening rules

- Keep only the code that answers the assignment: loading the data, the core function or model,
  training, and the results the assignment asks to print or show.
- Remove extra experiments, comparisons, plots and explanations that the assignment did not ask for.
- Remove all markdown cells. If the assignment asks for a written answer or conclusion,
  keep it as one short markdown cell of 2-3 sentences.
- Keep the teacher's scaffolding as it is: function names, signatures, classes and the cells that
  the assignment asks to fill in. Do not rename or delete them.
- Keep functions small and plain. Do not introduce classes unless the teacher's scaffold uses them.
  No docstrings.
- Comments are few and short, in Mongolian written with Latin letters, in plain words. For example:

  ```python
  # test deer shalgah
  # age-iin hooson utgiig median-aar nuhuj baigaad scale hiihed
  ```

- Print only the key results (accuracy, loss, shapes).
- Keep exactly one check that proves the code is correct: a hand-computed example,
  a numerical gradient check, or the test-set metric. Do not add more.
- Do not change hyperparameters, the train/test split, seeds or anything else that changes the results.
  If a change is unavoidable, say why.

## 3. Run and verify

- Save a backup copy of the notebook in the scratchpad before editing.
- Execute the notebook with the repo's `.venv` (it lives in the main checkout, also when you work in a worktree):

  ```bash
  ROOT="$(dirname "$(git rev-parse --path-format=absolute --git-common-dir)")"
  "$ROOT/.venv/bin/jupyter" nbconvert --to notebook --execute --inplace \
    --ExecutePreprocessor.kernel_name=ml-venv <notebook>
  ```

  If the `ml-venv` kernel is missing, register it with
  `"$ROOT/.venv/bin/python" -m ipykernel install --user --name ml-venv --display-name "Machine Learning (.venv)"`.
- If training would take more than about 15 minutes on the Mac, ask first: it may belong on a Colab T4 instead.
- Check that every cell ran, there are zero errors and the numbers make sense.
  Strip download progress bars (stderr stream output) from the saved notebook.
  Make sure the Cyrillic text is intact.

## 4. Git and the user's own edits

- Run `git status` before writing a file. If the user has modified it by hand (status `M`),
  do not overwrite it. Ask first.
- Do not commit or push. The user reviews, edits and commits.
- If the user does ask you to commit, never add `Co-Authored-By` or any other Claude attribution.
- If a result changes, list the files that quote the old number (`README.md`, `*_tailbar.html`)
  and do not edit them without asking.

## 5. Report

When done, report briefly:

- cells and lines: before → after
- what was removed and why
- key results: old → new
- what the user should check
