# groktest — mini-AI v0.3（GitHub Pages）

ブラウザだけで動く WebGPU / WASM デモです。モデルは Hugging Face から読み込みます。

## デモ

**https://kubobeem.github.io/groktest/**

1. 「Hugging Face から読込」を押す  
2. チャットする

モデル: [kubobeem/testmodeler](https://huggingface.co/kubobeem/testmodeler)（`mini-ai-v0.3-f16.gguf`）

## Pages の有効化（初回のみ）

Repository → **Settings** → **Pages** → Source: **Deploy from a branch** → Branch: `main` / `/ (root)` → Save

## 技術

- [wllama](https://github.com/ngxson/wllama)（ブラウザ内推論）
- モデルは HF、UI は GitHub Pages のみ
