langfuse + langchainをdocker-composeとdevcontainerでいい感じに使うテンプレリポジトリ

devcontainer側で3000番ポートを使いたい時はdocker-composeを書き換えること

手順
1. VSCodeで開く
2. devcontainerで開く
3. http://localhost:3000で開く
4. langfuseの初期設定をする
5. llm-batchフォルダ内に.envファイルを用意して以下の環境変数を設定する
```
LANGFUSE_SECRET_KEY=langfuseにあるシークレットキーをここにコピペ(APIキーを作った時だけしか見れないので注意)
LANGFUSE_PUBLIC_KEY=langfuseにあるパブリックキーをここにコピペ
LANGFUSE_HOST=http://langfuse-server:3000 <- ここのポート番号はdocker-composeを書き換えた場合は変更したポート番号にする
```
6. llm-batchフォルダ内でuv syncをして必要なライブラリをインストールする
7. python main.pyを実行するとlangfuseに実行結果が記録される
