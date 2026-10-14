# groktest — mini-AI v0.3 WebGPU デモ

ゼロから学習した超小型日本語チャットモデル（`mini-ai-v0.3-f16.gguf`）を、ブラウザ上で **WebGPU / WASM（wllama）** により動かすデモです。

## 含まれるもの

| ファイル | 説明 |
|---------|------|
| `index.html` | チャット UI（@wllama/wllama + WebGPU） |
| `mini-ai-v0.3-f16.gguf` | 学習済みモデル（約 2.2 MB, Llama アーキテクチャ, f16） |
| `serve.py` | COOP/COEP 付きローカルサーバ（マルチスレッド用） |

## すぐ試す

```bash
# このディレクトリで
python3 serve.py
# → http://127.0.0.1:8080/
```

1. 左ペインで `mini-ai-v0.3-f16.gguf` を選択 → **読み込む**
2. サンプル質問をクリック、または自由入力して送信

Chrome / Edge 推奨。WebGPU が使えると `n_gpu_layers` で GPU オフロードされます（使えない環境では自動的に WASM/CPU）。

## モデルについて

- **学習**: 合成日本語 Q&A のみ（外部コーパス・事前学習重みなし）
- **サイズ**: ~0.96M パラメータ / context 128 / 文字レベル tokenizer
- **得意**: あいさつ、首都、色、鳴き声、簡単な四則、オウム返し、「わからない」応答
- **プロンプト形式**:

```
質問：ねこの鳴き声は？
答え：
```

## GitHub Pages で公開する場合

Pages では任意ヘッダを付けにくいため、マルチスレッド（SharedArrayBuffer）が無効になることがあります。それでも **単一スレッド WASM** で動作します。GGUF はリポジトリに含めるか、Release アセットからダウンロードしてローカル選択してください。

## 技術

- [wllama](https://github.com/ngxson/wllama) v3（llama.cpp の WASM / WebGPU バインディング）
- ブラウザ完結（サーバへ質問は送りません）

## ライセンス

デモコードは自由に改変・再配布して構いません。モデルは実験用途向けです。
