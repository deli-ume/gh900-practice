# gh900-practice

GH-900（GitHub Foundations）の練習用リポジトリです。
小さな電卓プログラムを題材に、Issue → PR → Actions → マージまでを一通り体験できます。

## 構成
```
.
├── src/calc.py                  # 電卓（わざとバグがあります）
├── tests/test_calc.py           # テスト（Actionsで自動実行されます）
├── .github/
│   ├── CODEOWNERS               # レビュアーを自動で指定する
│   ├── ISSUE_TEMPLATE/          # Issueテンプレート（フォーム形式・Markdown形式）
│   ├── pull_request_template.md # PRテンプレート
│   └── workflows/ci.yml         # GitHub Actions
├── .devcontainer/devcontainer.json  # Codespacesの設定
├── CONTRIBUTING.md / SECURITY.md / CODE_OF_CONDUCT.md / LICENSE
└── HANDS_ON.md                  # ハンズオン手順書 ← ここから始める
```

## Markdownの練習
- [x] リポジトリを作る
- [ ] HANDS_ON.md の演習1を終える

> 引用はこう表示されます

| 機能 | 試験の分野 |
|---|---|
| Issue / PR | 3. 共同作業 |
| Actions | 4. モダン開発 |
