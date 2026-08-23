# 配送方法を切り替える注文プログラム

標準配送と速達配送を切り替えられる注文プログラムを完成させる課題です。

継承を使うのはis-aの関係だけにし、`super()`とoverrideで配送方法の共通部分と差分を実装します。注文と配送方法のhas-aの関係はcompositionで表し、具体的な配送方法を判定する条件分岐を使わずに処理します。

## 利用バージョン

- Python 3.14.7
- pytest 9.1.1
- Ruff 0.16.1

## 環境構築

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install -r requirements-dev.txt
```

WindowsのPowerShellでは、次のcommandで仮想環境を有効にします。

```powershell
PS> .venv\Scripts\Activate.ps1
```

## 実装対象

- `shipping_app/shipping.py`
- `shipping_app/order.py`
- `DESIGN.md`

Python fileの`TODO`を確認し、`pass`を実装へ置き換えてください。class名、method名、戻り値の形式は変更しません。実装後は、`DESIGN.md`へ継承、composition、polymorphismを選んだ理由を記述します。

## 自動判定

```bash
$ python -m pytest
```

すべてのtestが成功したら、通常のcommandで配送方法ごとの結果を確認します。

```bash
$ python -m shipping_app.main
```

期待する結果は次のとおりです。

```text
標準配送 | 配送料: 500円 | 支払合計: 12,500円 | 2〜4日でお届け
速達配送 | 配送料: 1,300円 | 支払合計: 13,300円 | 翌日お届け
```
