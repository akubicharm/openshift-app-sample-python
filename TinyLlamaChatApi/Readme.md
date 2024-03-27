# TinyLlamaをAPIで利用するためのサンプル

## デプロイ方法

Dockerbuildのストラテジを使って、TinyLlamaのモデルを含んだコンテナを作成する。

## 使い方

JSON形式のデータをPOSTで送ると、TinyLlamaからメッセージをテキストで返す。

{
    "text": "I am glad today to give an update on the current efforts to enable new Regions for OSD on GCP.The GCP Region 'asia-south2 (Delhi)' is now enabled and can now be used for deploying OSD clusters.The region was also added to the service definition in our official documentation",
    "system": "Summarize message."
}