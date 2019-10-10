# TODOlist_work

## 参考

    ・ https://www.atmarkit.co.jp/ait/articles/1807/31/news042.html


## 確認
    ・ http://127.0.0.1:5000/


### めも

* cssの変更が効かないとき

検証⇒ Network ⇒ Disable cache　をチェック

* htmlのなぞについて

```bash
<a href="javascript:document.myform.submit()" class="button">submit</a>
# 検証のしたのターミナル？で
document.myform.submit()
# と同じ効果

<a href="/deletealldoneitems" class="button">delete all done items</a>
# リストを[done]して以下にアクセスするのと同じ効果
http://127.0.0.1:5000/deletealldoneitems
```
