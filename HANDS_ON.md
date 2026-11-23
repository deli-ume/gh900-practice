# ハンズオン手順書（全体で約90分）

各演習の【暗記】は、暗記シートで覚えた項目との対応です。
**リポジトリはPublicで作ってください**（PublicならActions・Pages・Wikiを無料で使えます。中身は練習用のコードだけです）。

---

## 演習0：リポジトリを作る（10分）
1. GitHubで新しいリポジトリ `gh900-practice` を作る（Public、READMEなし）
2. ZIPを解凍したフォルダで次を実行する
   ```bash
   git init
   git add .
   git commit -m "first commit"
   git branch -M main
   git remote add origin https://github.com/<ユーザー名>/gh900-practice.git
   git push -u origin main
   ```
3. `.github/CODEOWNERS` の `YOUR_USERNAME` を自分のユーザー名に書き換える（Web画面の鉛筆アイコンから編集してよい）

**確認すること**
- トップにREADMEが表示され、右側に「MIT license」と出る
- Markdownのチェックボックス・表・引用の見た目
- 【暗記】README / LICENSE / CODEOWNERS の役割

---

## 演習1：Issueを作る（10分）
1. **Issues → New issue** を開くと、テンプレートが2種類並ぶ
2. 「バグ報告」（フォーム形式）を選び、`subtract(10, 3) が 13 を返す` と入力する
3. 右側で設定する
   - **Assignees**：自分
   - **Labels**：`bug` が自動で付いているのを確認する
   - **Milestone**：「v1.0」を新しく作って設定する（Issues → Milestones）
4. 番号（#1）をメモしておく

**確認すること**
- 【暗記】YAMLのテンプレート＝Issueフォーム、Markdownのテンプレート＝通常のテンプレート
- 【暗記】Label / Milestone / Assignees
- 検索欄で `is:open label:bug assignee:@me` と入力して絞り込んでみる

---

## 演習2：github.devで直してPRを作る（15分）
1. リポジトリのトップで **`.`（ピリオド）キー**を押す → github.dev が開く
2. `src/calc.py` の `return a + b`（subtract）を `return a - b` に直す
3. `tests/test_calc.py` の test_subtract のコメントを外す
4. 左のソース管理アイコン → **新しいブランチ `fix/subtract` にコミットする**
5. GitHubに戻ると「Compare & pull request」が出る → クリックする
6. PRテンプレートが自動で入っているので、`fixes #1` と書く
7. まず **Create draft pull request** で作る

**確認すること**
- 【暗記】github.devにはターミナルがない（実行できない）
- 【暗記】Draft PRはマージボタンが押せない
- CODEOWNERSにより、レビュアーに自動で指定される仕組み（※自分が作ったPRには自分は指定されない）

---

## 演習3：Actionsを見る（10分）
1. PRの下部に、CIのチェックが表示される
2. **Actions** タブ → 実行結果 → `test` → 各Stepのログを開く
3. `report` が `test` の後に実行されている（needs:）ことを確認する
4. Actionsタブ → 左の「CI」→ **Run workflow** で手動実行する（workflow_dispatch）

**確認すること**
- 【暗記】Workflow / Event / Job / Step / Action / Runner の対応（`ci.yml` のコメント参照）

---

## 演習4：ブランチ保護を設定する（10分）
1. **Settings → Branches → Add branch ruleset**（または Add classic branch protection rule）
2. 対象：`main`
3. 次を有効にする
   - Require a pull request before merging（**承認数は0**のままにする ※1人だと自分のPRを承認できないため）
   - Require status checks to pass → `test` を追加する
4. ローカルからmainに直接pushしてみる → **拒否される**のを確認する

**確認すること**
- 【暗記】ブランチ保護でできること（PR必須、ステータスチェック必須、force push禁止）
- 【暗記】Rulesetsはタグにも適用できる

---

## 演習5：レビューしてマージする（10分）
1. PRで **Ready for review** を押す（Draftを解除）
2. **Files changed** → 行番号の「+」からコメントを付ける
3. **Review changes** を開き、Comment / Approve / Request changes の3つの選択肢を確認する（自分のPRなのでApproveは選べない）
4. マージボタンの▼から **Squash and merge** を選んでマージする
5. **Delete branch** を押す

**確認すること**
- Issue #1 が**自動でクローズ**されている ← 【暗記】fixes キーワード
- 【暗記】3種類のマージ方法、GitHub Flow の⑤マージ → ⑥ブランチ削除

---

## 演習6：Projectsを使う（10分）
1. 自分のプロフィール → **Projects → New project**
2. **Table / Board / Roadmap** を切り替えてみる
3. 「+ Add item」から gh900-practice のIssueを追加する
4. メニュー → **Workflows** で「Item closed → Status: Done」が有効になっていることを確認する
5. **Insights**（グラフのアイコン）を開く

**確認すること**
- 【暗記】Projectsはユーザー／Organizationの単位で作る（リポジトリの中ではない）
- 【暗記】Iterationフィールド（スプリント）の追加画面も見ておく

---

## 演習7：設定・Insightsを見る（10分）
| 見る場所 | 確認すること |
|---|---|
| Settings → General の下部（Danger Zone） | 公開範囲の変更（Public / Private） |
| Settings → Collaborators | 招待時のロール（個人リポジトリでは選べない。Organizationのリポジトリでは Read / Triage / Write / Maintain / Admin） |
| Insights → Pulse / Contributors / Traffic | 活動状況・閲覧数 |
| Insights → Dependency graph | 依存関係 |
| 右上の Watch ▼ | Participating / All Activity / Ignore / Custom |
| 右上の Star | ブックマーク |
| Settings → General → Features | Wiki / Discussions / Projects のオン・オフ |

---

## 演習8：その他の機能（15分）
1. **Discussions**：Settingsで有効にする → カテゴリ（Q&A、Ideasなど）を確認し、Q&Aの投稿で「Mark as answer」を見る
2. **Wiki**：ページを1つ作る
3. **GitHub Pages**：Settings → Pages → Branch `main` / `/(root)` → 数分で `https://<ユーザー名>.github.io/gh900-practice/` が表示される
4. **Gist**：https://gist.github.com で「Create secret gist」を作り、ログアウトした状態（シークレットウィンドウ）でURLを開くと見られることを確認する
5. **Codespaces**（任意）：Code ▼ → Codespaces → Create。devcontainer.json に従ってテストが自動実行され、ターミナルが使える
   - ⚠ 無料枠を使うので、終わったら **停止・削除する**（https://github.com/codespaces）

---

## 演習9：Forkを体験する（5分）
1. GitHub公式のフォーク練習用リポジトリ https://github.com/octocat/Spoon-Knife を開く
2. **Fork** を押す → 自分のアカウントにコピーされる
3. フォーク先の画面に「forked from octocat/Spoon-Knife」と出ていることを確認する

**確認すること**
- 【暗記】Fork＝GitHub上のコピー（元とつながっている）、Clone＝ローカルへのコピー
- 比較用に gh900-practice を **Settings → Template repository** にして「Use this template」から新しく作ると、**履歴が引き継がれない**ことも確認できる
