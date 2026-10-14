# groktest — mini-AI v0.3 WebGPU デモ

ゼロから学習した超小型日本語チャットを、ブラウザ上で **WebGPU / WASM（wllama）** で動かすデモです。

## モデル（Hugging Face）

- **https://huggingface.co/kubobeem/testmodeler**
- ファイル: `mini-ai-v0.3-f16.gguf`（約 2.2 MB）

デモ画面の **「Hugging Face から読込」** でそのまま使えます。

## すぐ試す

```bash
git clone https://github.com/kubobeem/groktest.git
cd groktest
python3 serve.py
# → http://127.0.0.1:8080/
```

1. 「Hugging Face から読込」をクリック
2. サンプル質問 or 自由入力

Chrome / Edge 推奨。

## 技術

- [wllama](https://github.com/ngxson/wllama) v3
- モデル本体は HF、UI はこのリポジトリ
